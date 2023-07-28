# Generadores
# Es una función especial, retorna una secuencia de valores
# suspende la ejecución de la función yield(producir) (no se usa return)

def generador():
    yield 1 # Se suspende la ejecución cada vez que aparece la palabra reservada yield
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3


# Consumimos el generador pero a demanda

gen = generador()

# Con cada llamada consumimos un valor

print(next(gen))
print(next(gen))
print(next(gen))

# Si en este caso pedimos un cuarto valor, nos va a dar error
# Es un error del tipo StopIteration
#  print(next(gen))

# Consumiendo los valores del generador con un ciclo for
# Lo volvemos a llamar porque hemos consumido ya todos los elementos del iterador
for valor in generador():
    print(f'Numero de iteración mostrado {valor}')
