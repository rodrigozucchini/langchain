from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.7
)

chat_prompt = ChatPromptTemplate.from_messages({
    ("system", "Eres un traductor del español al ingles muy preciso."),
    ("human", "{texto}")
})

mensajes = chat_prompt.invoke({"texto": "Hola mundo, ¿Como estas?"})

respuesta = llm.invoke(mensajes)

print("Respuesta del modelo:", respuesta.content)