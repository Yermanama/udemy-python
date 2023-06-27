

if bool(''):
    print('Devuelve verdadero')
else:
    print('Devuelve falso, porque es una cadena vacía.')

# Python funciona de manera que esta sentencia de aquí abajo es lo mismo que la de arriba

if '':
    print('Devuelve verdadero')
else:
    print('Devuelve falso, porque es una cadena vacía.')


if (1,2):
    print('Devuelve verdadero, al ser una tupla con valores en su interior.')
else:
    print('Esta parte de aquí no se va a reproducir.')


# Lo mismo ocurre con los valores en while

variable = 0
while variable:
    print('Esta parte de aquí no se reproduce.')

variable = 1

while variable:
    print('Este ciclo se ejecuta de manera infinita. Por lo que ponemos un break.')
    break
