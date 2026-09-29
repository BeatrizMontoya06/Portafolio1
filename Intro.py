import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA: BEE'S PORTAFOLIO (ESTILO MYSPACE / BLOG 2000s COLORIDO)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="~* Bee's Portafolio *~", 
    page_icon="⭐", 
    layout="wide"
)

# Estilo visual MySpace / Blog de los 2000s: colores brillantes, degradados, fuentes retro, bordes punteados
st.markdown("""
    <style>
    /* Fondo con degradado colorido estilo MySpace antiguo */
    .stApp {
        background: linear-gradient(135deg, #ffc0cb, #e6e6fa, #afeeee);
        color: #333333;
        font-family: 'Comic Sans MS', 'Verdana', sans-serif;
    }
    
    /* Encabezado estilo banner de MySpace / Blog */
    .myspace-header {
        background: linear-gradient(90deg, #ff1493, #ff69b4, #8a2be2, #00ffff);
        border: 4px solid #ffffff;
        padding: 30px;
        text-align: center;
        border-radius: 12px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    h1 {
        color: #ffffff !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-shadow: 3px 3px #ff007f, -2px -2px #0000ff;
        font-size: 42px;
        letter-spacing: 2px;
    }
    
    h2, h3 {
        color: #ff1493 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    /* Barra lateral estilo perfil clásico de MySpace */
    div[data-testid="stSidebar"] {
        background-color: #fff0f5 !important;
        border-right: 4px dotted #ff69b4;
    }
    
    /* Tarjetas de aplicaciones estilo posts de blog */
    .myspace-card {
        background-color: #ffffff;
        border: 3px dashed #ff1493;
        border-radius: 15px;
        padding: 18px;
        margin-bottom: 25px;
        box-shadow: 5px 5px 0px #8a2be2;
    }
    
    .myspace-card:hover {
        border-color: #00ffff;
        box-shadow: 5px 5px 0px #ff1493;
    }
    
    /* Enlaces y botones coloridos */
    .stButton>button {
        background-color: #ff1493 !important;
        color: #ffffff !important;
        border: 2px solid #ffff00;
        border-radius: 15px;
        font-weight: bold;
    }
    
    a {
        color: #ff1493 !important;
        font-weight: bold;
        text-decoration: none;
    }
    a:hover {
        color: #8a2be2 !important;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ENCABEZADO PRINCIPAL (BEE'S PORTAFOLIO)
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="myspace-header">
        <h1>~* Bee's Portafolio *~</h1>
        <p style="color: #ffffff; font-family: 'Comic Sans MS', sans-serif; font-size: 18px; font-weight: bold; text-shadow: 1px 1px #000000;">
            ✨ Mis aplicaciones y proyectos de Inteligencia Artificial ✨
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# BARRA LATERAL (ESTILO PERFIL DE USUARIO 2000s)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.subheader("⭐ Perfil")
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
    st.subheader("🔗 Enlaces Útiles")
    st.write(f"Páginas y ejercicios prácticos: [Visitar enlace]({url_ia})")
    st.markdown("💖 *¡Gracias por visitar mi espacio!* 💖")

# Función auxiliar para mostrar la vista previa interactiva (iframe)
def render_preview(url):
    components.iframe(f"{url}?embed=true", height=200, scrolling=False)

# -----------------------------------------------------------------------------
# DISTRIBUCIÓN EN 3 COLUMNAS CON LOS 10 ENLACES Y PREVIEWS EN VIVO
# -----------------------------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("🚀 Intro Portal")
    render_preview("https://introbeatrizmontoya.streamlit.app/")
    st.write("Punto de entrada principal al sistema interactivo.")
    st.markdown("[🔗 Abrir App Completa](https://introbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("🗣️️ Voz a Texto")
    render_preview("https://textoavozbeatrizmontoya.streamlit.app/")
    st.write("Convierte la voz en texto de forma rápida y sencilla.")
    st.markdown("[🔗 Abrir App Completa](https://textoavozbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("🌐 Traductor")
    render_preview("https://traductorbeatrizmontoya.streamlit.app/")
    st.write("Traductor inteligente para comunicarte sin barreras.")
    st.markdown("[🔗 Abrir App Completa](https://traductorbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("🎧 Texto a Audio")
    render_preview("https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/")
    st.write("OCR y conversión de texto a audio multimedia.")
    st.markdown("[🔗 Abrir App Completa](https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("☁️ Nube de Palabras")
    render_preview("https://wordcloudbeatrizmontoya.streamlit.app/")
    st.write("Visualiza la frecuencia de tus términos con nubes de palabras.")
    st.markdown("[🔗 Abrir App Completa](https://wordcloudbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("❤️ Análisis de Sentimientos")
    render_preview("https://asentimientosbeatrizmontoya.streamlit.app/")
    st.write("Descubre la emoción o polaridad oculta detrás de un texto.")
    st.markdown("[🔗 Abrir App Completa](https://asentimientosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("📝 Análisis de Texto")
    render_preview("https://astextobeatrizmontoya.streamlit.app/")
    st.write("Herramienta completa para procesar y analizar textos.")
    st.markdown("[🔗 Abrir App Completa](https://astextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("🔍 Detector de Objetos")
    render_preview("https://detectordeobjetosbeatrizmontoya.streamlit.app/")
    st.write("Identifica y detecta objetos visuales con inteligencia artificial.")
    st.markdown("[🔗 Abrir App Completa](https://detectordeobjetosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("👋 Gesto / Movimiento")
    render_preview("https://tmbeatrizmontoya.streamlit.app/")
    st.write("Detección de gestos y movimientos con Teachable Machine.")
    st.markdown("[🔗 Abrir App Completa](https://tmbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="myspace-card">', unsafe_allow_html=True)
    st.subheader("🔤 Detector de Texto")
    render_preview("https://detectordetextobeatrizmontoya.streamlit.app/")
    st.write("Reconocimiento óptico de caracteres (OCR) integrado.")
    st.markdown("[🔗 Abrir App Completa](https://detectordetextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página estilo blog colorido 2000s
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #ff1493; font-family: "Comic Sans MS", cursive, sans-serif; font-size: 14px; font-weight: bold;'>
        ✨ Bee's Portafolio • Creado con Streamlit & Vibes de los 2000s ✨
    </p>
""", unsafe_allow_html=True)
