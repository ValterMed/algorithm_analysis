import numpy as np
import time
import matplotlib.pyplot as plt

class ListaVector:
    def __init__(self):
        """
        Constructor de la clase ListaVector.
        Inicializa una lista vacía utilizando un vector NumPy.
        """
        self.vector = np.array([])

    def agregar_elemento_vector(self, valor):
        """
        Agrega un nuevo elemento al final del vector.

        Parámetros:
            - valor: El valor que se agregará al vector.
        """
        inicio = time.time()
        self.vector = np.append(self.vector, valor)
        fin = time.time()
        return fin - inicio

    def eliminar_elemento_vector(self, valor):
        """
        Elimina la primera ocurrencia del valor proporcionado en el vector.

        Parámetros:
            - valor: El valor del elemento que se desea eliminar.
        """
        inicio = time.time()
        try:
            indice = np.where(self.vector == valor)[0][0] 
            self.vector = np.delete(self.vector, indice)  
        except IndexError:
            print(f"El valor {valor} no está en el vector.")
        fin = time.time()
        return fin - inicio

    def imprimir_vector(self):
        """
        Imprime todos los elementos del vector.
        """
        print(self.vector)


#ejemplo de uso:
lista_vector = ListaVector()
tiempos_agregar_vector = []
tiempos_eliminar_vector = []

for i in range(1000):
    tiempo_agregar_vector = lista_vector.agregar_elemento_vector(i)
    tiempos_agregar_vector.append(tiempo_agregar_vector)
    
for i in range(1000):
    tiempo_eliminar_vector = lista_vector.eliminar_elemento_vector(i)
    tiempos_eliminar_vector.append(tiempo_eliminar_vector)

print("Gráfico de tiempo de agregar y eliminar elementos en Lista Vector con NumPy:")
plt.plot(range(1000), tiempos_agregar_vector, label='Agregar')
plt.plot(range(1000), tiempos_eliminar_vector, label='Eliminar')
plt.xlabel('Número de elementos')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.show()
