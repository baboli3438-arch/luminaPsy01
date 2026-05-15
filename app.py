import streamlit as st
from groq import Groq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="Lumina Psy | Virtual Clinic",
    page_icon="🌿",
    layout="centered"
)

# 2. GELİŞMİŞ GÖRSEL TASARIM (CSS)
def apply_custom_design():
    st.markdown("""
        <style>
        /* Modern Arka Plan ve Yazı Tipi */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        /* Başlık ve Alt Başlık */
        .main-title {
            font-weight: 800;
            background: -webkit-linear-gradient(#1e3a8a, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 0px;
        }
        
        .sub-title {
            color: #4b5563;
            text-align: center;
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: 40px;
        }

        /* Sohbet Balonları */
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.7) !important;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 20px !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            margin-bottom: 15px;
        }
        
        /* Kullanıcı Mesajı Farklılaştırma */
        [data-testid="stChatMessageUser"] {
            background-color: rgba(59, 130, 246, 0.1) !important;
        }

        /* Sidebar Güzelleştirme */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.9);
            border-right: 1px solid #e5e7eb;
        }

        /* Kartlar (Features) */
        .feature-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            border: 1px solid #f3f4f6;
        }
        
        /* Butonlar */
        .stButton>button {
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_design()

# 3. SIDEBAR (YAN PANEL)
with st.sidebar:
    st.markdown("### 🌿 Lumina Care")
    groq_api_key = st.text_input("Groq API Key", type="password")
    
    st.divider()
    st.markdown("#### Mindful Tools")
    if st.button("🧘 1 Minute Breathing"):
        st.toast("Breath in... 2... 3... 4... and out...", icon="🌬️")
        
    st.markdown("---")
    st.caption("Developed with empathy for a better mind.")
    if st.button("Reset Session", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# 4. GİRİŞ EKRANI (HERO)
st.markdown("<h1 class='main-title'>Lumina Psy</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Safe. Professional. Always here.</p>", unsafe_allow_html=True)

# Görsel Kartlar
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="feature-card"><b>🔒 Encrypted</b><br>Private Chat</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="feature-card"><b>☁️ Calm</b><br>Safe Space</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="feature-card"><b>⚡ Fast</b><br>Instant Care</div>', unsafe_allow_html=True)

st.write("") # Boşluk
st.divider()

# 5. SOHBET MANTIĞI
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mesajları Ekrana Bas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcı Girişi
if prompt := st.chat_input("Speak your mind..."):
    if not groq_api_key:
        st.warning("Please enter your API key to start.")
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
            "You are Lumina Psy, a warm and professional Clinical Psychologist AI. "
            "Your tone is soft, welcoming, and clinically grounded. Use CBT techniques. "
            "Keep it empathetic and safe."
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])

        # Rolling Memory (Last 6 turns)
        full_history = [
            HumanMessage(content=m["content"]) if m["role"] == "user" else AIMessage(content=m["content"])
            for m in st.session_state.messages[:-1]
        ]
        rolling_history = full_history[-12:] 

        chain = prompt_template | llm
        
        with st.chat_message("assistant"):
            with st.spinner("Listening carefully..."):
                response = chain.invoke({"chat_history": rolling_history, "input": prompt})
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})

    except Exception as e:
        st.error(f"Connection issue: {str(e)}")

# 6. ALT BİLGİ
st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚠️ Lumina is an AI support tool and not a substitute for medical intervention.")
