import numpy as np
import time
import matplotlib.pyplot as plt

class ListaArrayNumpy:
    def __init__(self):
        """
        Constructor de la clase ListaArrayNumpy.
        Inicializa una lista vacía utilizando un array NumPy.
        """
        self.array = np.array([])

    def agregar_elemento(self, valor):
        """
        Agrega un nuevo elemento al final de la lista.

        Parámetros:
            - valor: El valor que se agregará a la lista.
        """
        inicio = time.time()
        self.array = np.append(self.array, valor)
        fin = time.time()
        return fin - inicio

    def eliminar_elemento(self, valor):
        """
        Elimina la primera ocurrencia del valor proporcionado en la lista.

        Parámetros:
            - valor: El valor del elemento que se desea eliminar.
        """
        inicio = time.time()
        try:
            indice = np.where(self.array == valor)[0][0]  # Encuentra el índice del primer valor
            self.array = np.delete(self.array, indice)  # Elimina el valor en ese índicr
        except IndexError:
            print(f"El valor {valor} no está en la lista.")
        fin = time.time()
        return fin - inicio

    def imprimir_lista(self):
        """
        Imprime todos los elementos de la lista.
        """
        print(self.array)


# Ejemplo de uso:
lista_numpy = ListaArrayNumpy()
tiempos_agregar = []
tiempos_eliminar = []

for i in range(1000):
    tiempo_agregar = lista_numpy.agregar_elemento(i)
    tiempos_agregar.append(tiempo_agregar)
    
for i in range(1000):
    tiempo_eliminar = lista_numpy.eliminar_elemento(i)
    tiempos_eliminar.append(tiempo_eliminar)

print("Gráfico de tiempo de agregar y eliminar elementos en Lista Array con NumPy:")
plt.plot(range(1000), tiempos_agregar, label='Agregar')
plt.plot(range(1000), tiempos_eliminar, label='Eliminar')
plt.xlabel('Número de elementos')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.show()
