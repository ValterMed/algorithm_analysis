import numpy as np
import time
import matplotlib.pyplot as plt

class ArrayLinkedList:
    def __init__(self):
       
        self.array_list = np.array([])

    def add_item(self, value):
        """
        Adds a new item to the end of the list.

        Parameters:
            - value: The value to be added to the list.
        """
        start = time.time()
        self.array_list = np.append(self.array_list, value)
        end = time.time()
        return end - start

    def remove_item(self, value):
       
        start = time.time()
        try:
            index = np.where(self.array_list == value)[0][0]  # Finds the index of the first occurrence
            self.array_list = np.delete(self.array_list, index)  # Removes the value at that index
        except IndexError:
            print(f"The value {value} is not in the list.")
        end = time.time()
        return end - start

    def print_list(self):
        """
        Prints all elements of the list.
        """
        print(self.array_list)


# Example of usage:
array_linked_list = ArrayLinkedList()
add_times = []
remove_times = []

for i in range(1000):
    add_time = array_linked_list.add_item(i)
    add_times.append(add_time)
    
for i in range(1000):
    remove_time = array_linked_list.remove_item(i)
    remove_times.append(remove_time)


print("Graph of time to add and remove items in Array Linked List with NumPy:")
plt.plot(range(1000), add_times, label='Add')
plt.plot(range(1000), remove_times, label='Remove')
plt.xlabel('Number of items')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
