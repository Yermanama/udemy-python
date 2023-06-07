# Dada la siguiente tupla,
# crear una lista que sólo incluya los números menores a 5
tupla = (13, 1, 8, 3, 2, 5, 8)
tuplaLista = list(tupla)
for numero in tuplaLista:
    if numero > 5:
        tuplaLista.remove(numero)

print(tuplaLista)
