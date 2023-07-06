import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# modelos = openai.Model.list()
# print(modelos)

modelo = 'text-davinci-002'
pregunta = 'Elige un nombre para un gato macho'

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=pregunta,
    n=3,
    temperature=1,
    max_tokens=100
)

# texto_generado = respuesta.choice[0].text.strip()
# print(texto_generado)

for idx, opcion in enumerate(respuesta.choices):
    texto_generado = opcion.text.strip()
    print(f"Respuesta {idx + 1}: {texto_generado}\n")
