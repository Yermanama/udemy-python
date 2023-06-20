from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

lista_opciones = [1, 2, 3, 4]
estado = True
catalogo1 = CatalogoPeliculas()

while estado:
    opcion = None
    while opcion not in lista_opciones:
        print("\nPor favor, introduce uno de los siguientes valores para proceder con el programa:")
        print("1) Agregar una película al catálogo")
        print("2) Listar las películas que hay en el catálogo")
        print("3) Eliminar el archivo películas")
        print("4) Salir del programa\n")

        opcion = int(input('Introduce tu elección: '))

        if opcion == 1:
            nombre_pelicula = input('Por favor, escribe el nombre de la película que quieres añadir: ')
            pelicula = Pelicula(nombre_pelicula)
            catalogo1.agregar_pelicula(pelicula_nueva=pelicula)
        elif opcion == 2:
            print("Las películas en el catálogo son:")
            catalogo1.listar_peliculas()
        elif opcion == 3:
            print("Eliminando archivo de películas...")
            catalogo1.eliminar()
        elif opcion == 4:
            print("Saliendo del programa...")
            estado = False


