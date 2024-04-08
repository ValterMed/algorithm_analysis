
class NodoArbol:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Funcion para crear el árbol

class ArbolBinarioBusqueda:
    def __init__(self):
        self.root = None

    def insertar(self, value):
        if self.root is None:
            self.root = NodoArbol(value)
        else:
            self._insertar_recursivo(self.root, value)

    def _insertar_recursivo(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = NodoArbol(value)
            else:
                self._insertar_recursivo(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = NodoArbol(value)
            else:
                self._insertar_recursivo(node.right, value)

    def buscar(self, value):
        return self._buscar_recursivo(self.root, value)

    def _buscar_recursivo(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._buscar_recursivo(node.left, value)
        else:
            return self._buscar_recursivo(node.right, value)

    def _imprimir_recursivo(self, node, space):
        if node is not None:
            space += 5
            self._imprimir_recursivo(node.right, space)
            print()
            for _ in range(5, space):
                print(end=" ")
            print(node.value)
            self._imprimir_recursivo(node.left, space)

    def imprimir(self):
        self._imprimir_recursivo(self.root, 0)


# Ejemplo de uso
#Insertar valores al arbol
arbol = ArbolBinarioBusqueda()
arbol.insertar(20)
arbol.insertar(9)
arbol.insertar(15)
arbol.insertar(9)
arbol.insertar(1)
arbol.insertar(12)
arbol.insertar(14)
arbol.insertar(23)
arbol.insertar(19)
arbol.insertar(1)

# Mostrar el árbol binario
print("Árbol binario:")
arbol.imprimir()
