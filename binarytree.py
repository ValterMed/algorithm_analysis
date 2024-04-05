#Declaramos la clase TreeNode, que servira como punto de referencia
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#Declaramos la clase binarytree que servira para insertar valores en el arbol
class BinaryTree:
    def __init__(self):
        self.root = None

    # Metodo para insertar nodos nuevos y buscar nodos existentes
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            # Si el valor ya existe en el arbol, se omite
            pass

    # Metodo para hacer un recorrido en orden del arbol
    def inorder_traversal(self):
        if self.root:
            self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, current_node):
        if current_node:
            self._inorder_traversal_recursive(current_node.left)
            print(current_node.value, end=" ")
            self._inorder_traversal_recursive(current_node.right)

    # Metodo de busqueda de un nodo especifico
    def search_node(self, value):
        return self._search_node_recursive(self.root, value)

    def _search_node_recursive(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_node_recursive(current_node.left, value)
        return self._search_node_recursive(current_node.right, value)

    # Metodo para imprimir un nodo especifico y sus nodos hijos
    def print_subtree(self, node):
        if node:
            print("Subtree rooted at node", node.value, ":")
            self._inorder_traversal_recursive(node)
        else:
            print("Node not found!")

# Ejemplo:
if __name__ == "__main__":
    # Instanciamos el objeto BinaryTree e insertamos valores
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.insert(1)  
    tree.insert(9)  
    # Imprimimos el arbol completo en orden
    print("Inorder Traversal:")
    tree.inorder_traversal()
    print("\n")

    # Buscamos el nodo con valor 2 (reemplace para buscar otro)
    target_value = 2
    target_node = tree.search_node(target_value)
    if target_node:
        print("Found node with value", target_value)
        tree.print_subtree(target_node)
    else:
        print("Node with value", target_value, "not found in the tree")

