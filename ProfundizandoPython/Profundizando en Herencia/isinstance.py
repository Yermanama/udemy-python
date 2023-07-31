class ListaSimple:

    def __init__(self, elementos) -> None:
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]
    
    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return(self._elementos)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._elementos})'
    

class ListaOrdenada(ListaSimple):

    def __init__(self, elementos) -> None:
        super().__init__(elementos)
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        super().ordenar()
        

class ListaEnteros(ListaSimple):
    
    def __init__(self, elementos) -> None:
        for elemento in elementos:
            self._validar(elemento)
        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'No es un número entero: {elemento}')
        
    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass



lista_ent_ord = ListaEnterosOrdenada([-3, -54, 0, 67, 1, 23])
print(lista_ent_ord)

print(isinstance(lista_ent_ord, ListaEnterosOrdenada))
print(isinstance(lista_ent_ord, ListaEnteros))
print(isinstance(lista_ent_ord, ListaOrdenada))
print(isinstance(lista_ent_ord, ListaSimple))
print(isinstance(lista_ent_ord, object))
# Devuelve verdadero si está en alguno de los elementos, es de tipo OR
print(isinstance(lista_ent_ord, (ListaEnteros, ListaOrdenada, ListaSimple, ListaEnterosOrdenada, object)))