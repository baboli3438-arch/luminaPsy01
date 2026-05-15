import streamlit as st
import os
from groq import Groq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

# --- 1. CONFIG & API SETUP ---
st.set_page_config(
    page_title="Lumina Psy | AI Virtual Clinic",
    page_icon="🌿",
    layout="wide"
)

# API Key doğrudan Streamlit Secrets üzerinden çekiliyor
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    # Eğer localde çalıştırıyorsan ve secrets yoksa hata vermemesi için .env kontrolü (Yedek Plan)
    groq_api_key = os.getenv("GROQ_API_KEY")

# --- 2. BLUWHALE INSPIRED DESIGN (CSS) ---
def apply_bluwhale_design():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Spline+Sans:wght@400;500;700&display=swap');
        
        .stApp {
            background-color: #030712;
            font-family: 'Spline Sans', sans-serif;
            color: #E2E8F0;
        }

        .main-title {
            font-weight: 700;
            color: #FFFFFF;
            text-align: center;
            font-size: 3.5rem;
            letter-spacing: -2px;
            margin-bottom: 0px;
            margin-top: -50px;
        }
        
        .sub-title {
            color: #9CA3AF;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 400;
            margin-bottom: 50px;
        }

        .stChatMessage {
            background-color: #111827 !important;
            border: 1px solid #1F2937;
            border-radius: 12px !important;
            margin-bottom: 15px;
            padding: 20px;
        }
        
        [data-testid="stChatMessageUser"] {
            border-left: 4px solid #3B82F6 !important;
        }

        .stChatInputContainer {
            background-color: #111827 !important;
            border: 1px solid #1F2937 !important;
            border-radius: 12px !important;
        }

        [data-testid="stSidebar"] {
            background-color: #030712;
            border-right: 1px solid #1F2937;
        }

        .feature-card {
            background: rgba(17, 24, 39, 0.5);
            padding: 25px;
            border-radius: 12px;
            text-align: left;
            border: 1px solid #1F2937;
            transition: all 0.3s ease;
        }
        .feature-card:hover {
            border-color: #3B82F6;
            background: rgba(59, 130, 246, 0.05);
        }

        .stButton>button {
            border-radius: 8px;
            background-color: #1F2937;
            color: white;
            border: 1px solid #374151;
            transition: all 0.2s;
        }
        .stButton>button:hover {
            background-color: #3B82F6;
            border-color: #3B82F6;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

apply_bluwhale_design()

# --- 3. HERO SECTION (GİRİŞ) ---
welcome_container = st.container()
with welcome_container:
    _, mid_col, _ = st.columns([1, 4, 1])
    with mid_col:
        st.markdown("<h1 class='main-title'>Lumina Psy</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-title'>Your Professional AI Companion for Emotional Resilience.</p>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="feature-card"><h3>🔒 Secure</h3>Conversations are encrypted and private.</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="feature-card"><h3>⚡ Instant</h3>Access priority support 24/7.</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="feature-card"><h3>🧠 Clinical</h3>Based on CBT & ACT methodologies.</div>', unsafe_allow_html=True)
        
        st.write("")
        st.divider()

# --- 4. CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Start typing your thoughts..."):
    if not groq_api_key:
        st.error("⚠️ GROQ_API_KEY is missing. Please check your Streamlit Secrets settings.")
        st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        llm = ChatGroq(
            temperature=0.6,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )

        system_prompt = (
            "You are Lumina Psy, a warm, professional, and empathetic Clinical Psychologist AI. "
            "Use Socratic questioning and CBT techniques. Maintain a focus on mental wellness."
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        full_history = [
            HumanMessage(content=m["content"]) if m["role"] == "user" else AIMessage(content=m["content"])
            for m in st.session_state.messages[:-1]
        ]
        rolling_history = full_history[-10:] 

        chain = prompt_template | llm
        
        with st.chat_message("assistant"):
            with st.spinner("Reflecting..."):
                response = chain.invoke({"chat_history": rolling_history, "input": prompt})
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})

    except Exception as e:
        st.error(f"Connection issue: {str(e)}")

# --- 5. SIDEBAR (MINIMAL) ---
with st.sidebar:
    st.markdown("### 🌿 Lumina Controls")
    st.caption("AI Session Status: Active")
    st.write("")
    if st.button("Reset Session", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("© 2026 Lumina Health")

# --- 6. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚠️ Lumina is an AI support tool and not a substitute for medical intervention or crisis care.")
