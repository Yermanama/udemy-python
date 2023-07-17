# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

palabras_lista = []

with urlopen(peticion) as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras_lista.append(palabra)

print(palabras_lista)


'''with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(palabras_lista)'''