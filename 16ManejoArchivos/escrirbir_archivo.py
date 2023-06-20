# Primero vamos a abrir, y en el caso de que no exista el archivo lo creará
# Lo metemos dentro de un try, except por si esto arroja algún problema
import os

directorio_objetivo = os.chdir('16ManejoArchivos')
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') # Se creará el archivo en la carpeta en donde estamos trabajando
    archivo.write('Agregamos informacion en el archivo creado/existido.\n')
    archivo.write('Adios.')
except Exception as error:
    print(f'Ha habido un error del tipo {error}')
finally: # Recordemos que siempre se ejecuta este bloque de código
    archivo.close() # Ya no vamos a poder editar el texto hasta que no lo abramos de nuevo
    print('Archivo cerrado, no se puede editar hasta que lo abras de nuevo')


