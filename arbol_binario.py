class Nodo:
    """Representa un nodo en un árbol binario."""
    def __init__(self, valor):
        """Inicializa un nodo con el valor dado."""
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    """Representa un árbol binario."""
    def __init__(self):
        """Inicializa un árbol binario vacío."""
        self.raiz = None

    def insertar(self, valor):
        """Inserta un nuevo valor en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def buscar(self, valor):
        """Busca un valor en el árbol."""
        return self._buscar_recursivo(valor, self.raiz)

    def imprimir_inorden(self):
        """Imprime los valores del árbol en orden (inorden)."""
        self._imprimir_inorden_recursivo(self.raiz)
