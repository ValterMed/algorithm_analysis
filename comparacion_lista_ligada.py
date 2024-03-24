# Importamos las bibliotecas necesarias
import time
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def to_list(self):
        list_ = []
        current = self.head
        while current:
            list_.append(current.data)
            current = current.next
        return list_

class NumPyLinkedList:
    def __init__(self):
        self.array = np.array([])

    def append(self, data):
        self.array = np.append(self.array, data)

    def to_list(self):
        return self.array.tolist()

def sub_suma_max(arr):
    max_suma = 0
    for i in range(len(arr)):
        sub_suma = 0
        for j in range(i, len(arr)):
            sub_suma += arr[j]
            if sub_suma > max_suma:
                max_suma = sub_suma
    return max_suma

sizes = np.arange(1, 1001, 100)
execution_times_native = []
execution_times_numpy = []

total_start_time = time.perf_counter()

for size in sizes:
    numbers = np.random.randint(-10, 10, size)

    ll = LinkedList()
    for number in numbers:
        ll.append(number)
    start_time = time.perf_counter()
    max_sum = sub_suma_max(ll.to_list())
    execution_time = time.perf_counter() - start_time
    execution_times_native.append(execution_time)

    npll = NumPyLinkedList()
    for number in numbers:
        npll.append(number)
    start_time = time.perf_counter()
    max_sum = sub_suma_max(npll.to_list())
    execution_time = time.perf_counter() - start_time
    execution_times_numpy.append(execution_time)

total_execution_time = time.perf_counter() - total_start_time

print(f"El tiempo total de ejecución del programa fue de: {total_execution_time} segundos.")

plt.figure(figsize=(10, 6))
plt.plot(sizes, execution_times_native, color='blue', label='Listas ligadas nativas')
plt.plot(sizes, execution_times_numpy, color='red', label='Listas ligadas con NumPy')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Segundos')
plt.title('Tiempo de ejecución de la función sub_suma_max')
plt.legend()
plt.show()