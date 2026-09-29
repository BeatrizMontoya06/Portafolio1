import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA: BEE'S PORTAFOLIO (ESTILO BLOG 2000s LLENO DE VIDA)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="🐝 Bee's Portafolio 2000s 🌸", 
    page_icon="🐝", 
    layout="wide"
)

# Estilo visual retro de los 2000s: colores alegres, bordes punteados, tipografía de blog
st.markdown("""
    <style>
    .stApp {
        background-color: #fff9e6;
        color: #333333;
        font-family: 'Comic Sans MS', 'Verdana', sans-serif;
    }
    
    .blog-header {
        background: linear-gradient(90deg, #ff99cc, #ffff99, #99ccff);
        border: 3px dashed #ff3399;
        padding: 20px;
        text-align: center;
        border-radius: 15px;
        box-shadow: 4px 4px 0px #ff3399;
    }
    
    h1, h2, h3 {
        color: #ff0066 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    div[data-testid="stSidebar"] {
        background-color: #ffebf0 !important;
        border-right: 3px dotted #ff66b2;
    }
    
    .blog-card {
        background-color: #ffffff;
        border: 2px solid #ff66b2;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 25px;
        box-shadow: 3px 3px 0px #ffcc00;
    }
    
    .stButton>button {
        background-color: #ff3399 !important;
        color: white !important;
        border: 2px dashed #ffff00;
        border-radius: 20px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ENCABEZADO PRINCIPAL (BEE'S PORTAFOLIO)
# -----------------------------------------------------------------------------
st.markdown("""
    <div class="blog-header">
        <h1>🐝 ~* Bee's Portafolio de IA *~ 🌸</h1>
        <p style="color: #660033; font-weight: bold; font-size: 16px;">
            ¡Bienvenidos a mi rincón web! Explora las vistas previas en vivo de mis proyectos de Inteligencia Artificial. ✨
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# BARRA LATERAL (ESTILO PERFIL DE BLOG 2000s)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.subheader("🌸 Sobre Mí & IA")
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
    st.subheader("🔗 Enlaces Favoritos")
    st.write(f"Páginas y ejercicios prácticos: [¡Visítalo aquí!]({url_ia})")
    st.markdown("✨ *¡Deja tu huella en el guestbook!* ✨")

# Función auxiliar para mostrar la vista previa interactiva (iframe) de manera limpia
def render_preview(url):
    components.iframe(f"{url}?embed=true", height=200, scrolling=False)

# -----------------------------------------------------------------------------
# DISTRIBUCIÓN EN 3 COLUMNAS CON PREVIEWS EN VIVO
# -----------------------------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🗣️ Voz a Texto")
    render_preview("https://textoavozbeatrizmontoya.streamlit.app/")
    st.write("Convierte la voz en texto de forma rápida y sencilla.")
    st.markdown("[🔗 Abrir App Completa](https://textoavozbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🌐 Traductor")
    render_preview("https://traductorbeatrizmontoya.streamlit.app/")
    st.write("Traductor inteligente para comunicarte sin barreras.")
    st.markdown("[🔗 Abrir App Completa](https://traductorbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🎧 Texto a Audio")
    render_preview("https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/")
    st.write("OCR y conversión de texto a audio multimedia.")
    st.markdown("[🔗 Abrir App Completa](https://ocr-audio-fkottyqbdcwtbbvr2sykwb.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("☁️ Nube de Palabras")
    render_preview("https://wordcloudbeatrizmontoya.streamlit.app/")
    st.write("Visualiza la frecuencia de tus términos con nubes de palabras.")
    st.markdown("[🔗 Abrir App Completa](https://wordcloudbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("❤️ Análisis de Sentimientos")
    render_preview("https://asentimientosbeatrizmontoya.streamlit.app/")
    st.write("Descubre la emoción o polaridad oculta detrás de un texto.")
    st.markdown("[🔗 Abrir App Completa](https://asentimientosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("📝 Análisis de Texto")
    render_preview("https://astextobeatrizmontoya.streamlit.app/")
    st.write("Herramienta completa para procesar y analizar textos.")
    st.markdown("[🔗 Abrir App Completa](https://astextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🔍 Detector de Objetos")
    render_preview("https://detectordeobjetosbeatrizmontoya.streamlit.app/")
    st.write("Identifica y detecta objetos visuales con inteligencia artificial.")
    st.markdown("[🔗 Abrir App Completa](https://detectordeobjetosbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("👋 Gesto / Movimiento")
    render_preview("https://tmbeatrizmontoya.streamlit.app/")
    st.write("Detección de gestos y movimientos con Teachable Machine.")
    st.markdown("[🔗 Abrir App Completa](https://tmbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🔤 Detector de Texto")
    render_preview("https://detectordetextobeatrizmontoya.streamlit.app/")
    st.write("Reconocimiento óptico de caracteres (OCR) integrado.")
    st.markdown("[🔗 Abrir App Completa](https://detectordetextobeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página estilo blog retro
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #ff0066; font-weight: bold;'>
        🌸 Hecho con mucho ❤️ en Bee's Portafolio • 2000s Retro Vibes 🐝
    </p>
""", unsafe_allow_html=True)
