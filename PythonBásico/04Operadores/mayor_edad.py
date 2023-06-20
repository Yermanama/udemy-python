edad: int = int(input('Por favor, inserta tu edad en número: '))
edad_adultos: int = 18
if edad >= edad_adultos:
    print(f'La persona con la edad de {edad} es un adulto.')
else:
    print(f'La persona con la edad de {edad} es menor de edad.')
