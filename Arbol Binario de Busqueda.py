import matplotlib.pyplot as plt

# Se define la clase TreeNode para representar los nodos del árbol
class TreeNode:
    def __init__(self, key):
        self.key = key  
        self.left = None  # hijo izquierdo
        self.right = None  # hijo derecho

# Función para insertar un nodo en el árbol binario de búsqueda
def insert_node(root, key):
    if root is None:
        return TreeNode(key)  

    # Inserta el nodo en la posición adecuada
    if key < root.key:
        root.left = insert_node(root.left, key)  # Si el valor es menor, inserta en el subárbol izquierdo
    elif key > root.key:
        root.right = insert_node(root.right, key)  # Si el valor es mayor, inserta en el subárbol derecho
    
    return root

# Función recursiva para graficar el árbol binario
def plot_tree(node, x, y, dx):
    if node:
        # Dibuja el nodo actual y su valor
        plt.text(x, y, str(node.key), style='italic')
        
        # Dibuja la conexión con el hijo izquierdo (si existe)
        if node.left:
            plt.plot([x, x - dx], [y - 1, y - 3], 'ko-') 
            plot_tree(node.left, x - dx, y - 4, dx / 2)  
        
        # Dibuja la conexión con el hijo derecho (si existe)
        if node.right:
            plt.plot([x, x + dx], [y - 1, y - 3], 'ko-')  
            plot_tree(node.right, x + dx, y - 4, dx / 2) 

# Función para dibujar el árbol binario
def draw_binary_tree(root):
    plt.figure(figsize=(8, 6))  
    plt.axis('off')  
    plot_tree(root, 0, 0, 30)  
    plt.show()  

# Función para encontrar el nodo mínimo en un subárbol
def find_min_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Función para eliminar un nodo en el árbol binario de búsqueda
def delete_node(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete_node(root.left, key)  # Busca el nodo a eliminar en el subárbol izquierdo
    elif key > root.key:
        root.right = delete_node(root.right, key)  # Busca el nodo a eliminar en el subárbol derecho
    else:  
        if root.left is None:  
            temp = root.right  
            root = None  
            return temp  
        elif root.right is None:  
            temp = root.left  
            root = None  
            return temp  
        
        # Si el nodo a eliminar tiene ambos hijos
        temp = find_min_node(root.right)  
        root.key = temp.key  
        root.right = delete_node(root.right, temp.key)  
    
    return root  

# Ejemplo 
keys = [50, 30, 70, 20, 40, 60, 80]  
root = None  
for key in keys:
    root = insert_node(root, key)  

draw_binary_tree(root)  
