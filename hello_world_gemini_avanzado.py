from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

chat = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.7
)

plantilla = PromptTemplate(
    input_variables=["nombre"],
    template="Saluda al usuario con su nombre.\nNombre del usuario: {nombre}\nAsistente:"
)

chain = plantilla | chat

resultado = chain.invoke({"nombre": "Rodrigo"})

print(resultado.content)