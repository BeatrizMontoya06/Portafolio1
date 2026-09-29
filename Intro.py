import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA: BEE'S PORTAFOLIO (ESTILO BREAKCORE / WEBCORE 2000s)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="[:: BEE'S BREAKCORE PORTAL 2000s ::]", 
    page_icon="💀", 
    layout="wide"
)

# Estilo visual Breakcore / Webcore / Internet 2000s oscuro, glitch, cyberpunk underground
st.markdown("""
    <style>
    /* Fondo oscuro con textura digital / glitch */
    .stApp {
        background-color: #080808;
        color: #e0e0e0;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Cabecera estilo net-art / breakcore con destellos de color glitch */
    .breakcore-header {
        background: linear-gradient(135deg, #1a0033, #330033, #001a33);
        border: 2px dashed #ff007f;
        padding: 25px;
        text-align: center;
        box-shadow: 0px 0px 15px rgba(255, 0, 127, 0.4);
        position: relative;
    }
    
    h1, h2, h3 {
        color: #00ffff !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 2px 2px #ff007f, -2px -2px #00ff66;
        letter-spacing: 2px;
    }
    
    /* Sidebar al estilo terminal / winamp underground */
    div[data-testid="stSidebar"] {
        background-color: #0d0d0d !important;
        border-right: 2px solid #00ff66;
    }
    
    /* Tarjetas de aplicaciones estilo ventana de Windows 98 / Webcore glitch */
    .breakcore-card {
        background-color: #121212;
        border: 2px solid #ff007f;
        border-radius: 4px;
        padding: 15px;
        margin-bottom: 25px;
        box-shadow: 4px 4px 0px #00ffff;
        transition: transform 0.1s ease;
    }
    
    .breakcore-card:hover {
        border-color: #00ff66;
        box-shadow: 4px 4px 0px #ff007f;
    }
    
    /* Botones y enlaces estilo arcade/terminal */
    .stButton>button {
        background-color: #ff007f !important;
        color: #000000 !important;
        border: 2px solid #00ffff;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
    }
    
    a {
        color: #00ffff !important;
        text-decoration: none;
    }
    a:hover {
        color: #ff007f !important;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ENCABEZADO PRINCIPAL (ESTÉTICA BREAKCORE / WEBCORE)
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="breakcore-header">
        <h1>💀 ~* b33_p0rtf0l10.exe *~ 🎛️</h1>
        <p style="color: #00ff66; font-family: 'Courier New', monospace; font-size: 14px; letter-spacing: 1px;">
            [ SYSTEM ACTIVE // BREAKCORE / WEBCORE 2000S ARCHIVE // INTELLECTUAL ARTIFICIAL ]
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# BARRA LATERAL (ESTILO PERFIL UNDERGROUND / TERMINAL)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.subheader("💾 [ SYSTEM_INFO ]")
    try:
        st.image("OIG5.jpg", width=150)
    except:
        pass
    st.markdown("---")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)
    st.markdown("---")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    st.subheader("⚡ [ QUICK_LINKS ]")
    st.write(f"Páginas y ejercicios prácticos: [ACCESS HERE]({url_ia})")
    st.markdown("📟 *status: online // streaming at 180bpm*")

# Función auxiliar para mostrar la vista previa interactiva (iframe) optimizada para webcore
def render_preview(url):
    components.iframe(f"{url}?embed=true", height=200, scrolling=False)

# -----------------------------------------------------------------------------
# DISTRIBUCIÓN EN 3 COLUMNAS CON EL NUEVO INTRO Y PREVIEWS EN VIVO
# -----------------------------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("📺 00. Intro Portal")
    render_preview("https://introbeatrizmontoya.streamlit.app/")
    st.write("Punto de entrada principal al sistema interactivo.")
    st.markdown("[🔗 Abrir App Completa](https://introbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("🗣️ 01. Voz a Texto")
    render_preview("https://textoavozbeatrizmontoya.streamlit.app/")
    st.write("Convierte la voz en texto de forma rápida y sencilla.")
    st.markdown("[🔗 Abrir App Completa](https://textoavozbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("🌐 02. Traductor")
    render_preview("https://traductorbeatrizmontoya.streamlit.app/")
    st.write("Traductor inteligente para comunicarte sin barreras.")
    st.markdown("[🔗 Abrir App Completa](https://traductorbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("🎧 03. Texto a Audio")
    render_preview("https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/")
    st.write("OCR y conversión de texto a audio multimedia.")
    st.markdown("[🔗 Abrir App Completa](https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("☁️ 04. Nube de Palabras")
    render_preview("https://wordcloudbeatrizmontoya.streamlit.app/")
    st.write("Visualiza la frecuencia de tus términos con nubes de palabras.")
    st.markdown("[🔗 Abrir App Completa](https://wordcloudbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("❤️ 05. Sentimientos")
    render_preview("https://asentimientosbeatrizmontoya.streamlit.app/")
    st.write("Descubre la emoción o polaridad oculta detrás de un texto.")
    st.markdown("[🔗 Abrir App Completa](https://asentimientosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("📝 06. Análisis de Texto")
    render_preview("https://astextobeatrizmontoya.streamlit.app/")
    st.write("Herramienta completa para procesar y analizar textos.")
    st.markdown("[🔗 Abrir App Completa](https://astextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("🔍 07. Detector Objetos")
    render_preview("https://detectordeobjetosbeatrizmontoya.streamlit.app/")
    st.write("Identifica y detecta objetos visuales con inteligencia artificial.")
    st.markdown("[🔗 Abrir App Completa](https://detectordeobjetosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("👋 08. Gestos / Movimiento")
    render_preview("https://tmbeatrizmontoya.streamlit.app/")
    st.write("Detección de gestos y movimientos con Teachable Machine.")
    st.markdown("[🔗 Abrir App Completa](https://tmbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="breakcore-card">', unsafe_allow_html=True)
    st.subheader("🔤 09. Detector de Texto")
    render_preview("https://detectordetextobeatrizmontoya.streamlit.app/")
    st.write("Reconocimiento óptico de caracteres (OCR) integrado.")
    st.markdown("[🔗 Abrir App Completa](https://detectordetextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página estilo breakcore / net-art
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #ff007f; font-family: "Courier New", Courier, monospace; font-size: 13px;'>
        [:: PRODUCED BY BEE • BREAKCORE ARCHIVE 2000s • ALL RIGHTS RESERVED ::]
    </p>
""", unsafe_allow_html=True)
