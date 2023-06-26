# Profundizando en el tipo float

a = 3.0
print(f'a -> {a}')

print(f'a:2f para float con dos decimales -> {a:.2f}')

# Constructor floar puede recibir tanto str como int

a = int(10)
print(f'Valor de int a float con dos decimales {a:.2f}')

a = float('10')
print(f'Valor de string de a float con dos decimales {a:.2f}')

# Notación exponencial (valores positivos o negativos)

a = 3e5
print(f'La notación exponencial nos permite acortar la manera en la que escribimos números muy grandes. -> {a:.2f}')

a= 3e-5
print(f'También podemos usar la notación exponencial para números negativos: {a:.5f}')

# Cualquier cálculo que involucre un float, se promueve a float
a = 4.0 + 5
print(f'Podemos ver si hay un float entre medias, el resultado es un float-> {a}')