from Computadora import Computadora

class Orden():

    contador_ordenes: int = 0
    
    @classmethod
    def asignarID(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes
    
    def __init__(self) -> None:
        self._id_orden: int = self.asignarID()
        self._lista_computadoras = []

    def agregarComputadora(self, computadora_nueva: Computadora):
        self._lista_computadoras.append(computadora_nueva)

    @property
    def lista_computadoras(self):
        return self._lista_computadoras
    
    @lista_computadoras.setter
    def lista_computadoras(self, nueva_lista: list):
        self._lista_computadoras = nueva_lista

    def __str__(self) -> str:
        computadoras_str = '\n---\n'.join(str(computadora) for computadora in self._lista_computadoras)
        return (f'*** Orden ***\n'
                f'ID: {self._id_orden}\n'
                f'Computadoras: \n{computadoras_str}\n'
                f'****************')

                
