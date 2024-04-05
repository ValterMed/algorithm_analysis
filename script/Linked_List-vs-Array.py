import time
import numpy as np
import matplotlib.pyplot as plt

# Classes that define the Linked list
class Node(object):
    def __init__(self, data):
        self.val = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
        
    # Method of the linked list that allows to insert elements
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
# Fuction that repeat the process of inserting an elment n times in a linked list
def insert_linked_list(size):
        linked_list = Linked_list()
        
        start_time = time.time()
        
        for i in range(size):
            linked_list.append(i)
        
        end_time = time.time()
        
        return end_time - start_time
        
# Function that defines the array
def array(size):
    start_time = time.time()
    
    array = np.zeros(size)
    for i in range(size):
        array[i] = i
    
    end_time = time.time()
    
    return end_time - start_time    


if __name__ == '__main__':
    
    sizes = [10**i for i in range(1, 6)]  # Sizes of arrays: [10, 100, 1000, 10000, 100000]
    numpy_times = []
    python_times = []

    for size in sizes:
        numpy_times.append(array(size))
        python_times.append(insert_linked_list(size))

    plt.plot(sizes, numpy_times, label='NumPy array')
    plt.plot(sizes, python_times, label='Linked list')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Comparison between Array and linked list Writing Time')
    plt.legend()
    plt.show()
