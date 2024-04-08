class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar_nodo(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_nodo_recursivo(self.raiz, valor)

    def _insertar_nodo_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_nodo_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_nodo_recursivo(nodo.derecha, valor)

    def buscar_valor(self, valor):
        return self._buscar_valor_recursivo(self.raiz, valor)

    def _buscar_valor_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_valor_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_valor_recursivo(nodo.derecha, valor)

    def _imprimir_nodos_recursivo(self, nodo, espacio):
        if nodo is not None:
            espacio += 5
            self._imprimir_nodos_recursivo(nodo.derecha, espacio)
            print()
            for _ in range(5, espacio):
                print(end=" ")
            print(nodo.valor)
            self._imprimir_nodos_recursivo(nodo.izquierda, espacio)

    def imprimir_arbol(self):
        self._imprimir_nodos_recursivo(self.raiz, 0)

#Ejemplo
arbol_busqueda = ArbolBusqueda()
arbol_busqueda.insertar_nodo(1)
arbol_busqueda.insertar_nodo(2)
arbol_busqueda.insertar_nodo(33)
arbol_busqueda.insertar_nodo(4)
arbol_busqueda.insertar_nodo(55)
arbol_busqueda.insertar_nodo(7)
arbol_busqueda.insertar_nodo(66)
arbol_busqueda.insertar_nodo(13)
arbol_busqueda.insertar_nodo(77)
arbol_busqueda.insertar_nodo(9)

#Print del árbol
print("Árbol de búsqueda:")
arbol_busqueda.imprimir_arbol()