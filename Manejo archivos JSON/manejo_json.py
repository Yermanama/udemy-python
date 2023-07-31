# Leer archivo json
# JSON - Javascript Object Notation

import requests


respuesta = requests.get(
    "http://globalmentoring.com.mx/api/personas.json",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537",
        "Accept": "application/json",
    }
)
json_respuesta = respuesta.json()
print(json_respuesta)

for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]}, {persona["edad"]}')

# Accedemos a las variables independientes

print(f'La llave total cotiene {json_respuesta["total"]}, y la llave de mensaje contiene {json_respuesta["mensaje"]}')