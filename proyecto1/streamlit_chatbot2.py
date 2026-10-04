import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate

# Configuración inicial
st.set_page_config(page_title="Chatbot Básico", page_icon="🤖")
st.title("🤖 Chatbot Básico con LangChain")
st.markdown("Este es un *chatbot de ejemplo* construido con LangChain + Streamlit. ¡Escribe tu mensaje abajo para comenzar!")

temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
model_name = st.selectbox("Modelo", ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.6-flash"])
chat_model = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)

# Inicializar el historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = [] 

# Mostrar mensajes previos en la interfaz
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        #No muestorm ensaje por pantalla del sistema
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)

# Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

if pregunta:
    # Mostrar inmediatamente el mensaje del usuario por pantalla
    with st.chat_message("user"):
        st.markdown(pregunta)

    # Almacenamos el mensaje en la memoria de streamlit
    st.session_state.mensajes.append(HumanMessage(content=pregunta))

# Respuesta Modelo
    respuesta = chat_model.invoke(st.session_state.mensajes)

    #Mostrar respuesta en la interfaz
    with st.chat_message("assistant"):
        st.markdown(respuesta.content)

    st.session_state.mensajes.append(respuesta)