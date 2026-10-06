from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Eses un asistentes que mantiene el contexto de la conversacion"), 
    MessagesPlaceholder(variable_name="historial"),
    ("human", "{pregunta_actual}")
])

historial_conversaciones = [
  HumanMessage(content="USUARIO: ¿Cuál es la capital de Francia?"),
  AIMessage(content="AI: La capital de Francia es Paris"),   
  HumanMessage(content="USUARIO: ¿Y cuantos habitantes tiene?"),
  AIMessage(content="AI: Paris tiene aproximadamente 2.2 millones de habitantes"),
]

mensajes = chat_prompt.format_messages(
    historial= historial_conversaciones,
    pregunta_actual = "¿Puedes decirme algo interesante de su arquitectura?"
)

for m in messages:
    print(m.content)