import streamlit as st
from groq import Groq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

# 1. SAYFA AYARLARI VE GÖRSEL KİMLİK
st.set_page_config(
    page_title="Lumina Psy | AI Mental Wellness",
    page_icon="🧠",
    layout="centered"
)

# Profesyonel CSS Tasarımı
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main-title {
            font-weight: 700;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 5px;
        }
        
        .sub-title {
            color: #6B7280;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 30px;
        }

        .stChatMessage {
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 10px;
        }

        .footer {
            font-size: 0.8rem;
            color: #9CA3AF;
            text-align: center;
            padding: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

local_css()

# 2. YAN PANEL (SIDEBAR) REHBERİ
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/brain.png", width=70)
    st.title("Lumina Control")
    
    # API Anahtarı Girişi
    groq_api_key = st.text_input("Groq API Key", type="password", help="Get your key at console.groq.com")
    
    # Bellek Ayarı
    memory_window = st.select_slider(
        "Memory Depth (Contextual History):",
        options=[2, 4, 6, 8, 10],
        value=6
    )
    
    st.markdown("---")
    st.markdown("### 🧘 Quick Relief")
    if st.button("4-7-8 Breathing Technique"):
        st.info("Inhale for 4s... Hold for 7s... Exhale for 8s... Repeat.")
        
    if st.button("Clear History"):
        st.session_state.messages = []
        st.rerun()

# 3. GİRİŞ EKRANI (HERO SECTION)
st.markdown("<h1 class='main-title'>Lumina Psy</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Your professional partner for emotional resilience and clarity.</p>", unsafe_allow_html=True)

# Bilgi Kartları
col1, col2, col3 = st.columns(3)
with col1:
    st.success("🔒 **Private**\n\nSecure Session")
with col2:
    st.warning("⚡ **Fast**\n\nReal-time AI")
with col3:
    st.info("🧠 **Expert**\n\nCBT Framework")

st.divider()

# 4. SOHBET GEÇMİŞİ YÖNETİMİ
if "messages" not in st.session_state:
    st.session_state.messages = []

# Geçmiş mesajları ekrana bas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. ANA MANTIK VE API ÇAĞRISI
if prompt := st.chat_input("How are you feeling today?"):
    
    if not groq_api_key:
        st.error("Please provide your Groq API Key in the sidebar.")
        st.stop()

    # Kullanıcı mesajını göster
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # GÜNCEL MODEL: llama-3.3-70b-versatile
        llm = ChatGroq(
            temperature=0.6,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )

        # Uzman Sistem Talimatı
        system_message = (
            "You are Lumina Psy, a highly empathetic AI Assistant with expertise in Clinical Psychology and Psychiatry. "
            "Your goal is to provide evidence-based emotional support using CBT and ACT principles. "
            "STRICT RULES:\n"
            "1. Validate emotions before analyzing.\n"
            "2. Never provide a clinical diagnosis or prescribe drugs.\n"
            "3. If self-harm is mentioned, stop therapy and provide emergency hotline info immediately.\n"
            "4. Keep responses concise, fluent, and professional."
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_message),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        # Rolling Memory Hazırlığı
        full_history = []
        for msg in st.session_state.messages[:-1]:
            if msg["role"] == "user":
                full_history.append(HumanMessage(content=msg["content"]))
            else:
                full_history.append(AIMessage(content=msg["content"]))

        rolling_history = full_history[-(memory_window * 2):] if full_history else []

        # Zinciri Çalıştır
        chain = prompt_template | llm
        
        with st.chat_message("assistant"):
            with st.spinner("Reflecting on your thoughts..."):
                response = chain.invoke({
                    "chat_history": rolling_history,
                    "input": prompt
                })
                ai_content = response.content
                st.markdown(ai_content)
        
        st.session_state.messages.append({"role": "assistant", "content": ai_content})

    except Exception as e:
        st.error(f"System update in progress or API error: {str(e)}")

# 6. YASAL UYARI (FOOTER)
st.markdown("---")
st.markdown(
    "<div class='footer'>⚠️ <b>Disclaimer:</b> Lumina Psy is an AI-based wellness tool. It is NOT a replacement for professional medical advice, diagnosis, or emergency psychiatric care. If you are in crisis, please call emergency services immediately.</div>", 
    unsafe_allow_html=True
)
