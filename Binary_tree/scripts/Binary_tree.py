

# Python class that represents a single node in a binary tree
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
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            # Ignorar nodos duplicados
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecha)
      
if __name__ == '__main__':
    
    arbol = ArbolBinarioBusqueda()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(15)
    arbol.insertar(3)
    arbol.insertar(7)
    arbol.insertar(12)
    arbol.insertar(18)

    print(arbol.buscar(10))  # True
    print(arbol.buscar(5))   # True
    print(arbol.buscar(15))  # True
    print(arbol.buscar(3))      