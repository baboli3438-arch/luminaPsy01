import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. SİSTEM AYARLARI ---
st.set_page_config(page_title="Lumina Psy | Future Clinic", page_icon="💠", layout="wide")

# API Anahtarı (İstediğin özel satır)
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    groq_api_key = os.getenv("GROQ_API_KEY")

# --- 2. FÜTÜRİSTİK SİBER-TASARIM (CSS) ---
st.markdown("""
    <style>
    /* Arka Plan: Hareketli Siber Gradyan */
    .stApp {
        background: radial-gradient(circle at top right, #0a0e1a, #030712);
        color: #00d4ff;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Başlık: Fütüristik Neon Efekti */
    .hero-title {
        font-size: 5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #00d4ff, #0055ff, #8000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -4px;
        margin-top: -60px;
        filter: drop-shadow(0 0 15px rgba(0, 212, 255, 0.4));
    }

    /* Fütüristik Kartlar (Glassmorphism) */
    .futuristic-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 212, 255, 0.2);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 24px;
        text-align: center;
        transition: 0.5s all ease;
    }
    .futuristic-card:hover {
        background: rgba(0, 212, 255, 0.08);
        border-color: #00d4ff;
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.2);
    }

    /* Mesaj Balonları: Siber Stil */
    .stChatMessage {
        background: rgba(16, 24, 40, 0.8) !important;
        border: 1px solid rgba(0, 212, 255, 0.1);
        border-radius: 0 20px 20px 20px !important;
        margin-bottom: 20px;
    }
    [data-testid="stChatMessageUser"] {
        background: rgba(0, 85, 255, 0.1) !important;
        border-right: 4px solid #00d4ff !important;
        border-radius: 20px 0 20px 20px !important;
    }

    /* Input Alanı: Glow (Işıltı) Efekti */
    .stChatInputContainer {
        border-radius: 50px !important;
        border: 1px solid rgba(0, 212, 255, 0.3) !important;
        background: rgba(3, 7, 18, 0.9) !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
    }

    /* Gizli Arayüz Elemanları */
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. ANA EKRAN (HERO) ---
st.markdown("<h1 class='hero-title'>LUMINA 2050</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00d4ff; font-size:1.2rem; opacity:0.8;'>Quantum-Neural Emotional Intelligence Support</p>", unsafe_allow_html=True)

st.write("")
st.write("")

# Fütüristik 3'lü Bölüm
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="futuristic-card"><h2 style="color:#00d4ff;">🧬 Biometric</h2>Analyze emotional pulse.</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="futuristic-card"><h2 style="color:#00d4ff;">🛰️ Global</h2>Connected to your mind 24/7.</div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="futuristic-card"><h2 style="color:#00d4ff;">🔮 Adaptive</h2>Personalized neural response.</div>', unsafe_allow_html=True)

st.write("")
st.write("")
st.divider()

# --- 4. SOHBET SİSTEMİ ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mesaj Geçmişini Göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Giriş ve Yanıt
if prompt := st.chat_input("Zihnindeki frekansları paylaş..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # LLM (En güçlü Groq modeli)
        llm = ChatGroq(
            temperature=0.8,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are Lumina 2050, a futuristic, highly advanced AI Clinical Psychologist. Use sophisticated but empathetic language. Help the human navigate their neural-emotional state."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        history = [
            HumanMessage(content=m["content"]) if m["role"] == "user" else AIMessage(content=m["content"])
            for m in st.session_state.messages[:-1]
        ]

        chain = prompt_template | llm
        
        with st.chat_message("assistant"):
            with st.spinner("🔄 Decoding neural patterns..."):
                response = chain.invoke({"chat_history": history[-10:], "input": prompt})
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})

    except Exception as e:
        st.error(f"Neural Connection Error: {str(e)}")

# --- 5. YAN PANEL ---
with st.sidebar:
    st.markdown("<h2 style='color:#00d4ff;'>SYSTEM STATUS</h2>", unsafe_allow_html=True)
    st.write("🟢 Neural Core: Operational")
    st.write("🔵 Encryption: Active")
    st.divider()
    if st.button("Purge Session Data (Reset)"):
        st.session_state.messages = []
        st.rerun()
