print("Hola, este es un programa que sirve para saber si un número es par o es impar")

num: int = int(input("Escribe el primer número por favor: "))
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")
