class Producto:

    contador_productos = 0

    @classmethod
    def generar_nuevo_valor(cls):
        cls.contador_productos += 1
        return cls.contador_productos
    
    def __init__(self, nombre: str, precio: float) -> None:
        self._id_producto = self.generar_nuevo_valor()
        self._nombre = nombre
        self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio
        


    def __str__(self) -> str:
        return f'Objeto tipo Producto [Id: {self._id_producto} | Nombre: {self._nombre} | Precio: {self._precio}]'
    

if __name__ == "__main__":
    producto1 = Producto("Camisa", 10.00)
    producto2 = Producto("Pantalón", 15.00)
    print(producto1, producto2, sep='\n')