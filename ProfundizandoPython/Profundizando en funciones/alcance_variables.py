# También se conoce como scope, donde podemos usar las variables

# Si la definimos fuera de cualquier función se puede utilizar en donde queramos
var_global = "Variable global"


def imprimir():
    global var_global
    # Para acceder a una variable global pero accedida desde una función
    print(f"Esta es una variable global {var_global}")
    # Definición de variable global - Esta solo se peude acceder dentro del lugar donde se definió - Pero si que se puede en las funciones anidadas
    var_local = "Variable local"
    print(f"Esta es una variable local{var_local}")
    def funcion_anidada():
        print(f'Aqui todaváía se pueden acceder a las dos variables {var_global}, {var_local}')
    funcion_anidada()

    # SI queremos cambiar el valor dentro de la función de la variable global, no nos deja porque no está asociada a un valor dentro de la función y al reconoce como error
    var_global = 'Hola que tal'

    # SI queremos hacer el cambio de verdad podemos indicar que estamos trabajando con una variable global al inicio de la función 
    var_global = 'Nuevo nombre de la variable global '

imprimir()
print(f'Variable global fuera de la función : {var_global}')
# print(f'Variable local desde fuera de la función : {var_local}') -> Esto no se puede hacer

