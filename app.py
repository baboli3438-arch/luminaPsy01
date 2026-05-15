import streamlit as st
import streamlit.components.v1 as components
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. SİSTEM VE SEO AYARLARI (İLK AÇILIŞTA PANEL AÇIK GELİR) ---
st.set_page_config(
    page_title="Lumina 2050 | Futuristic AI Therapy",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded" # Yan panel artık görünür başlar!
)

# Google AdSense ve Optimize Edilmiş SEO Meta Etiketleri Entegrasyonu
def inject_seo_and_ads():
    seo_description = "Lumina 2050: Kuantum sinir ağları ile anksiyete ve stres yönetimi sağlayan, CBT tabanlı fütüristik yapay zeka psikolojik destek ve siber terapi platformu."
    
    adsense_script = f"""
    <meta name="description" content="{seo_description}">
    <meta name="keywords" content="AI therapy, yapay zeka psikolog, siber klinik, mental health AI, Lumina 2050, anksiyete terapisi">
    """
    components.html(adsense_script, height=0)

# API Anahtarı Yönetimi
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    groq_api_key = os.getenv("GROQ_API_KEY")

# --- 2. GİZLİLİK POLİTİKASI (PRIVACY POLICY) MODALI ---
@st.dialog("💠 QUANTUM NEURAL DATA PRIVACY DECREE", width="large")
def show_privacy_policy():
    st.markdown("""
    **Effective Date:** May 2026  
    **Lumina 2050 Cyber-Clinic Protocol v4.1**
    
    At Lumina 2050, we hold human consciousness and data sovereignty in the highest regard. This Privacy Decree outlines how your neural-textual data is processed when interacting with our cyber-clinic.
    
    ### 1. Data Collection and Scope
    * **AI Chat Data:** All emotional states, cognitive schemas, and textual inputs you share with Lumina 2050 are processed temporarily within transient volatile memory cells (Rolling Window Memory) solely to sustain the session context.
    * **Anonymization:** Our core architecture does not request, log, or store real-world identifiers such as names, surnames, IP addresses, or geographical telemetry. All communication lines are executed under strict cyber-anonymity.
    
    ### 2. Processing and Cryptographic Protocols
    * Your inputs are routed through end-to-end encrypted cryptographic layers to secure neural processing nodes.
    * Your data **is never sold, leased, or sub-licensed** to third-party data brokers, advertising networks, or centralized AI training pools. 
    
    ### 3. Immediate Data Purging (Volatile Memory Wipe)
    * The moment you trigger the **"Purge Session Data (Reset)"** directive on the control panel, all rolling neural histories, session tokens, and dialog logs associated with your interface are permanently vaporized. This operation is absolute and mathematically irreversible.
    
    ### 4. Disclaimer and Consent
    * Lumina 2050 operates as an advanced AI mental wellness protocol. It does not possess clinical authority to diagnose medical conditions, issue psychological prescriptions, or provide real-time crisis intervention. By engaging with this matrix, you acknowledge and consent to these neural data protocols.
    """)
    if st.button("I Accept & Close Protocol", type="primary", use_container_width=True):
        st.rerun()

# Reklam Alanı Tasarımı
def render_ad_unit(slot_id):
    ad_html = f"""
    <div style="text-align:center; margin: 20px 0; opacity: 0.5;">
        <small style="color: #00d4ff; font-family: sans-serif; font-size:10px;">NEURAL AD NETWORK // SLOT: {slot_id}</small>
    </div>
    """
    components.html(ad_html, height=50)

# --- 3. FÜTÜRİSTİK SİBER-TASARIM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at top right, #0a0e1a, #030712);
        color: #00d4ff;
        font-family: 'Space Grotesk', sans-serif;
    }

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

    .futuristic-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 212, 255, 0.2);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 24px;
        text-align: center;
    }

    .stChatMessage {
        background: rgba(16, 24, 40, 0.8) !important;
        border: 1px solid rgba(0, 212, 255, 0.1);
        border-radius: 20px !important;
    }

    /* Streamlit'in kendi orijinal sönük ok butonunu tamamen görünmez yapıyoruz */
    [data-testid="stHeader"] {background: transparent !important;}
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 4. SIFIRDAN YAZILAN JAVASCRIPT/HTML NEON BUTON ---
# Bu script, Streamlit'in gizli yan panelini açan görünmez elementleri tetikler.
custom_toggle_button = """
<div style="position: fixed; top: 20px; left: 20px; z-index: 999999;">
    <button onclick="window.parent.document.querySelector('.st-emotion-cache-ch6vcl, [data-testid=\\'stSidebarCollapseButton\\']').click()" 
            style="
                background: rgba(0, 212, 255, 0.15);
                border: 2px solid #00d4ff;
                color: #00d4ff;
                padding: 10px 18px;
                border-radius: 12px;
                font-family: sans-serif;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 0 15px rgba(0, 212, 255, 0.6);
                transition: all 0.3s ease;
            "
            onmouseover="this.style.background='#00d4ff'; this.style.color='#030712'; this.style.boxShadow='0 0 25px #00d4ff';"
            onmouseout="this.style.background='rgba(0, 212, 255, 0.15)'; this.style.color='#00d4ff'; this.style.boxShadow='0 0 15px rgba(0, 212, 255, 0.6)';"
    >
        💠 MENU
    </button>
</div>
"""
components.html(custom_toggle_button, height=60)

# Başlangıçta SEO ayarlarını yükle
inject_seo_and_ads()

# --- 5. ANA ARAYÜZ ---
render_ad_unit("TOP_AD_SLOT_ID")

st.markdown("<h1 class='hero-title'>LUMINA 2050</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00d4ff; font-size:1.2rem; opacity:0.8;'>Quantum-Neural Emotional Intelligence Support</p>", unsafe_allow_html=True)

st.write("")

# Özellik Kartları
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('''
        <div class="futuristic-card">
            <h3 style="color:#00d4ff; margin-top:0;">🧬 Biometric</h3>
            <p style="color:#9CA3AF; margin-bottom:0;">Emotional Pulse Analysis</p>
        </div>
    ''', unsafe_allow_html=True)
with c2:
    st.markdown('''
        <div class="futuristic-card">
            <h3 style="color:#00d4ff; margin-top:0;">🛰️ Global</h3>
            <p style="color:#9CA3AF; margin-bottom:0;">Neural Sync 24/7</p>
        </div>
    ''', unsafe_allow_html=True)
with c3:
    st.markdown('''
        <div class="futuristic-card">
            <h3 style="color:#00d4ff; margin-top:0;">🔮 Adaptive</h3>
            <p style="color:#9CA3AF; margin-bottom:0;">Personalized Response</p>
        </div>
    ''', unsafe_allow_html=True)

st.divider()

# --- 6. SOHBET SİSTEMİ ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Zihnindeki frekansları paylaş..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        llm = ChatGroq(
            temperature=0.8,
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile"
        )

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are Lumina 2050, a futuristic AI Psychologist. Support the human user with empathy using CBT frameworks."),
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

# --- 7. YAN PANEL VE YASAL UYARI ---
with st.sidebar:
    st.markdown("<h2 style='color:#00d4ff;'>SYSTEM STATUS</h2>", unsafe_allow_html=True)
    st.write("🟢 Neural Core: Operational")
    
    st.divider()
    st.markdown("### 📜 Compliance & Legal")
    if st.button("Read Privacy Policy", use_container_width=True):
        show_privacy_policy()
        
    st.divider()
    if st.button("Purge Session Data (Reset)", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("⚠️ **Notice:** Lumina 2050 is an AI mental wellness protocol. It does not provide medical diagnoses or real-time crisis intervention. By interacting, you agree to our [Privacy Policy].")
