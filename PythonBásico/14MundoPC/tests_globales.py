from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

raton1 = Raton('Bluetooth', 'racer')
teclado1 = Teclado('Cable', 'Asus')
monitor1 = Monitor('AOC', 'Grande')
computadora1 = Computadora("Mi ordenador", monitor1, teclado1, raton1)

raton2 = Raton('Cable', 'Logitech')
teclado2 = Teclado('Wireless', 'Mars Gaming')
monitor2 = Monitor('HP', 'Pequeña')
computadora2 = Computadora('Computadora Carmen', monitor2, teclado2, raton2)


orden_prueba = Orden()
orden_prueba.agregarComputadora(computadora_nueva=computadora1)
orden_prueba.agregarComputadora(computadora_nueva=computadora2)

print(orden_prueba)