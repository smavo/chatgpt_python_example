import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# modelos = openai.Model.list()
# print(modelos)

modelo = 'text-davinci-002'
pregunta = 'Puedes crear un poema de 15 palabras sobre el amor'

respuesta = openai.Completion.create(
    engine=modelo,
    prompt=pregunta,
    n=1,
    temperature=0.1
)

texto_generado = respuesta.choice[0].text.strip()

print(texto_generado)
