# Template literal

nombre = 'Juan'
edad = 23
sueldo = 8988.00

mensaje = f'Nombre {nombre} edad {edad} sueldo {sueldo:.1f}'
print(mensaje)

# Con el método print podemos tambien darle algún formato
print(nombre, edad, sueldo, sep=', ')