import time
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        """
        Constructor de la clase Nodo.
        
        Parámetros:
            - valor: El valor que contendrá el nodo.
        """
        self.valor = valor
        self.siguiente = None  # El enlace al siguiente nodo


class ListaEnlazada:
    def __init__(self):
        """
        Constructor de la clase ListaEnlazada.
        Inicializa una lista enlazada vacía.
        """
        self.cabeza = None  # La referencia al primer nodo de la lista

    def agregar_elemento(self, valor):
        """
        Agrega un nuevo elemento al final de la lista enlazada.

        Parámetros:
            - valor: El valor que se agregará a la lista.
        """
        inicio = time.time()
        nuevo_nodo = Nodo(valor)  # Crea un nuevo nodo con el valor proporcionado
        if self.cabeza is None:  # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        else:
            # Recorre la lista hasta encontrar el último nodo
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            # Agrega el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo
        fin = time.time()
        return fin - inicio

    def eliminar_elemento(self, valor):
        """
        Elimina el primer nodo que contenga el valor proporcionado de la lista enlazada.

        Parámetros:
            - valor: El valor del nodo que se desea eliminar.
        """
        inicio = time.time()
        actual = self.cabeza  # Inicia desde la cabeza de la lista
        anterior = None  # Almacena el nodo anterior al actual
        # Busca el nodo con el valor especificado
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:  # Si se encontró un nodo con el valor especificado
            if anterior is None:  # Si el nodo a eliminar es la cabeza
                self.cabeza = actual.siguiente  # Actualiza la cabeza de la lista
            else:
                # Elimina el nodo actual actualizando el enlace del nodo anterior
                anterior.siguiente = actual.siguiente
        fin = time.time()
        return fin - inicio

    def imprimir_lista(self):
        """
        Imprime los valores de todos los nodos en la lista enlazada.
        """
        actual = self.cabeza  # Inicia desde la cabeza de la lista
        while actual:
            print(actual.valor, end=" -> ")  # Imprime el valor del nodo
            actual = actual.siguiente  # Avanza al siguiente nodo
        print("None")


# Ejemplo de uso:
lista = ListaEnlazada()
tiempos_agregar = []
tiempos_eliminar = []

for i in range(1000):
    tiempo_agregar = lista.agregar_elemento(i)
    tiempos_agregar.append(tiempo_agregar)
    
for i in range(1000):
    tiempo_eliminar = lista.eliminar_elemento(i)
    tiempos_eliminar.append(tiempo_eliminar)

print("Gráfico de tiempo de agregar y eliminar elementos en Lista Enlazada:")
plt.plot(range(1000), tiempos_agregar, label='Agregar')
plt.plot(range(1000), tiempos_eliminar, label='Eliminar')
plt.xlabel('Número de elementos')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.show()





