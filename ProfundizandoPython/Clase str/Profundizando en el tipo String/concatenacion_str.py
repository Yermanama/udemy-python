# Profundización en el tipo str

# Concatenación automática en str
mensaje = 'Hola' 'Mundo'
print(mensaje)

mensaje = 'Hola' + 'Mundo'
print(mensaje)

# En el caso de las variables debemos de usar el +, de la primera manera no funciona
variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
print(mensaje)

# Pero si tenemos literales tipo str, podemos seguir haciéndolo de la manera anterior
mensaje += 'Universidad' 'Python'
print(mensaje)