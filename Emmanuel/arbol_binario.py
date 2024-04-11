class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def _imprimir_recursivo(self, nodo, espacio):
        if nodo is not None:
            espacio += 5
            self._imprimir_recursivo(nodo.derecha, espacio)
            print()
            for _ in range(5, espacio):
                print(end=" ")
            print(nodo.valor)
            self._imprimir_recursivo(nodo.izquierda, espacio)

    def imprimir(self):
        self._imprimir_recursivo(self.raiz, 0)

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(7)
arbol.insertar(3)
arbol.insertar(12)
arbol.insertar(14)
arbol.insertar(20)
arbol.insertar(18)
arbol.insertar(16)

# Mostrar el árbol binario
print("Árbol binario:")
arbol.imprimir()
