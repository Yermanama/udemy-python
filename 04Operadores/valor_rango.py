valor_input: int = int(input('Introduce un valor: '))
valor_inferior: int = 1
valor_superior: int = 5

# Esto es para el ejercicio
"""if valor_input >= 1 and valor_input <= 5:
    print(f'El número {valor_input} está en rango [1,5]')
else: 
    print(f'El número {valor_input} NO está en rango [1,5]')"""

if valor_inferior <= valor_input <= valor_superior:
    print(f'El número {valor_input} está en rango [1,5]')
else:
    print(f'El número {valor_input} NO está en rango [1,5]')
