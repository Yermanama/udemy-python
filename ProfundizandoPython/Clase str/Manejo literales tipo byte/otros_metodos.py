import urllib
from urllib.request import urlopen

peticion = urllib.request.Request(
    "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt",
    data=None,
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    },
)

with urlopen(peticion) as archivo:
    contenido = archivo.read().decode('utf-8')
    

# Contar ocurrencias de una cadena dentro de otra
print('Numero de veces que aparece universidad en contenido',contenido.count('Universidad'))    

# Para transformar todo el contenido en mayúsculas
print(contenido.upper())

# Para transformar el contenido en minúsculas
print(contenido.lower())

# Para saber si una cadena se encuentra en otra - es siempre mejor convertirlo todo a minúsculas para que no falle
print('python'.lower() in contenido.lower())

#También se puede hacer la comprobación en mayúsculas
print('python'.upper() in contenido.upper())

# Empieza con o termina con 
print(contenido.startswith('En GlobalMentoring.com.mx'))
print(contenido.endswith('GlobalMentoring.com.mx'))

# Comprobar si una cadena es todo minúscula o todo mayúscula
mensaje = 'mensaje en minúsculas'
print(mensaje.islower())
mensaje = 'MENSAJE EN MAYÚSCULAS'
print(mensaje.isupper())