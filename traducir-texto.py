import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def traducir_texto(texto, idioma):
    prompt = f"Traduce el texto '{texto}' al {idioma}."
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        n=1,
        max_tokens=1000,
        temperature=0.5
    )

    return response.choices[0].text.strip()


mi_texto = input("Ingresa un texto: ")
mi_idioma = input("A que idioma lo quieres traducir: ")
traduccion = traducir_texto(mi_texto, mi_idioma)
print(traduccion)
