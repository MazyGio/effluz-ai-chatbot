import os
from openai import OpenAI
from langchain_core.utils.function_calling import convert_to_openai_tool
from effluzchatbot import test_add_expense_tool, test_report_tool
import json
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def parse_function_args(response):
    message = response.choices[0].message
    return json.loads(message.tool_calls[0].function.arguments)

SYSTEM_MESSAGE = """Tu tarea es completar objetivos específicos y crear una
orden de venta. Tienes a tu disposición una variedad de herramientas, cada
una especializada en realizar un tipo de tarea.

Para completar el objetivo:
Pensamiento: Considera el objetivo y determina qué herramienta es la mejor
para completarlo según sus capacidades y el tipo de trabajo.

Usa la herramienta report_tool con una instrucción detallando los resultados
de tu trabajo.

Si encuentras un problema y no puedes completar la tarea:
Usa la herramienta report_tool para comunicar el desafío o la razón del
fallo.

Recibirás feedback basado en los resultados de la ejecución de cada herramienta.
Este feedback es crucial para abordar y resolver cualquier problema por medio
utilizando las herramientas disponibles de manera estratégica.
"""
user_message = "Gasté $4.75 hoy en un café, por favor registra este gasto. La tasa de impuestos es del 7%."

client = OpenAI(api_key=OPENAI_API_KEY)
model_name = "gpt-4o-mini"

messages = [
    {"role": "system", "content": SYSTEM_MESSAGE},
    {"role": "user", "content": user_message}
]

del test_add_expense_tool["function"]["parameters"]["required"]

response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    tools=[test_add_expense_tool, test_report_tool],
)

print(parse_function_args(response))