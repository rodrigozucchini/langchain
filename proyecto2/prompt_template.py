from langchain_core.prompts import PromptTemplate

template = "Eres un experto en marketing. Sugiere un slogan creativo para un producto de {producto}"

prompt = PromptTemplate(
    template = template,
    input_variables = ["producto"]
)

prompt_lleno = prompt.format(producto="café organico")
print(prompt_lleno)