import urllib
from urllib.request import urlopen

peticion = urllib.request.Request(
    "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt",
    data=None,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    },
)

with urlopen(peticion) as mensaje:
    contenido = mensaje.read().decode('utf-8')


# Reemplazar contenido en un str
#print(contenido.replace(' ', '-'))

# Para eliminar caracteres al inicio y al final de una cadena
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original: ', titulo, len(titulo))
titulo = titulo.strip(' ')
print('Cadena modificada:', titulo, len(titulo))
titulo = '*** GlobalMentoring.com.mx ***'
print('Cadena con asteriscos modificados:', titulo.strip('*'))
print('Solo quitamos los de la derecha', titulo.rstrip('*'))
print('Solo quitamos de la izquierda', titulo.lstrip('*'))