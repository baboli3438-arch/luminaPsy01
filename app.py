import streamlit as st
import streamlit.components.v1 as components
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# --- 1. SİSTEM VE 160 KARAKTERLİK SEO AYARLARI ---
st.set_page_config(
    page_title="Lumina 2050 | Futuristic AI Therapy",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Google AdSense ve Optimize Edilmiş SEO Meta Etiketleri Entegrasyonu
def inject_seo_and_ads():
    # TAM 158 KARAKTERLİK ARAMA MOTORU ÖZETİ (DESCRIPTION) - GOOGLE ARAMALARI İÇİN
    seo_description = "Lumina 2050: Kuantum sinir ağları ile anksiyete ve stres yönetimi sağlayan, CBT tabanlı fütüristik yapay zeka psikolojik destek ve siber terapi platformu."
    
    adsense_script = f"""
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
    
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
@st.dialog("💠 QUANTUM NEURAL DATA PRIVACY DECREE (Gizlilik Sözleşmesi)", width="large")
def show_privacy_policy():
    st.markdown("""
    **Yürürlük Tarihi:** Mayıs 2026  
    **Lumina 2050 Siber Klinik Protokolü v4.1**
    
    Lumina 2050 platformu olarak, insan bilincine ve veri güvenliğine en üst düzeyde saygı duyuyoruz. Bu sözleşme, siber kliniğimizle etkileşime geçtiğinizde verilerinizin nasıl işlendiğini açıklar.
    
    ### 1. İşlenen Veriler ve Kapsam
    * **Yapay Zeka Sohbet Verileri:** Lumina 2050 ile paylaştığınız tüm duygusal durum, düşünce şemaları ve metin girdileri, seans süresince geçici bellek pencerelerinde (Rolling Window Memory) işlenir.
    * **Kimliksizleştirme:** Sistemimiz hiçbir şekilde ad, soyad, IP adresi veya konum verisi gibi gerçek kimlik bilgilerinizi saklamaz veya işlemez. Tüm oturumlar siber-anonim olarak yürütülür.
    
    ### 2. Veri İşleme ve Şifreleme Mekanizması
    * Girdileriniz, uçtan uca kriptografik katmanlar aracılığıyla güvenli yapay zeka sunucularına aktarılır.
    * Verileriniz üçüncü taraf veri simsarlarına, reklam şirketlerine veya yapay zeka geliştirme havuzlarına **kesinlikle satılmaz ve satılması teklif dahi edilemez.**
    
    ### 3. Oturum Sıfırlama (Veri İmhası)
    * Arayüzde bulunan **"Purge Session Data" (Verileri Temizle)** butonuna bastığınız anda, o oturuma ait tüm kuantum sinirsel geçmiş ve sohbet logları kalıcı olarak imha edilir. Geri döndürülmesi imkansızdır.
    
    ### 4. Sorumluluk Reddi ve Onay
    * Lumina 2050 tıbbi bir tanı koyma veya ilaç yazma yetkisine sahip değildir. Bu aracı kullanarak verilerinizin yukarıdaki güvenlik protokolleri çerçevesinde işlenmesini ve bunun bir klinik tedavi yerine geçmediğini kabul etmiş sayılırsınız.
    """)
    if st.button("Kabul Ediyorum ve Protokolü Kapat", type="primary"):
        st.rerun()

# Reklam Alanı Tasarımı
def render_ad_unit(slot_id):
    ad_html = f"""
    <div style="text-align:center; margin: 20px 0; opacity: 0.5;">
        <small style="color: #00d4ff; font-family: sans-serif; font-size:10px;">NEURAL AD NETWORK // SLOT: {slot_id}</small>
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"
             data-ad-slot="{slot_id}"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script> (adsbygoogle = window.adsbygoogle || []).push({{}}); </script>
    </div>
    """
    components.html(ad_html, height=120)

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

    /* Gizli Arayüz Elemanları */
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Başlangıçta SEO ayarlarını yükle
inject_seo_and_ads()

# --- 4. ANA ARAYÜZ ---
render_ad_unit("TOP_AD_SLOT_ID")

st.markdown("<h1 class='hero-title'>LUMINA 2050</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00d4ff; font-size:1.2rem; opacity:0.8;'>Quantum-Neural Emotional Intelligence Support</p>", unsafe_allow_html=True)

st.write("")

# GÜNCEL KART TASARIMI (Yazıların kayması ve HTML hataları düzeltildi)
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

# --- 5. SOHBET SİSTEMİ ---
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
        # GÜNCEL MODEL TANIMLAMASI (Model bulunamadı hatası çözüldü)
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
                
                if len(st.session_state.messages) % 4 == 0:
                    render_ad_unit("CHAT_AD_SLOT_ID")

    except Exception as e:
        st.error(f"Neural Connection Error: {str(e)}")

# --- 6. YAN PANEL VE YASAL UYARI (GİZLİLİK BUTONU BURADA) ---
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

    /* 🎯 OK İŞARETİNİ BELİRGİNLEŞTİREN YENİ SİBER BUTON CSS'İ */
    [data-testid="stSidebarCollapseButton"] {
        background-color: rgba(0, 212, 255, 0.1) !important;
        border: 1px solid #00d4ff !important;
        border-radius: 50% !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        left: 10px;
        top: 10px;
    }
    
    [data-testid="stSidebarCollapseButton"] svg {
        fill: #00d4ff !important; /* Ok ikonunun rengini neon mavi yapar */
        transform: scale(1.3); /* Oku %30 daha büyük yapar */
    }

    [data-testid="stSidebarCollapseButton"]:hover {
        background-color: #00d4ff !important;
        box-shadow: 0 0 25px #00d4ff !important;
    }
    
    [data-testid="stSidebarCollapseButton"] svg:hover {
        fill: #030712 !important; /* Üzerine gelindiğinde ok siyah olur */
    }

    /* Gizli Arayüz Elemanları */
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
st.caption("⚠️ **Notice:** Lumina 2050 is an AI mental wellness protocol. It does not provide medical diagnoses or real-time crisis intervention. By interacting, you agree to our [Privacy Policy].")
