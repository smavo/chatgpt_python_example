import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

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
    ingreso_usuario= input('\nTu:')
    if ingreso_usuario.lower() == 'salir':
        break
    
    promtp = f"El usuario pregunta: {ingreso_usuario}\nChatGpt Responde:"
    respuesta_gpt= preguntar_chat_gpt(promtp)
    print(f"Chatbot: {respuesta_gpt}")

