from Producto import Producto

class Orden:
    
    contador_ordenes = 0

    @classmethod
    def generar_nueva_orden(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    
    def __init__(self, productos: list) -> None:
        self._id_orden: int = self.generar_nueva_orden()
        self._lista_productos: list = list(productos)

    def añadir_producto(self, producto):
        self._lista_productos.append(producto)

    
    def sumar_precios(self):
        total = 0 
        for producto in self._lista_productos:
            total += producto.precio
        return total

    @property
    def lista_productos(self):
        return self._lista_productos
    
    @lista_productos.setter
    def id_orden(self, nueva_lista: list):
        self._lista_productos = nueva_lista

    def __str__(self) -> str:
        producto_str = ''
        for producto in self._lista_productos:
            producto_str += producto.__str__() + ' | '
        return f'Objeto tipo Orden [Id: {self._id_orden} | Lista de productos: {producto_str}]'
    

if __name__ == "__main__":
    producto1 = Producto("Camiseta", 10)
    producto2 = Producto("Pantalón", 12)
    productos = [producto1, producto2]
    orden1 = Orden(productos)
    print(orden1)