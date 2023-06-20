from Dominio.Pelicula import Pelicula
import os

class CatalogoPeliculas:

    ruta_archivo = 'Catalogo_peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula_nueva: Pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'\n{pelicula_nueva.nombre}')


    @classmethod
    def listar_peliculas(cls):
        try:
            with open(cls.ruta_archivo, 'r', encoding= 'utf8') as archivo:
                print(archivo.read())
        except Exception as error:
            print(f'Ha habido un error del tipo {error}')

    @classmethod
    def eliminar(cls):
        try:
            os.remove(cls.ruta_archivo)
        except Exception as error:
            print(f'Ha habido un error del tipo {error}')
    
    