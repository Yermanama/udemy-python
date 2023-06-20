class MiClase:

    # Las variables de clase son las que se asocian sólo a la clase en si misma
    variable_clase = "Valor variable clase"

    # Las varibales de instancia son las que se asocian a los objetos
    def __init__(self, variable_instancia) -> None:
        self.variable_instancia = variable_instancia

# Para acceder a la variable de clase no hace falta crear objeto
print(MiClase.variable_clase)

# Para acceder a las variables de instancia tenemos que crear un objeto antes
mi_clase = MiClase("Valor variable instancia")
print(mi_clase.variable_instancia)

# Pero desde el objeto también podemos acceder a la variable de clase
print(mi_clase.variable_clase)

# Y lo podemos hacer desde cualquier objeto que creemos a partir de esa clase
mi_clase2 = MiClase("Este es el segundo objeto")
print(mi_clase2.variable_instancia)
print(mi_clase2.variable_clase)

# También debemos de saber que podemos crear variables de clase al vuelo
MiClase.nueva_variable = "Esta es una nueva variable"
# Lo malo es que al definirla al vuelo, el IDE no lo reconoce
# Pero podemos como antes acceder desde la clase o desde los objetos
print("Variables al vuelo")
print(MiClase.nueva_variable)
print(mi_clase.nueva_variable)
print(mi_clase2.nueva_variable)

