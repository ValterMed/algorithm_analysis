class Nodo:
    def __init__(self, valor):
        """
        Inicializa un nuevo nodo en el árbol binario de búsqueda.

        Args:
        - valor: El valor que contendrá el nodo.
        """
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        """
        self.raiz = None

    def insertar(self, valor):
        """
        Inserta un nuevo nodo con el valor dado en el árbol binario de búsqueda.

        Args:
        - valor: El valor que se desea insertar en el árbol.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        """
        Inserta recursivamente un nuevo nodo con el valor dado en el árbol.

        Args:
        - nodo: El nodo actual en el proceso de inserción.
        - valor: El valor que se desea insertar en el árbol.
        """
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
        else:
            # Valor ya existe, no se permite duplicados en un árbol binario de búsqueda
            pass

    def buscar(self, valor):
        """
        Busca si un valor dado está presente en el árbol binario de búsqueda.

        Args:
        - valor: El valor que se desea buscar en el árbol.

        Returns:
        - True si el valor está presente en el árbol, False en caso contrario.
        """
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        """
        Busca recursivamente si un valor dado está presente en el árbol.

        Args:
        - nodo: El nodo actual en el proceso de búsqueda.
        - valor: El valor que se desea buscar en el árbol.

        Returns:
        - True si el valor está presente en el árbol, False en caso contrario.
        """
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)

    def eliminar(self, valor):
        """
        Elimina un nodo con el valor dado del árbol binario de búsqueda.

        Args:
        - valor: El valor del nodo que se desea eliminar del árbol.
        """
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        """
        Elimina recursivamente un nodo con el valor dado del árbol.

        Args:
        - nodo: El nodo actual en el proceso de eliminación.
        - valor: El valor del nodo que se desea eliminar del árbol.

        Returns:
        - El nodo modificado después de la eliminación.
        """
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                nodo.valor = self._encontrar_min_valor(nodo.derecha)
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _encontrar_min_valor(self, nodo):
        """
        Encuentra recursivamente el valor mínimo en el subárbol derecho de un nodo.

        Args:
        - nodo: El nodo raíz del subárbol derecho.

        Returns:
        - El valor mínimo encontrado en el subárbol derecho.
        """
        min_valor = nodo.valor
        while nodo.izquierda is not None:
            min_valor = nodo.izquierda.valor
            nodo = nodo.izquierda
        return min_valor

    def recorrido_inorden(self):
        """
        Realiza un recorrido inorden (izquierda, raíz, derecha) en el árbol.
        """
        return self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo):
        """
        Realiza un recorrido inorden (izquierda, raíz, derecha) recursivo en el árbol.

        Args:
        - nodo: El nodo raíz del subárbol actual.
        """
        if nodo is not None:
            self._recorrido_inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._recorrido_inorden_recursivo(nodo.derecha)


# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arbol.insertar(valor)

print("Recorrido Inorden:")
arbol.recorrido_inorden()

print("\nBuscando el valor 40:", arbol.buscar(40))
print("Buscando el valor 100:", arbol.buscar(100))

arbol.eliminar(30)
print("\nRecorrido Inorden después de eliminar el nodo con valor 30:")
arbol.recorrido_inorden()
