import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA (ESTILO CYBER SPACE / BEATRIZ'S HIVE - 2000s)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Bea's Cyber Space 🐝", 
    page_icon="⭐", 
    layout="wide"
)

# Estilo visual oscuro con patrón de puntos digital y acentos neón Y2K
st.markdown("""
    <style>
    /* Fondo oscuro con patrón de puntos digital */
    .stApp {
        background-color: #0b0714;
        background-image: radial-gradient(#251a3a 1px, transparent 1px);
        background-size: 20px 20px;
        color: #d1c4e9;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Barra superior de marquesina en color amarillo brillante */
    .top-marquee {
        background-color: #ffcc00;
        color: #1a0826;
        padding: 8px 15px;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        border: 2px dashed #ff007f;
        border-radius: 4px;
        margin-bottom: 20px;
        box-shadow: 0px 0px 10px rgba(255, 204, 0, 0.4);
    }
    
    /* Título principal brillante tipo web retro */
    .main-title {
        text-align: center;
        color: #ffaa00 !important;
        font-family: 'Courier New', Courier, monospace;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 2px 2px #ff007f, 0px 0px 10px rgba(255, 170, 0, 0.6);
        margin-bottom: 25px;
    }
    
    /* Estilo de los encabezados */
    h2, h3 {
        color: #ffaa00 !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 1px 1px #ff007f;
    }
    
    /* Barra lateral estilo Y2K Cyber Space */
    div[data-testid="stSidebar"] {
        background-color: #100a1d !important;
        border-right: 2px solid #ff007f;
    }
    
    /* Tarjetas de aplicaciones estilo ventana de blog retro */
    .cyber-card {
        background-color: #140d24;
        border: 2px solid #ff007f;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 25px;
        box-shadow: 4px 4px 0px #7b1fa2;
        transition: 0.2s ease;
    }
    
    .cyber-card:hover {
        border-color: #ffcc00;
        box-shadow: 4px 4px 0px #ff007f;
    }
    
    /* Enlaces y botones estilizados */
    a {
        color: #00e5ff !important;
        text-decoration: none;
        font-weight: bold;
    }
    a:hover {
        color: #ff007f !important;
        text-decoration: underline;
    }
    
    .stButton>button {
        background-color: #ff007f !important;
        color: #ffffff !important;
        border: 2px solid #ffcc00;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# BARRA SUPERIOR AMARILLA
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="top-marquee">
        🐝 Bienvenid@ a Bea's Hive ✦ Diseño Interactivo ✦ Experiencias Inmersivas ✦ Arte, Narrativa & Tecnología ✦ ¡Explora mis proyectos! 🚀
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TÍTULO PRINCIPAL
# -----------------------------------------------------------------------------
st.markdown("<div class='main-title'>✨ * Welcome to Bea's Blog * ✨</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# BARRA LATERAL (LIMPIA, SIN LA SECCIÓN DE PERFIL ANTERIOR)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("<p style='color: #ff007f; font-weight: bold; border-bottom: 2px solid #ff007f; padding-bottom: 5px;'>🎵 Background Music</p>", unsafe_allow_html=True)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.markdown("<p style='font-size: 11px; color: #a1887f;'>Sonando desde los archivos locales.</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.subheader("🔗 Enlaces Clave")
    st.write(f"Páginas y ejercicios: [Acceder]({url_ia})")

# Función auxiliar para incrustar las vistas previas de las apps
def render_preview(url):
    components.iframe(f"{url}?embed=true", height=200, scrolling=False)

# -----------------------------------------------------------------------------
# CONTENIDO PRINCIPAL: PORTAFOLIO DE APLICACIONES (3 COLUMNAS)
# -----------------------------------------------------------------------------
st.markdown("### 🗂️ APLICACIONES Y PROYECTOS DE INTELIGENCIA ARTIFICIAL")
st.write("Explora las vistas previas interactivas de cada herramienta desarrollada en el sistema:")
st.write("")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🚀 00. Intro Portal")
    render_preview("https://introbeatrizmontoya.streamlit.app/")
    st.write("Punto de entrada principal al sistema.")
    st.markdown("[🔗 Abrir App Completa](https://introbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🗣️ 01. Voz a Texto")
    render_preview("https://textoavozbeatrizmontoya.streamlit.app/")
    st.write("Convierte la voz en texto de forma rápida.")
    st.markdown("[🔗 Abrir App Completa](https://textoavozbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🌐 02. Traductor")
    render_preview("https://traductorbeatrizmontoya.streamlit.app/")
    st.write("Traductor inteligente sin barreras.")
    st.markdown("[🔗 Abrir App Completa](https://traductorbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🎧 03. Texto a Audio")
    render_preview("https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/")
    st.write("OCR y conversión multimedia.")
    st.markdown("[🔗 Abrir App Completa](https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("☁️ 04. Nube de Palabras")
    render_preview("https://wordcloudbeatrizmontoya.streamlit.app/")
    st.write("Visualiza frecuencias de términos.")
    st.markdown("[🔗 Abrir App Completa](https://wordcloudbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("❤️ 05. Sentimientos")
    render_preview("https://asentimientosbeatrizmontoya.streamlit.app/")
    st.write("Descubre la polaridad en textos.")
    st.markdown("[🔗 Abrir App Completa](https://asentimientosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📝 06. Análisis de Texto")
    render_preview("https://astextobeatrizmontoya.streamlit.app/")
    st.write("Procesa y analiza contenidos escritos.")
    st.markdown("[🔗 Abrir App Completa](https://astextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🔍 07. Detector Objetos")
    render_preview("https://detectordeobjetosbeatrizmontoya.streamlit.app/")
    st.write("Identifica elementos visuales con IA.")
    st.markdown("[🔗 Abrir App Completa](https://detectordeobjetosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("👋 08. Gestos / Movimiento")
    render_preview("https://tmbeatrizmontoya.streamlit.app/")
    st.write("Detección mediante modelos entrenados.")
    st.markdown("[🔗 Abrir App Completa](https://tmbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🔤 09. Detector de Texto")
    render_preview("https://detectordetextobeatrizmontoya.streamlit.app/")
    st.write("Reconocimiento óptico (OCR).")
    st.markdown("[🔗 Abrir App Completa](https://detectordetextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #ff007f; font-family: "Courier New", Courier, monospace; font-size: 12px;'>
        [:: BEA'S CYBER SPACE • 2000S RETRO VIBES • ALL RIGHTS RESERVED ::]
    </p>
""", unsafe_allow_html=True)
