# Dar formato con format

nombre = 'Juan'
edad = 38
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)


mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1} '.format(nombre, edad, sueldo)
print(mensaje)


mensaje = 'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'.format(nombre=nombre, edad =edad, sueldo=sueldo)
print(mensaje)

diccionario = {'nombre' : 'Ignacio', 'edad': 28, 'sueldo': 8000.00}
mensaje = 'Nombre {persona[nombre]} Edad {persona[edad]} Sueldo {persona[sueldo]:.2f}'.format(persona = diccionario)