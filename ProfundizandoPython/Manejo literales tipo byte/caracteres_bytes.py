
# Caracteres byte
# Si ponemos la b delante de la cadena, indicamos que los caracteres deben de tener caraceteres tipo byte   
caracteres_en_byte = b'Hola mundo'
print(caracteres_en_byte)

mensaje = b'Universdiad de python'
print(mensaje[0])
# Este print nos devuelve 85 en vez de U, ya que corresponde el valor en byte de la primera posición -> La U 
print(chr(mensaje[0]))
# Este print nos devuelve el valor de U, ya que 85 corresponde a dicho caracter en ascii


print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir de str a bytes
string = 'Programación con python'
print(f'La string original es: {string}')

# UTF-8 soporta acentos por lo que es el tipo de codificación que tiene la variable string
# Para pasarlo a bytes usamos el método encode
bytes = string.encode('utf-8')
print(f'Ahora esta es la literal en bytes: {bytes}')


# Convertir de bytes a str
string2 = bytes.decode('utf-8')
print(f'Volvemos a pasar decodificado: {string2}')