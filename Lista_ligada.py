class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaLigada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, valor):
        if not self.cabeza:
            self.cabeza = Nodo(valor)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(valor)

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" ")
            actual = actual.siguiente
        print()

    def __eq__(self, otra_lista):
        actual_self = self.cabeza
        actual_otra = otra_lista.cabeza
        while actual_self and actual_otra:
            if actual_self.valor != actual_otra.valor:
                return False
            actual_self = actual_self.siguiente
            actual_otra = actual_otra.siguiente
        # Las listas deben tener la misma longitud
        return actual_self is None and actual_otra is None


# Creamos dos listas ligadas
lista_1 = ListaLigada()
lista_1.insertar_al_final(1)
lista_1.insertar_al_final(2)
lista_1.insertar_al_final(3)

lista_2 = ListaLigada()
lista_2.insertar_al_final(1)
lista_2.insertar_al_final(2)
lista_2.insertar_al_final(3)

# Imprimimos ambas listas
print("Lista 1:")
lista_1.imprimir()
print("Lista 2:")
lista_2.imprimir()

# Comparamos las listas
if lista_1 == lista_2:
    print("Las listas son iguales")
else:
    print("Las listas son diferentes")
