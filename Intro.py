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

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://imultimod.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://yolov5cmc.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 # NUEVA AÑADIDA EN COL 1
 st.subheader("Generador Texto LSTM")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En este enlace generaremos texto utilizando redes neuronales LSTM.") 
 url_lstm = "https://lstmnlpbeatrizmontoya.streamlit.app/"
 st.write(f"LSTM: [Enlace]({url_lstm})")

 # NUEVA AÑADIDA EN COL 1
 st.subheader("Tablero Inteligente")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En este enlace exploraremos un tablero interactivo e inteligente.") 
 url_tablero = "https://histinfbeatrizmontoya.streamlit.app/"
 st.write(f"Tablero: [Enlace]({url_tablero})")


with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Transcriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 # NUEVA AÑADIDA EN COL 2
 st.subheader("Generación Aumentada (ChatPDF)")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("Aplicación basada en generación aumentada para interactuar con tus documentos.") 
 url_rag = "https://chatpdfbeatrizmontoya.streamlit.app/"
 st.write(f"ChatPDF: [Enlace]({url_rag})")

 # NUEVA AÑADIDA EN COL 2
 st.subheader("RecepMqtt")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("Recepción de datos y señales a través de protocolo MQTT.") 
 url_recepmqtt = "https://recepmqttbeatrizmontoya.streamlit.app/"
 st.write(f"RecepMqtt: [Enlace]({url_recepmqtt})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 # NUEVA AÑADIDA EN COL 3
 st.subheader("Vision App")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("Aplicación especializada en visión artificial.") 
 url_vision = "https://visionappbeatrizmontoya.streamlit.app/"
 st.write(f"Vision App: [Enlace]({url_vision})")

 # NUEVA AÑADIDA EN COL 3
 st.subheader("MNIST (Clasificación de Dígitos)")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("Predicción de dígitos escritos a mano utilizando el dataset MNIST.") 
 url_mnist = "https://mnistpredbeatrizmontoya.streamlit.app/"
 st.write(f"MNIST: [Enlace]({url_mnist})")

 # NUEVAS ADICIONALES EN COL 3 (SendMqtt y Control Voice)
 st.subheader("SendMqtt")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("Envío de comandos y control a través de protocolo MQTT.") 
 url_sendmqtt = "https://sendcmqttbeatrizmontoya.streamlit.app/"
 st.write(f"SendMqtt: [Enlace]({url_sendmqtt})")

 st.subheader("Control Voice")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("Aplicación de control remoto por medio de comandos de voz.") 
 url_ctrlvoice = "https://ctrlvoicebeatrizmontoya.streamlit.app/"
 st.write(f"Control Voice: [Enlace]({url_ctrlvoice})")
