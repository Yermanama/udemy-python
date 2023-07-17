# Para centrar un Sring 
titulo = 'Hola Me Llamo German'
print(titulo.center(len(titulo)+20, '*'))

# Para alinear a la izquierda
print(titulo.ljust(len(titulo) + 20, '-'))

# Para alinear a la derecha
print(titulo.rjust(len(titulo) + 20, '+'))