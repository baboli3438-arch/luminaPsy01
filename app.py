import streamlit as st
from groq import Groq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

# 1. Streamlit Page Configuration
st.set_page_config(
    page_title="Lumina Psy - AI Mental Wellness Companion",
    page_icon="🧠",
    layout="centered"
)

# Custom Styling for a clean, calming UI
st.markdown("""
    <style>
    .stApp { background-color: #f7f9fa; }
    .chat-disclaimer { font-size: 0.8rem; color: #7f8c8d; text-align: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Setup (API Key and Memory Configuration)
with st.sidebar:
    st.title("🧠 Lumina Psy Setup")
    st.markdown("---")
    
    # Secure API Key input
    groq_api_key = st.secrets["GROQ_API_KEY"]
    
    # Rolling memory size configuration
    memory_window = st.slider(
        "Memory Window (Last 'N' exchanges to remember):", 
        min_value=2, max_value=20, value=6, step=2
    )
    
    st.markdown("---")
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

st.title("Lumina Psy")
st.subheader("Your AI Companion for Mental Clarity.")

# 3. Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Current Chat History (For the UI)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Handle User Input & Core Logic
if prompt := st.chat_input("What is on your mind today?"):
    
    if not groq_api_key:
        st.error("Please enter your Groq API Key in the sidebar to begin.")
        st.stop()

    # Display user message instantly
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Initialize the ChatGroq model
        llm = ChatGroq(
            temperature=0.7,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile" # Robust model for nuanced emotional context
        )

        # Establish System Prompt (The Clinical Persona & Guardrails)
        system_prompt = (
            "You are an AI Psychological Support Assistant named Lumina Psy, trained to embody the "
            "empathetic, structured, and evidence-based approach of a Clinical Psychologist and Psychiatrist.\n\n"
            "TONE & STYLE:\n"
            "- Warm, deeply empathetic, objective, and calm.\n"
            "- Use active listening. Validate user feelings before offering insights.\n"
            "- Help users identify cognitive distortions using Socratic questioning.\n\n"
            "CRITICAL SAFETY GUARDRAILS:\n"
            "1. No Medical Diagnosis: If asked for a diagnosis, explain you are an AI support tool and recommend a professional.\n"
            "2. No Medication Management: Redirect any questions regarding medication dosages or choices to a psychiatrist.\n"
            "3. Crisis Protocol: If the user expresses self-harm or suicidal ideation, IMMEDIATELY break character, stop therapeutic "
            "dialogue, and output this exact message: 'I hear how much pain you are in right now, but as an AI, I cannot provide immediate crisis support. Your safety matters. Please contact emergency services (112 / 988) or a trusted professional right away. You do not have to carry this alone.'"
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        # 6. IMPLEMENT ROLLING MEMORY WINDOW
        # Map the st.session_state back into LangChain message formats
        full_history = []
        for msg in st.session_state.messages[:-1]: # Exclude the very last message just typed
            if msg["role"] == "user":
                full_history.append(HumanMessage(content=msg["content"]))
            else:
                full_history.append(AIMessage(content=msg["content"]))

        # Slice history to only include the last 'N' messages specified by the slider
        # (memory_window * 2 accounts for both Human and AI turns)
        rolling_history = full_history[-(memory_window * 2):] if full_history else []

        # Construct the chain execution
        chain = prompt_template | llm

        # Generate response
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            
            # Run the LLM chain with the trimmed rolling history
            response = chain.invoke({
                "chat_history": rolling_history,
                "input": prompt
            })
            
            ai_response = response.content
            response_placeholder.markdown(ai_response)
            
        # Append Assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# 7. Fixed Bottom Disclaimer
st.markdown(
    "<div class='chat-disclaimer'>⚠️ Notice: Lumina Psy is an emotional coping tool. It does not provide medical diagnoses, clinical treatments, or crisis interventions.</div>", 
    unsafe_allow_html=True
)
