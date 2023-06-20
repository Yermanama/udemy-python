class ManejoArchivos:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self._nombre, 'r', encoding='utf8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()
            
