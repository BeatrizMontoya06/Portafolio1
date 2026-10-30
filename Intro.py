import streamlit as st
from PIL import Image

# Configuración con estética Y2K / 2000s Cyber-Retro
st.set_page_config(
    page_title="~*~ B.E.E. // Cyber-Portfolio 2000 ~*~",
    page_icon="💿",
    layout="wide"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #000066;
        background-image: linear-gradient(0deg, #000066 0%, #660066 100%);
        color: #00FFCC;
        font-family: "Courier New", Courier, monospace;
    }
    .y2k-header {
        border: 4px ridge #FF00FF;
        background-color: #000000;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 0px 20px #00FFFF;
        margin-bottom: 25px;
    }
    .y2k-card {
        border: 2px dashed #00FFFF;
        background-color: #1a0033;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0px 0px 10px #FF00FF;
    }
    .y2k-title {
        color: #FFFF00;
        text-shadow: 2px 2px #FF00FF;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera Cyber-Retro 2000s
st.markdown("""
    <div class="y2k-header">
        <h1 class="y2k-title">~*~ 💿 B.E.E. // CYBER-PORTFOLIO 2000 💿 ~*~</h1>
        <p style="color: #FF99FF; font-weight: bold;">[!] Sistema Operativo IA v1.0 // Conectado a la Autopista de la Información [!]</p>
        <marquee behavior="scroll" direction="left" scrollamount="6" style="color: #00FFFF; font-weight: bold; background: #000; padding: 5px;">
            *** BIENVENIDOS A MI PORTAFOLIO DE INTELIGENCIA ARTIFICIAL // MÚSICA, CIBERESPACIO Y SISTEMAS CIBERFÍSICOS ***
        </marquee>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
  st.markdown("### 💾 **Sys.Profile**")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)
  st.markdown("---")
  st.markdown("🌐 **Estado:** `ONLINE`")
  st.markdown("💿 **Skin:** `Y2K Cyber-Glitch`")

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("🌐 Enlaces y Prácticas del Sistema")
st.write(f"Enlace para páginas y ejercicios: [Acceso Principal]({url_ia})")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🔊 Texto a Voz")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://imultimod.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("👁️ Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yolov5cmc.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🤖 Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("📜 Generador Texto LSTM")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace usaremos el generador de texto LSTM.") 
 url = "https://lstmnlpbeatrizmontoya.streamlit.app/"
 st.write(f"LSTM: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("📊 Tablero Inteligente")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos el tablero inteligente.") 
 url = "https://histinfbeatrizmontoya.streamlit.app/"
 st.write(f"Tablero: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)


with col2: 
 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🎤 Voz a Texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("📈 Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("📼 Transcriptor Audio/Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("⚡ Generación Aumentada")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa generación aumentada.") 
 url = "https://chatpdfbeatrizmontoya.streamlit.app/"
 st.write(f"Generacion Aumentada: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("📡 RecepMqtt")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la recepción MQTT.") 
 url = "https://recepmqttbeatrizmontoya.streamlit.app/"
 st.write(f"RecepMqtt: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)


with col3: 
 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("💬 Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("📷 Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)
 
 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🕹️ Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("👾 Vision app")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la aplicación de visión.") 
 url = "https://visionappbeatrizmontoya.streamlit.app/"
 st.write(f"Vision app: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🔢 Mnist")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la aplicación MNIST.") 
 url = "https://mnistpredbeatrizmontoya.streamlit.app/"
 st.write(f"Mnist: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🚀 sendcmqtt")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos el envío MQTT.") 
 url = "https://sendcmqttbeatrizmontoya.streamlit.app/"
 st.write(f"sendcmqtt: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)

 st.markdown('<div class="y2k-card">', unsafe_allow_html=True)
 st.subheader("🎙️ Control Voice")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos el control por voz.") 
 url = "https://ctrlvoicebeatrizmontoya.streamlit.app/"
 st.write(f"control voice: [Enlace]({url})")
 st.markdown('</div>', unsafe_allow_html=True)
