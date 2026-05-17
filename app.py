import streamlit as st
from google import genai

st.set_page_config(
    page_title="VetaSync Assistant – Scientific Animal Education AI",
    page_icon="🐾",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0f0e 0%, #1a1a18 100%);
        color: #f0f0f0;
    }
    
    [data-testid="stSidebar"] {
        background-color: rgba(20, 20, 19, 0.7);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    [data-testid="stSidebarContent"] {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }

    [data-testid="stSidebar"] .stMarkdown h1 {
        font-size: 1.5rem !important;
        margin-bottom: 0px !important;
        margin-top: -10px !important;
        font-weight: 600 !important;
        color: white !important;
    }

    [data-testid="stSidebar"] .stMarkdown p {
        font-size: 0.85rem !important;
        margin-bottom: 0px !important;
        opacity: 0.8;
    }

    [data-testid="stSidebar"] hr {
        margin: 0.5rem 0 !important;
        opacity: 0.2;
    }

    [data-testid="stSidebar"] h3 {
        margin-bottom: 0.4rem !important;
        font-size: 1rem !important;
        opacity: 0.9;
    }

    .stButton>button {
        background: rgba(255, 255, 255, 0.03);
        color: #dddddd;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 6px 14px;
        text-align: left;
        width: 100%;
        transition: all 0.2s ease;
        margin-bottom: 0.1rem;
        font-size: 0.85rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.2);
        color: white;
        transform: translateX(4px);
    }

    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(12px);
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 15px;
        padding: 15px !important;
    }

    [data-testid="stChatMessage"]:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }

    h1 {
        font-weight: 600 !important;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #ffffff, #888888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .emergency-box {
        animation: pulse 2s infinite;
        background: rgba(255, 50, 50, 0.1);
        border: 2px solid #ff3232;
        padding: 15px;
        border-radius: 15px;
        color: #ff5555;
        font-weight: 600;
        margin-bottom: 25px;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.9; }
        50% { transform: scale(1.01); opacity: 1; }
        100% { transform: scale(1); opacity: 0.9; }
    }

    .sidebar-footer {
        font-size: 0.75rem;
        color: #aaaaaa;
        margin-top: 2rem !important;
        padding-bottom: 15px !important;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# VetaSync Assistant")
    st.markdown("Asisten AI Edukasi Kesehatan Hewan")
    st.markdown("---")
    
    st.markdown("### 🐶 Topik Anjing")
    if st.button("🍼 Nutrisi Dasar & Sosialisasi Puppy"):
        st.session_state.quick_query = "Bagaimana panduan perawatan nutrisi dan sosialisasi anak anjing (puppy) menurut jurnal veteriner?"
    if st.button("🦷 Kesehatan Gigi & Periodontal"):
        st.session_state.quick_query = "Jelaskan pentingnya dental prophylaxis pada anjing dan risiko penyakit periodontal berdasarkan studi ilmiah."
    if st.button("👴 Perawatan Fisio-Nutrisi Anjing Senior"):
        st.session_state.quick_query = "Apa saja perubahan fisiologis dan nutrisi yang dibutuhkan anjing lansia (senior dog)?"
    if st.button("🦟 Pencegahan Penyakit Cacing Jantung"):
        st.session_state.quick_query = "Jelaskan siklus hidup dan pencegahan penyakit cacing jantung (heartworm) pada anjing."

    st.markdown("---")
    st.markdown("### 🐱 Topik Kucing")
    if st.button("🍼 Imunisasi & Nutrisi Awal Kitten"):
        st.session_state.quick_query = "Apa standar nutrisi dan imunisasi awal untuk anak kucing (kitten) sesuai literatur ISFM?"
    if st.button("💧 Manajemen Diet Kucing CKD"):
        st.session_state.quick_query = "Jelaskan manajemen diet untuk kucing dengan Chronic Kidney Disease (CKD) berdasarkan jurnal ilmiah."
    if st.button("🍗 Strategi Penurunan Berat Badan"):
        st.session_state.quick_query = "Bagaimana risiko kesehatan akibat obesitas pada kucing dan strategi penurunan berat badan yang aman?"
    if st.button("📉 Lingkungan Rendah Stress (Feline-Friendly)"):
        st.session_state.quick_query = "Jelaskan konsep feline-friendly environment untuk mengurangi stress pada kucing rumah."

    st.markdown('<div class="sidebar-footer">Powered by Google Gemini 2.5 Flash</div>', unsafe_allow_html=True)

st.title("👋 Selamat Datang!")
st.markdown("#### Saya adalah VetaSync Assistant, siap membantu edukasi kesehatan hewan Anda.")

API_KEY = "YOUR_API_KEY_HERE"

@st.cache_resource
def get_client(api_key):
    return genai.Client(api_key=api_key)

client = get_client(API_KEY)

system_instruction = """
Kamu adalah VetaSync Assistant, seorang spesialis edukasi kesehatan hewan (Animal Health Educator) yang memberikan informasi medis dan perawatan hewan yang sangat akurat, ilmiah, dan berbasis bukti (evidence-based medicine).

TARGET PENGGUNA: Pemilik hewan dan Staf Klinik Hewan. Jangan bedakan cara berkomunikasi, berikan standar kualitas informasi tinggi yang sama untuk keduanya.

KOMITMEN ILMIAH:
- Semua saran WAJIB menyertakan referensi jurnal ilmiah atau konsensus organisasi veteriner terpercaya (contoh: JAVMA, WSAVA, AAHA, ISFM, Journal of Feline Medicine and Surgery).
- Gunakan sitasi dalam teks (contoh: "Menurut studi di JSAP (2021)...").

PANDUAN KONTEN:
- Fokus pada: Nutrisi, Protokol Vaksinasi, Perilaku, Penyakit Menular, Kesehatan Gigi, Perawatan Hewan Senior, dan Kesejahteraan (Animal Welfare).
- Gunakan gaya bahasa profesional, hangat, dan simpatik.
- Hindari referensi ke sistem manajemen klinik atau alur kasir/staff yang spesifik. Fokus murni pada EDUKASI HEWAN.
- Selalu gunakan Markdown yang cantik (tabel, list, bold) agar mudah dibaca.

PENANGANAN DARURAT:
- Jika pengguna mendeskripsikan gejala kritis (tidak bisa kencing, kesulitan napas, kejang, pendarahan, trauma), berikan instruksi darurat untuk segera ke klinik dokter hewan tanpa menunda-nunda.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

if "quick_query" in st.session_state:
    user_input = st.session_state.quick_query
    del st.session_state.quick_query
else:
    user_input = st.chat_input("Tanyakan topik kesehatan hewan (contoh: Diet CKD Kucing, Vaksinasi Anjing)...")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            history = []
            for msg in st.session_state.messages[:-1]:
                history.append({
                    "role": "user" if msg["role"] == "user" else "model",
                    "parts": [{"text": msg["content"]}]
                })
            
            chat = client.chats.create(
                model="gemini-2.5-flash",
                config={"system_instruction": system_instruction},
                history=history
            )
            
            response = chat.send_message(user_input)
            
            emergency_keywords = ["darurat", "berhenti napas", "pendarahan", "kejang", "kritis", "kecelakaan", "tidak makan", "tidak bisa kencing"]
            if any(key in user_input.lower() for key in emergency_keywords):
                st.markdown("""<div class="emergency-box">⚠️ PERINGATAN DARURAT ILMIAH: Gejala ini berkorelasi dengan risiko kegagalan organ atau ancaman nyawa. Segera bawa hewan ke klinik dokter hewan terdekat untuk penanganan darurat!</div>""", unsafe_allow_html=True)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
            if "quick_query" not in st.session_state:
                st.rerun()
                
        except Exception as e:
            st.error(f"Gagal memproses informasi edukasi: {e}")