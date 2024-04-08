import time
import numpy as np
import matplotlib.pyplot as plt

# Clase Node para representar un nodo en la lista enlazada
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Clase LinkedList para representar una lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None

    # Método para agregar un nodo al final de la lista enlazada
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Método para convertir la lista enlazada a una lista de Python
    def to_list(self):
        list_ = []
        current = self.head
        while current:
            list_.append(current.data)
            current = current.next
        return list_

# Función para comparar el rendimiento entre lista enlazada y array NumPy
def compare_performance(sizes):
    ll_times = []
    np_times = []

    for size in sizes:
        # Lista enlazada
        ll = LinkedList()
        start_time_ll = time.time()
        for i in range(size):
            ll.append(i)
        end_time_ll = time.time()
        ll_times.append(end_time_ll - start_time_ll)

        # NumPy array
        start_time_np = time.time()
        np_array = np.zeros(size)
        for i in range(size):
            np_array[i] = i
        end_time_np = time.time()
        np_times.append(end_time_np - start_time_np)

    return ll_times, np_times

# Función principal para ejecutar y visualizar los resultados
def main():
    sizes = [10, 100, 1000, 10000]  # Tamaños de datos para comparar
    ll_times, np_times = compare_performance(sizes)

    # Graficando los resultados
    plt.plot(sizes, ll_times, label="Linked List")
    plt.plot(sizes, np_times, label="NumPy Array")
    plt.xlabel('Tamaño de los datos')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de Rendimiento: Lista Enlazada vs NumPy Array')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()