"""Proporciona tu edad:

0-10: La infancia es increíble...
10-20: Muchos cambios y mucho estudio... 
20-30: Amor y comienza el trabajo...

Cualquier otro valor: Etapa de vida no reconocida
"""

input_usuario: int = int(input('Dime cuantos años tienes: '))

if 0 <= input_usuario <= 10:
    print('La infancia es increíble... ')
elif 10 < input_usuario <= 20:
    print('Muchos cambios y mucho estudio...')
elif 20 < input_usuario <= 30:
    print('Amor y comienza el trabajo...')
else:
    print('Etapa de vida no reconocida.')
