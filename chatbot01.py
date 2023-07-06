import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

preguntas_anteriores = []
respuestas_anteriores = []

def preguntar_chat_gpt(pregunta, modelo='text-davinci-002'):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt = pregunta,
        max_tokens=150,
        temperature=1.5
    )
    return respuesta.choices[0].text.strip()

print("Bienvenido a nuestro chatbot Basico. Escribe 'salir' cuando quieras terminar")

while True:
    conversacion_historica=""
    ingreso_usuario= input('\nTu:')
    if ingreso_usuario.lower() == 'salir':
        break

    for question, respuesta in zip(preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {question}\n"
        conversacion_historica += f"Chat GTP responde: {respuesta}\n"
    
    promtp = f"El usuario pregunta: {ingreso_usuario}\n"
    conversacion_historica += promtp

    respuesta_gpt= preguntar_chat_gpt(conversacion_historica)
    print(f"{respuesta_gpt}")

    preguntas_anteriores.append(ingreso_usuario)
    respuestas_anteriores.append(respuesta_gpt)



