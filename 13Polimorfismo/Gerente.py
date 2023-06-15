from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento) -> None:
        super().__init__(nombre=nombre, sueldo=sueldo)
        self._departamento = departamento

    @property 
    def departamento(self):
        return self.departamento
    
    @departamento.setter
    def departamento(self, nuevo_valor):
        self._departamento = nuevo_valor

    def __str__(self) -> str:
        return f'Gerente [Departamento: {self._departamento}] {super().__str__()}'