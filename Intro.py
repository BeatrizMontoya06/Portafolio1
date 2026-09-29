import streamlit as st
from PIL import Image

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA: BEE'S PORTAFOLIO (ESTILO BLOG 2000s LLENO DE VIDA)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="🐝 Bee's Portafolio 2000s 🌸", 
    page_icon="🐝", 
    layout="wide"
)

# Estilo visual retro de los 2000s: colores alegres, bordes punteados, tipografía de blog de MySpace/MetroFlog
st.markdown("""
    <style>
    /* Fondo con tono cálido tipo blog clásico */
    .stApp {
        background-color: #fff9e6;
        color: #333333;
        font-family: 'Comic Sans MS', 'Verdana', sans-serif;
    }
    
    /* Cabecera estilo cartel de blog de los 2000s */
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
    
    /* Barra lateral decorada como panel de perfil de usuario antiguo */
    div[data-testid="stSidebar"] {
        background-color: #ffebf0 !important;
        border-right: 3px dotted #ff66b2;
    }
    
    /* Tarjetas de aplicaciones estilo post de blog */
    .blog-card {
        background-color: #ffffff;
        border: 2px solid #ff66b2;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 3px 3px 0px #ffcc00;
    }
    
    /* Botones y enlaces divertidos */
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
            ¡Bienvenidos a mi rincón web! Explora mis proyectos de Inteligencia Artificial cargados de energía y color. ✨
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------------------------------------------------------
# BARRA LATERAL (ESTILO PERFIL DE BLOG 2000s)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.subheader("🌸 Sobre Mí & IA")
    st.image("OIG5.jpg", width=150) # Imagen decorativa de perfil en la sidebar
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

# -----------------------------------------------------------------------------
# DISTRIBUCIÓN EN 3 COLUMNAS (ESTILO POSTS DE BLOG)
# -----------------------------------------------------------------------------
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🎙️ Texto a Voz")
    try:
        st.image(Image.open('txt_to_audio2.png'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("¡Escucha cómo el texto cobra vida con esta aplicación!")
    st.markdown("[🔗 Enlace a Texto a Voz](https://imultimod.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("👁️ Reconocimiento de Objetos")
    try:
        st.image(Image.open('txt_to_audio.png'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Descubre cómo detectamos objetos en tiempo real con YOLO.")
    st.markdown("[🔗 Enlace a YOLO](https://yolov5cmc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🤖 Entrenando Modelos")
    try:
        st.image(Image.open('OIG5.jpg'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Mira cómo puedes integrar y usar tu propio modelo entrenado.")
    st.markdown("[🔗 Enlace al Modelo](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🗣️ Voz a Texto")
    try:
        st.image(Image.open('OIG8.jpg'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Convierte tus palabras habladas en texto escrito al instante.")
    st.markdown("[🔗 Enlace a Voz a Texto](https://traductorw.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("📊 Análisis de Datos")
    try:
        st.image(Image.open('data_analisis.png'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Analiza datos complejos de forma inteligente usando agentes.")
    st.markdown("[🔗 Enlace a Datos](https://dataagente.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("📼 Transcriptor Audio/Video")
    try:
        st.image(Image.open('OIG3.jpg'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Realiza transcripciones automáticas de tus archivos multimedia.")
    st.markdown("[🔗 Enlace a Transcriptor](https://transcript-whisper.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("📚 Generación en Contexto")
    try:
        st.image(Image.open('Chat_pdf.png'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Chatea directamente con tus documentos PDF usando RAG.")
    st.markdown("[🔗 Enlace a RAG (PDF)](https://chatpdf-cc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("🖼️ Análisis de Imagen")
    try:
        st.image(Image.open('OIG4.jpg'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Explora la capacidad de comprensión visual avanzada.")
    st.markdown("[🔗 Enlace a Vision](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blog-card">', unsafe_allow_html=True)
    st.subheader("⚡ Sistema Ciberfísico")
    try:
        st.image(Image.open('OIG6.jpg'), width=180)
    except:
        st.write("[Imagen no encontrada]")
    st.write("Experimenta la interacción directa con el mundo físico.")
    st.markdown("[🔗 Enlace a Ciberfísico](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página estilo blog retro
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #ff0066; font-weight: bold;'>
        🌸 Hecho con mucho ❤️ en Bee's Portafolio • 2000s Retro Vibes 🐝
    </p>
""", unsafe_allow_html=True)
