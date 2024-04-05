#Primero importamos las librerias time, numpy, y matplotlib
import numpy as np
import time
import matplotlib.pyplot as plt

# Creamos la clase node
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Creamos la clase linked_list
class LinkedList: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = Node(data=data, next_node=self.head)  

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    # Método para imprimir la lista de nodos
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=" => ")
            node = node.next

# Funcion para comparar las velocidades de escritura
def compare_speed(n):
    # Linked list
    ll = LinkedList()
    start_time_ll = time.time()
    for i in range(n):
        ll.add_at_end(i)
    end_time_ll = time.time()

    # NumPy array
    arr = np.empty(n)
    start_time_np = time.time()
    for i in range(n):
        arr[i] = i
    end_time_np = time.time()

    return end_time_ll - start_time_ll, end_time_np - start_time_np

# Main function
def main():
    sizes = [10, 100, 1000, 10000]  # Longitudes de datos para comparar
    ll_times = []  # tiempo de ejecucion de linked list
    np_times = []  # tiempo de ejecucion de NumPy array

    for size in sizes:
        ll_time, np_time = compare_speed(size)
        ll_times.append(ll_time)
        np_times.append(np_time)

    # Graficando resultados
    plt.plot(sizes, ll_times, label="Linked List")
    plt.plot(sizes, np_times, label="NumPy Array")
    plt.xlabel('Size of Data')
    plt.ylabel('Time (seconds)')
    plt.title('Writing Speed Comparison: Linked List vs NumPy Array')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
