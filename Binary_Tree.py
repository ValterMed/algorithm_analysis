class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # Si el árbol está vacío, crea un nuevo nodo con el valor dado
    if root is None:
        return Node(key)
    else:
        # Si el valor es mayor que el valor actual del nodo, inserta en el sub árbol derecho
        if root.val < key:
            root.right = insert(root.right, key)
        # Si el valor es menor o igual, inserta en el sub árbol izquierdo
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        # Recorre primero el sub árbol izquierdo
        inorder(root.left)
        # Imprime el valor del nodo actual
        print(root.val)
        # Finalmente recorre el sub árbol derecho
        inorder(root.right)

def preorder(root):
    if root:
        # Imprime el valor del nodo actual primero
        print(root.val)
        # Recorre el sub árbol izquierdo
        preorder(root.left)
        # Finalmente recorre el sub árbol derecho
        preorder(root.right)

def postorder(root):
    if root:
        # Recorre primero el sub árbol izquierdo
        postorder(root.left)
        # Luego recorre el sub árbol derecho
        postorder(root.right)
        # Imprime el valor del nodo actual
        print(root.val)

def find_min_node(node):
    # Encuentra el nodo con el valor mínimo en un árbol dado
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        # Si el valor a eliminar es menor que el valor actual, buscar en el sub árbol izquierdo
        root.left = delete_node(root.left, key)
    elif key > root.val:
        # Si el valor a eliminar es mayor que el valor actual, buscar en el sub árbol derecho
        root.right = delete_node(root.right, key)
    else:
        # Si el nodo a eliminar tiene un solo hijo o ninguno
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Si el nodo a eliminar tiene dos hijos, encontrar el sucesor inorden (nodo con el valor mínimo en el subárbol derecho)
        temp = find_min_node(root.right)
        # Copiar el valor del sucesor inorden al nodo actual
        root.val = temp.val
        # Eliminar el sucesor inorden
        root.right = delete_node(root.right, temp.val)

    return root

def display_menu():
    print("1. Insertar nodo")
    print("2. Eliminar nodo")
    print("3. Recorrer en orden")
    print("4. Recorrer en preorden")
    print("5. Recorrer en postorden")
    print("6. Salir")
    return int(input("Seleccione una opción: "))

root = None

while True:
    choice = display_menu()
    if choice == 1:
        key = int(input("Ingrese el valor del nodo a insertar: "))
        root = insert(root, key)
    elif choice == 2:
        key = int(input("Ingrese el valor del nodo a eliminar: "))
        root = delete_node(root, key)
    elif choice == 3:
        print("Recorrido en orden:")
        inorder(root)
    elif choice == 4:
        print("Recorrido en preorden:")
        preorder(root)
    elif choice == 5:
        print("Recorrido en postorden:")
        postorder(root)
    elif choice == 6:
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida entre 1 y 6.")
