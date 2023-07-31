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
        return len(self._elementos)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{(self._elementos)}"


class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]) -> None:
        super().__init__(elementos)
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        self.ordenar()


class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]) -> None:
        for elemento in elementos:
            self._validar(elemento)
        super().__init__(elementos)

    def _validar(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f"No es un valor entero {elemento}")

    def agregar(self, elemento):
        self._validar(elemento)
        super().agregar(elemento)


class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass


# Lista entero ordenadas
lista_enteros_ordenada = ListaEnterosOrdenada([4, -4, 5, 10, 16, 0, 1])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(2)
print(lista_enteros_ordenada)

# Saber las clases padres y su orden
print(
    ListaEnterosOrdenada.__bases__
)  # (<class '__main__.ListaEnteros'>, <class '__main__.ListaOrdenada'>)

# MRO (Method resolution Order) -> De esta manera vemos el orden de las métodos que se van a llamar
print(
    ListaEnterosOrdenada.mro()
)  # [<class '__main__.ListaEnterosOrdenada'>, <class '__main__.ListaEnteros'>, <class '__main__.ListaOrdenada'>, <class '__main__.ListaSimple'>, <class 'object'>]
