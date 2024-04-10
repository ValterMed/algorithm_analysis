import numpy as np
import matplotlib.pyplot as plt

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = np.array([value, -1])  # El segundo elemento es el índice del siguiente nodo (-1 si no hay más nodos)
        else:
            current = self.head
            while current[1] != -1:
                current_index = int(current[1])
                current = self.array[current_index]
            new_node_index = len(self.array)
            new_node = np.array([value, -1])
            current[1] = new_node_index

    def display(self):
        current = self.head
        while current is not None:
            print(current[0], end=" -> ")
            current_index = int(current[1])
            current = self.array[current_index]

# Crear una lista enlazada
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# Mostrar la lista enlazada
linked_list.display()

# Visualizar la lista enlazada utilizando matplotlib
values = []
current = linked_list.head
while current is not None:
    values.append(current[0])
    current_index = int(current[1])
    current = linked_list.array[current_index]

plt.figure(figsize=(8, 6))
plt.title("Linked List")
plt.plot(values, marker='o', linestyle='-')
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
