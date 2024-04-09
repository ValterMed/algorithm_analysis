import networkx as nx
import matplotlib.pyplot as plt

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

    def _crear_grafo_recursivo(self, G, nodo):
        if nodo is not None:
            G.add_node(nodo.valor)
            if nodo.izquierda is not None:
                G.add_edge(nodo.valor, nodo.izquierda.valor)
                self._crear_grafo_recursivo(G, nodo.izquierda)
            if nodo.derecha is not None:
                G.add_edge(nodo.valor, nodo.derecha.valor)
                self._crear_grafo_recursivo(G, nodo.derecha)

    def dibujar_arbol(self):
        G = nx.DiGraph()
        self._crear_grafo_recursivo(G, self.raiz)
        pos = nx.spring_layout(G)  # Posición de los nodos
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()

# Ejemplo
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

# Dibujar árbol
print("Dibujando el árbol de búsqueda:")
arbol_busqueda.dibujar_arbol()
