"""with open('archivo.txt', 'r', encoding='utf8') as archivo:
    print(archivo.readlines())"""

from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

