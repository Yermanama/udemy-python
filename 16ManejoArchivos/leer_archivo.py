import os

os.chdir('16ManejoArchivos')

print(os.listdir(os.getcwd()))

try:
    with open('prueba.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except Exception as error:
    print(f'Ha habido un error del tipo: {error}')

# También podemos leer solos unas líneas o caracteres del archivo

try:
    with open('prueba.txt', 'r', encoding='utf8') as archivo:
        print('Vamos a leer solo los primeros 5 caracteres.')
        print(archivo.read(5))
except Exception as error:
    print(f'Ha habido un error del tipo {error}')


try:
    with open('prueba.txt', 'a', encoding='utf8') as archivo:
        print('Vamos a añadir una línea más en el archivo.')
        archivo.write('\nEsta es la última línea del archivo')
except Exception as error:
    print(f'Error del tipo -> {error}')

try:
    with open('prueba.txt', 'r', encoding='utf8') as archivo:
        numero_linea = 1 
        for linea in archivo:
            print(f'Numero de línea: {numero_linea} y la línea es: {linea}')
            numero_linea += 1
except Exception as error:
    print(f'El error es -> {error}')


# Podemos leer todas las líneas del archivo, devolviendo una lista con todas las líneas
try:
    with open('prueba.txt', 'r', encoding='utf8') as archivo:
        print(archivo.readlines())
except:
    print('Ha habido un error')

# Abrimos un nuevo archivo:
try:
    with open('copia.txt', 'a', encoding='utf8') as copia:
        contenido = open('prueba.txt', 'r', encoding='utf8').read()
        copia.write(contenido)
except:
    print('Ha habido un error al ejecutar el código.')

# Vamos a borrar todos los archivos que hemos creado

primer_archivo = 'prueba.txt'
segundo_archivo = 'copia.txt'

if os.path.exists(primer_archivo):
    os.remove(primer_archivo)
    print(f'Se ha borrado el archivo -> {primer_archivo}')
else:
    print('El archivo especificado no existe')

if os.path.exists(segundo_archivo):
    os.remove(segundo_archivo)
    print(f'Archivo: {segundo_archivo} eliminado')
else:
    print('El archivo especificado no existe.')
