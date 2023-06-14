from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100)
producto2 = Producto('Pantalón', 120)
producto3 = Producto('Sudadera', 300)
producto4 = Producto('Calcentines', 70)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
orden2 = Orden(productos=productos2)

print(orden1)
print(f'Calcular el total de la orden 1: {orden1.sumar_precios()}')
print("Añadimos productos a la primera orden")
orden1.añadir_producto(producto=producto3)
print(orden1)
print(f'Calculamos el total: {orden1.sumar_precios()}')
print(orden2)
print(f'Caluclar el total de la orden 2: {orden2.sumar_precios()}')
