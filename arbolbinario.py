import random
import plotly.express as px

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

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
            # Ignorar nodos duplicados
            pass

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        return self._search_recursive(current_node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            min_value = self._find_min_value(current_node.right)
            current_node.value = min_value
            current_node.right = self._delete_recursive(current_node.right, min_value)

        return current_node 

    def _find_min_value(self, current_node):
        min_value = current_node.value
        while current_node.left is not None:
            min_value = current_node.left.value
            current_node = current_node.left
        return min_value

    def inorder_traversal(self):
        values = []
        self._inorder_traversal_recursive(self.root, values)
        return values

    def _inorder_traversal_recursive(self, current_node, values):
        if current_node is not None:
            self._inorder_traversal_recursive(current_node.left, values)
            values.append(current_node.value)
            self._inorder_traversal_recursive(current_node.right, values)

    def plot_tree(self):
        depths = []
        values = []
        self._plot_tree_recursive(self.root, 0, depths, values)
        fig = px.line(x=depths, y=values, title='Binary Search Tree: Depth vs Value')
        fig.update_layout(xaxis_title='Depth', yaxis_title='Value')
        fig.show()

    def _plot_tree_recursive(self, current_node, depth, depths, values):
        if current_node is not None:
            self._plot_tree_recursive(current_node.left, depth + 1, depths, values)
            depths.append(depth)
            values.append(current_node.value)
            self._plot_tree_recursive(current_node.right, depth + 1, depths, values)

# Ejemplo de uso
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insertar algunos valores aleatorios
    for _ in range(10):
        value = random.randint(1, 100)
        bst.insert(value)

    # Verificar inserción correcta
    print("Inorder traversal:")
    print(bst.inorder_traversal())

    # Buscar un valor en el árbol
    search_value = 50
    found_node = bst.search(search_value)
    if found_node:
        print(f"El valor {search_value} está presente en el árbol")
    else:
        print(f"El valor {search_value} NO está presente en el árbol")

    # Eliminar un valor del árbol
    delete_value = 50
    bst.delete(delete_value)

    # Verificar que se eliminó correctamente
    found_node = bst.search(delete_value)
    if not found_node:
        print(f"El valor {delete_value} fue eliminado correctamente del árbol")

    # Visualizar el árbol
    bst.plot_tree()

