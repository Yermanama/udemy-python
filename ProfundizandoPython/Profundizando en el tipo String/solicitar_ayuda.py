import math
from uso_doctring import MiClase

# Solicitar ayuda -> Nos da el detalle de la clase a través de la terminal, la documentación.

# help(str)

# También la podemos llamar con objetos o métodos más específicos

# help(str.capitalize)

# Sirve para cualquier tipo de objeto en python que tenga un docstring

# help(math)

# help(math.isnan)

# También podemos solictar ayuda de clases y objetos que hayamos creado nosotros

# help(MiClase)
# help(MiClase.mi_metodo)

# Otras maneras de obtener información de las clases

print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)