import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

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
# BARRA LATERAL (PERFIL Y ENLACE GENERAL)
# -----------------------------------------------------------------------------
with st.sidebar:
  st.subheader("Aplicaciones de IA.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)
  st.markdown("---")
  url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
  st.write(f"🌐 [Sitio de Prácticas y Enlaces]({url_ia})")

# -----------------------------------------------------------------------------
# CONTENIDO PRINCIPAL: PORTAFOLIO DE APLICACIONES (3 COLUMNAS)
# -----------------------------------------------------------------------------
st.markdown("### 🗂️ APLICACIONES Y PROYECTOS DE INTELIGENCIA ARTIFICIAL")
st.write("Haz clic en cualquier aplicación para abrirla de forma segura en una nueva pestaña:")
st.write("")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🔊 Texto a Voz")
    st.write("Uso de aplicaciones de IA para texto a voz.")
    st.markdown("[🔗 Abrir Texto a Voz](https://imultimod.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🎯 Reconocimiento de Objetos")
    st.write("Detección de objetos en imágenes (YOLOv5).")
    st.markdown("[🔗 Abrir YOLO](https://yolov5cmc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🤖 Entrenando Modelos")
    st.write("Uso de modelos entrenados personalizados.")
    st.markdown("[🔗 Abrir Modelo](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📜 Generador Texto LSTM")
    st.write("Generación de texto con redes neuronales LSTM.")
    st.markdown("[🔗 Abrir Generador LSTM](https://lstmnlpbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📊 Tablero Inteligente")
    st.write("Tablero interactivo e inteligente.")
    st.markdown("[🔗 Abrir Tablero](https://histinfbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)


with col2: 
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🎤 Voz a Texto")
    st.write("Aplicación de conversión de voz a texto.")
    st.markdown("[🔗 Abrir Voz a Texto](https://traductorw.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📈 Análisis de Datos")
    st.write("Análisis de datos utilizando agentes inteligentes.")
    st.markdown("[🔗 Abrir Agente de Datos](https://dataagente.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📼 Transcriptor Audio/Video")
    st.write("Transcripciones automáticas con Whisper.")
    st.markdown("[🔗 Abrir Transcriptor](https://transcript-whisper.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("⚡ Generación Aumentada")
    st.write("Generación aumentada (RAG) para chat con documentos.")
    st.markdown("[🔗 Abrir ChatPDF](https://chatpdfbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📡 RecepMqtt")
    st.write("Recepción de datos y telemetría mediante MQTT.")
    st.markdown("[🔗 Abrir RecepMqtt](https://recepmqttbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)


with col3: 
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("💬 Generación en Contexto")
    st.write("Aplicación que usa RAG a partir de un documento PDF.")
    st.markdown("[🔗 Abrir RAG PDF](https://chatpdf-cc.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("📷 Análisis de Imagen")
    st.write("Capacidad avanzada de análisis visual.")
    st.markdown("[🔗 Abrir Vision GPT-4o](https://vision2-gpt4o.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🕹️ Vision App")
    st.write("Aplicación especializada en visión artificial.")
    st.markdown("[🔗 Abrir Vision App](https://visionappbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🔢 Mnist")
    st.write("Predicción de dígitos escritos a mano.")
    st.markdown("[🔗 Abrir Mnist Pred](https://mnistpredbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🚀 Send Mqtt")
    st.write("Envío de comandos por protocolo MQTT.")
    st.markdown("[🔗 Abrir Send Mqtt](https://sendcmqttbeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.subheader("🎙️ Control Voice")
    st.write("Control de dispositivos mediante comandos de voz.")
    st.markdown("[🔗 Abrir Control Voice](https://ctrlvoicebeatrizmontoya.streamlit.app/)")
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: #ff007f; font-family: "Courier New", Courier, monospace; font-size: 12px;'>
        [:: BEA'S CYBER SPACE • 2000S RETRO VIBES • ALL RIGHTS RESERVED ::]
    </p>
""", unsafe_allow_html=True)
