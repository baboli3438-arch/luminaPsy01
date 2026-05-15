import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. AYARLAR VE API ANAHTARI ---
st.set_page_config(page_title="Lumina Psy", page_icon="🌿", layout="wide")

# İstediğin o özel satır: API anahtarını doğrudan Streamlit Secrets'tan alır
groq_api_key = st.secrets["GROQ_API_KEY"]

# --- 2. BLUWHALE TARZI TASARIM (CSS) ---
st.markdown("""
    <style>
    /* Bluwhale Koyu Tema */
    .stApp {
        background-color: #030712;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Başlık Stili */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        color: #FFFFFF;
        letter-spacing: -2px;
        margin-top: -40px;
    }
    
    /* Bluwhale Mavisi Vurgulu Kartlar */
    .feature-card {
        background: #111827;
        border: 1px solid #1F2937;
        padding: 20px;
        border-radius: 12px;
        text-align: left;
        transition: 0.3s;
    }
    .feature-card:hover {
        border-color: #3B82F6;
    }

    /* Sohbet Balonları */
    .stChatMessage {
        background-color: #111827 !important;
        border: 1px solid #1F2937;
        border-radius: 10px !important;
    }
    
    /* Input Alanı */
    .stChatInputContainer {
        background-color: #111827 !important;
        border: 1px solid #3B82F6 !important;
    }

    /* Streamlit yazılarını gizle */
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. ARAYÜZ (GİRİŞ) ---
st.markdown("<h1 class='main-title'>Lumina Psy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9CA3AF;'>AI-Powered Emotional Intelligence Platform</p>", unsafe_allow_html=True)

# Bluwhale Tarzı 3'lü Bölüm
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="feature-card"><h4>🔒 Private</h4>Secure and anonymous sessions.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="feature-card"><h4>⚡ Real-time</h4>Instant AI-driven insights.</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="feature-card"><h4>🧠 Expert</h4>Built on clinical CBT frameworks.</div>', unsafe_allow_html=True)

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
if prompt := st.chat_input("Düşüncelerini buraya yazabilirsin..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # LLM Yapılandırması (llama-3.3-70b-versatile)
        llm = ChatGroq(
            temperature=0.6,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are Lumina Psy, an empathetic clinical psychologist AI. Provide support using CBT principles."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        # Bellek Yönetimi (Son 10 mesaj)
        history = [
            HumanMessage(content=m["content"]) if m["role"] == "user" else AIMessage(content=m["content"])
            for m in st.session_state.messages[:-1]
        ]

        chain = prompt_template | llm
        
        with st.chat_message("assistant"):
            with st.spinner("Düşünüyor..."):
                response = chain.invoke({"chat_history": history[-10:], "input": prompt})
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})

    except Exception as e:
        st.error(f"Bir hata oluştu: {str(e)}")

# Sidebar
with st.sidebar:
    st.markdown("### Lumina Care")
    if st.button("Sohbeti Sıfırla"):
        st.session_state.messages = []
        st.rerun()
