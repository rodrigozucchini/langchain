from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

plantilla_sistema = SystemMessagePromptTemplate.from_template("" \
    "Eres un {rol} especializado en {especialidad}. Responde demanera {tono}"                                 
)

plantilla_humano = HumanMessagePromptTemplate.from_template("" \
    "Mi pregunta sobre {tema} es: {pregunta}"                                 
)

chat_prompt = ChatPromptTemplate ([
    plantilla_sistema,
    plantilla_humano
])

mensajes = chat_prompt.format_messages(
    rol = "nutricionista",
    especialidad = "dietas veganas",
    tono = "professional acesible",
    tema="proteinas vegetales",
    pregunta = "¿Cuáles soon las mejores fuentes de proteína vegana para un atleta profesional?"
)

for m in mensajes:
    print(m.content)