import time
import matplotlib.pyplot as plt

class NodoLista:
    def __init__(self, valor):
        """
        Constructor de la clase NodoLista.
        
        Parámetros:
            - valor: El valor que contendrá el nodo.
        """
        self.valor = valor
        self.siguiente = None  #enlace al siguiente nodo


class ListaEnlazadaSimple:
    def __init__(self):
        """
        Constructor de la clase ListaEnlazadaSimple.
        Inicializa una lista enlazada vacía.
        """
        self.inicio = None  #referencia al primer nodo de la lista

    def agregar_elemento_lista(self, valor):
        """
        Agrega un nuevo elemento al final de la lista enlazada.

        Parámetros:
            - valor: El valor que se agregará a la lista.
        """
        inicio = time.time()
        nuevo_nodo = NodoLista(valor)  #nuevo nodo con el valor proporcionado
        if self.inicio is None:  #si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.inicio = nuevo_nodo
        else:
            #recorre la lista hasta encontrar el último nodo
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            #agrega el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo
        fin = time.time()
        return fin - inicio

    def eliminar_elemento_lista(self, valor):
        """
        Elimina el primer nodo que contenga el valor proporcionado de la lista enlazada.

        Parámetros:
            - valor: El valor del nodo que se desea eliminar.
        """
        inicio = time.time()
        actual = self.inicio  #inicia desde la cabeza de la lista
        anterior = None  #almacena el nodo anterior al actual
        #busca el nodo con el valor especificado
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:  #si se encontró un nodo con el valor especificado
            if anterior is None:  #si el nodo a eliminar es la cabeza
                self.inicio = actual.siguiente  #actualiza la cabeza de la lista
            else:
                #elimina el nodo actual actualizando el enlace del nodo anterior
                anterior.siguiente = actual.siguiente
        fin = time.time()
        return fin - inicio

    def imprimir_elementos_lista(self):
        """
        Imprime los valores de todos los nodos en la lista enlazada.
        """
        actual = self.inicio  
        while actual:
            print(actual.valor, end=" -> ") 
            actual = actual.siguiente  
        print("None")


#ejemplo de uso:
lista_enlazada = ListaEnlazadaSimple()
tiempos_agregar_lista = []
tiempos_eliminar_lista = []

for i in range(1000):
    tiempo_agregar_lista = lista_enlazada.agregar_elemento_lista(i)
    tiempos_agregar_lista.append(tiempo_agregar_lista)
    
for i in range(1000):
    tiempo_eliminar_lista = lista_enlazada.eliminar_elemento_lista(i)
    tiempos_eliminar_lista.append(tiempo_eliminar_lista)

print("Gráfico de tiempo de agregar y eliminar elementos en lista enlazada:")
plt.plot(range(1000), tiempos_agregar_lista, label='Agregar')
plt.plot(range(1000), tiempos_eliminar_lista, label='Eliminar')
plt.xlabel('Número de elementos')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.show()
