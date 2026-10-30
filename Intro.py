import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Ver Sitio Web]({url_ia})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Conversión de texto a voz")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Uso de aplicaciones de IA para texto a voz.") 
    st.write("Enlace: [Texto a Voz](https://imultimod.streamlit.app/)")

    st.subheader("Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("Detección de objetos en imágenes.") 
    st.write("Enlace: [YOLO v5](https://yolov5cmc.streamlit.app/)")

    st.subheader("Entrenando Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Uso de modelos entrenados personalizados.") 
    st.write("Enlace: [Modelo Entrenado](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("Generador Texto LSTM")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Generación de texto con redes neuronales LSTM.") 
    st.write("Enlace: [Generador LSTM](https://lstmnlpbeatrizmontoya.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("Tablero Inteligente")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("Tablero interactivo e inteligente.") 
    st.write("Enlace: [Tablero Inteligente](https://histinfbeatrizmontoya.streamlit.app/)")


with col2: 
    st.subheader("Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("Aplicación de conversión de voz a texto.") 
    st.write("Enlace: [Voz a Texto](https://traductorw.streamlit.app/)")

    st.subheader("Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("Análisis de datos utilizando agentes inteligentes.") 
    st.write("Enlace: [Agente de Datos](https://dataagente.streamlit.app/)")

    st.subheader("Transcriptor Audio y Video")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("Transcripciones automáticas de audio y video.") 
    st.write("Enlace: [Transcriptor](https://transcript-whisper.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("Generación Aumentada")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("Generación aumentada (RAG) para chat con documentos.") 
    st.write("Enlace: [ChatPDF (Aumentada)](https://chatpdfbeatrizmontoya.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("RecepMqtt")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Recepción de datos y telemetría mediante MQTT.") 
    st.write("Enlace: [RecepMqtt](https://recepmqttbeatrizmontoya.streamlit.app/)")


with col3: 
    st.subheader("Generación en Contexto")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("Aplicación que usa RAG a partir de un documento PDF.") 
    st.write("Enlace: [RAG PDF](https://chatpdf-cc.streamlit.app/)")

    st.subheader("Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Capacidad avanzada de análisis en imágenes.") 
    st.write("Enlace: [Vision GPT-4o](https://vision2-gpt4o.streamlit.app/)")
    
    st.subheader("Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Interacción con el mundo físico y sistemas ciberfísicos.") 
    st.write("Enlace: [Sistema Ciberfísico](https://vision2-gpt4o.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("Vision App")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Aplicación de visión artificial personalizada.") 
    st.write("Enlace: [Vision App](https://visionappbeatrizmontoya.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("Mnist")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Predicción de dígitos escritos a mano (MNIST).") 
    st.write("Enlace: [Mnist Pred](https://mnistpredbeatrizmontoya.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("sendcmqtt")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Envío de comandos por protocolo MQTT.") 
    st.write("Enlace: [Send Mqtt](https://sendcmqttbeatrizmontoya.streamlit.app/)")

    # --- NUEVA AÑADIDA ---
    st.subheader("control voice")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Control de dispositivos mediante comandos de voz.") 
    st.write("Enlace: [Control Voice](https://ctrlvoicebeatrizmontoya.streamlit.app/)")
