"""
Proporcionar nombre, id, precio, envio gratuito o no.
"""

print('Proporciona los siguientes datos del libro: ')
nombre_input: str = input("Introduce el nombre del libro, por favor: ")
id_input: int = int(input("Introduce el ID del libro, por favor: "))
precio_input: float = float(input("Introduce el precio del libro, por favor: "))
envio_input = input("Introduce [True/False], según si el envío es gratuito o no: ")

if envio_input == 'True':
    envio_input = True
elif envio_input == 'False':
    envio_input = False
else:
    envio_input = 'Valor incorrecto, debe de ser un valor True/False.'

print(f'Nombre del libro: {nombre_input}')
print(f'ID del libro: {id_input}')
print(f'Precio del libro: {precio_input}')
print(f'¿Envío gratuito?: {envio_input}')
