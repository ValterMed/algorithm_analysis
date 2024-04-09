import time
import random
import matplotlib.pyplot as plt

class NodoLista:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.inicio = None

    def agregar_elemento_lista(self, valor):
        inicio = time.time()
        nuevo_nodo = NodoLista(valor)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        fin = time.time()
        return fin - inicio

    def eliminar_elemento_lista(self, valor):
        inicio = time.time()
        actual = self.inicio
        anterior = None
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:
            if anterior is None:
                self.inicio = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
        fin = time.time()
        return fin - inicio

    def imprimir_elementos_lista(self):
        actual = self.inicio
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso:
lista_enlazada = ListaEnlazadaSimple()
tiempos_agregar_lista = []
tiempos_eliminar_lista = []

for i in range(100):
    tiempo_agregar_lista = lista_enlazada.agregar_elemento_lista(random.randint(0, 1000))
    tiempos_agregar_lista.append(tiempo_agregar_lista)

for i in range(100):
    tiempo_eliminar_lista = lista_enlazada.eliminar_elemento_lista(random.randint(0, 1000))
    tiempos_eliminar_lista.append(tiempo_eliminar_lista)

# Graficar los tiempos acumulados
print("Gráfico de tiempo de agregar y eliminar elementos en lista enlazada:")
plt.plot(range(100), [sum(tiempos_agregar_lista[:i]) for i in range(1, 101)], label='Agregar')
plt.plot(range(100), [sum(tiempos_eliminar_lista[:i]) for i in range(1, 101)], label='Eliminar')
plt.xlabel('Número de elementos')
plt.ylabel('Tiempo acumulado (segundos)')
plt.legend()
plt.show()
