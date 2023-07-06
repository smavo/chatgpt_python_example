import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

def crear_contenido1(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Por favor escribe un articulo corto sobre el tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.trip()

tema = input("Elije un tema para tu articulo: ")
tokens = int(input("Cuantos tokens maximos tendra un articulo: "))
temperatura = int(input("Del 1 al 10, que tan creativo quieres que sea tu articulo: ")) / 10
articulo_creado = crear_contenido1(tema, tokens, temperatura)

print(articulo_creado)


def resumir_texto(texto, tokens, temperatura,  modelo="text-davinci-002"):
    prompt=f"Por favor resumen el siguiente texto: {texto}\n\n"
    respuesta= openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()


original = input("Pega aqui el articulo que quieres resumir sin saltos de linea: ")
tokenss = int(input("Cuantos tokens maximos tendra un resumen: "))
temperaturas = int(input("Del 1 al 10, que tan creativo quieres que sea tu Resumen: ")) / 10
resumen = resumir_texto(original, tokenss, temperaturas)

print(resumen)

