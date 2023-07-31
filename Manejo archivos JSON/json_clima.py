import requests

respuesta = requests.get(
    "http://globalmentoring.com.mx/api/clima.json",
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537",
        "Accept": "application/json",
    },
)

json_respuesta = respuesta.json()
print(json_respuesta)

print(f'La descripción del clima es {json_respuesta["clima"][0]["descripcion"]}')
print(f'La temperatura mínima es {json_respuesta["principal"]["temp_min"]}')
print(f'La temperatura máxima es {json_respuesta["principal"]["temp_max"]}')