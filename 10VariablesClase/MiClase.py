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