import time
import numpy as np
import matplotlib.pyplot as plt

# Se define la clase Node para representar un nodo en la lista enlazada
class Node:
    def __init__(self, data):
        self.data = data  # Valor del nodo
        self.next = None  # Siguiente nodo

# Se define la clase LinkedList para la lista enlazada
class LinkedList:
    def __init__(self):
        self.head = None  

    # Método para insertar un nuevo nodo al principio de la lista
    def insert_at_beginning(self, data):
        new_node = Node(data)  
        new_node.next = self.head  
        self.head = new_node  

# Función para medir el tiempo de inserción en una lista enlazada
def linked_list_insertion_time(num_elements):
    linked_list = LinkedList() 
    start_time = time.time()  
    for i in range(num_elements):
        linked_list.insert_at_beginning(i)  
    end_time = time.time()  
    return end_time - start_time  

# Función para medir el tiempo de inserción en un array NumPy
def numpy_array_insertion_time(num_elements):
    array = np.empty(0, dtype=int) 
    start_time = time.time()  
    for i in range(num_elements):
        array = np.insert(array, 0, i) 
    end_time = time.time()  
    return end_time - start_time  

num_elements_list = [100, 500, 1000, 5000, 10000]  # Lista de tamaños de elementos a probar
linked_list_times = []  # Lista para almacenar los tiempos de inserción en la lista enlazada
numpy_array_times = []  # Lista para almacenar los tiempos de inserción en el array NumPy

# Itera sobre los diferentes tamaños de elementos y mide los tiempos de inserción
for num_elements in num_elements_list:
    linked_list_time = linked_list_insertion_time(num_elements)  
    numpy_array_time = numpy_array_insertion_time(num_elements)  
    linked_list_times.append(linked_list_time)  
    numpy_array_times.append(numpy_array_time)  


# Se grafican los tiempos de inserción en función del número de elementos para ambas estructuras de datos
plt.plot(num_elements_list, linked_list_times, label="Lista enlazada") 
plt.plot(num_elements_list, numpy_array_times, label="Array NumPy")  
plt.xlabel("Número de elementos") 
plt.ylabel("Tiempo de inserción (segundos)")  
plt.title("Comparación del tiempo de inserción")  
plt.legend() 
plt.show()  

