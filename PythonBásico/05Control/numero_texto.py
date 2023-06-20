numero_input: int = int(input("Escribe un número, el que quieras: "))

if numero_input == 1:
    print(f'{numero_input} es el número uno.')
elif numero_input == 2:
    print(f'El {numero_input} es el número dos.')
elif numero_input == 3:
    print(f'El {numero_input} es el número tres.')
else:
    print(f'El {numero_input} es más que los tres primeros números, por lo que no lo he programado.')
