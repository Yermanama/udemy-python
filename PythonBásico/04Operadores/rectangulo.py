print("Hola este es un programa para calcular el área y el perímetro  de tu rectángulo, vamos a proceder.")
height: int = int(input("Por favor, introduce el valor de la altura de tu rectángulo: "))
width: int = int(input("Ahora introduce el valor del ancho de tu rectángulo: "))

area: int = height * width
perimeter: int = 2*height + 2*width

print(f"Area: {area}\n"
      f"Perimetro: {perimeter}")
