# Generador de numeros del 1 al 5

def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución') # Porque sabemos que se suspende la ejecución cada vez que vemos la palabra yield

# Utilizamos el generador 
generador = generador_numeros()
print(f'Objeto generador: {generador}') # Saldrá que es un objeto de tipo generador
print(type(generador))

# Consumimos los valores del generador

for valor in generador:
    print(f'Valor generador {valor}')

# Consumir a demanda
generador = generador_numeros() # Lo volvemos a llamar porque ya se había consumido anteriormente

try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir el generador: {e}')

# Otra forma de consumir el generador

generador = generador_numeros()

while True:
    try:
        valor = next(generador)
        print(f'Imprimmos el valor: {valor}')
    except StopIteration as e:
        print('Se terminó de iterar el generador')
        break