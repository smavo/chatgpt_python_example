import openai
import os
import spacy
import numpy as np
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []
modelo_spacy = spacy.load('es_core_news_md')
palabras_prohibidas = ['madrid', 'Palabra2']


def simulitud_coseno(vector1, vector2):
    superposicion = np.doc(vector1, vector2)
    magnitud1 = np.linalg.norm(vector1)
    magnitud2 = np.linalg.norm(vector2)
    sim_cos = superposicion / (magnitud1 * magnitud2)
    return sim_cos


def es_relevante(respuesta, entrada, umbral=0.5):
    entrada_vectorizada = modelo_spacy(entrada).vector
    respuesta_vectorizada = modelo_spacy(respuesta).vector
    similitud = simulitud_coseno(entrada_vectorizada, respuesta_vectorizada)
    return similitud >= umbral

def fitlrar_lista_negra(texto, lista_negra):
    token = modelo_spacy(texto)
    resultado = []

    for t in token:
        if t.text.lower() not in lista_negra:
            resultado.append(t.text)
        else:
            resultado.append("[XXXXX]")
    return " ".join(resultado)


def preguntar_chat_gpt(pregunta, modelo='text-davinci-002'):
    response = openai.Completion.create(
        engine=modelo,
        prompt=pregunta,
        max_tokens=150,
        temperature=1.5
    )
    respuesta_sin_controlar = response.choices[0].text.strip()
    respuesta_controlada = fitlrar_lista_negra(respuesta_sin_controlar, palabras_prohibidas)
    return respuesta_controlada


print("Bienvenido a nuestro chatbot Basico. Escribe 'salir' cuando quieras terminar")

while True:
    conversacion_historica = ""
    ingreso_usuario = input('\nTu:')
    if ingreso_usuario.lower() == 'salir':
        break

    for question, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {question}\n"
        conversacion_historica += f"Chat GTP responde: {respuesta}\n"

    promtp = f"El usuario pregunta: {ingreso_usuario}\n"
    conversacion_historica += promtp
    respuesta_gpt = preguntar_chat_gpt(conversacion_historica)

    relevante = es_relevante(respuesta_gpt, ingreso_usuario)

    if relevante:
        print(f"{respuesta_gpt}")
        preguntas_anteriores.append(ingreso_usuario)
        respuestas_anteriores.append(respuesta_gpt)
    else:
        print("La respuesta no es revelante")
