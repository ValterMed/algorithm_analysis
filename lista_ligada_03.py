import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
       
        self.value = value
        self.next = None  # Link to the next node


class LinkedList:
    def __init__(self):
        """
        Constructor for the LinkedList class.
        Initializes an empty linked list.
        """
        self.head = None  # Reference to the first node in the list

    def add_element(self, value):
        """
        Adds a new element to the end of the linked list.

        Parameters:
            - value: The value to be added to the list.
        """
        start = time.time()
        new_node = Node(value)  # Creates a new node with the provided value
        if self.head is None:  # If the list is empty, the new node becomes the head
            self.head = new_node
        else:
            # Traverse the list to find the last node
            current = self.head
            while current.next:
                current = current.next
            # Adds the new node to the end of the list
            current.next = new_node
        end = time.time()
        return end - start

    def remove_element(self, value):
        """
        Removes the first node containing the provided value from the linked list.

        Parameters:
            - value: The value of the node to be removed.
        """
        start = time.time()
        current = self.head  # Starts from the head of the list
        previous = None  # Stores the node before the current one
        # Finds the node with the specified value
        while current and current.value != value:
            previous = current
            current = current.next
        if current:  # If a node with the specified value is found
            if previous is None:  # If the node to be removed is the head
                self.head = current.next  # Updates the head of the list
            else:
                # Removes the current node by updating the link of the previous node
                previous.next = current.next
        end = time.time()
        return end - start

    def print_list(self):
        """
        Prints the values of all nodes in the linked list.
        """
        current = self.head  # Starts from the head of the list
        while current:
            print(current.value, end=" -> ")  # Prints the value of the node
            current = current.next  # Moves to the next node
        print("None")


# Example of usage:
linked_list = LinkedList()
add_times = []
remove_times = []

for i in range(1000):
    add_time = linked_list.add_element(i)
    add_times.append(add_time)
    
for i in range(1000):
    remove_time = linked_list.remove_element(i)
    remove_times.append(remove_time)


#show all
print("Graph of time to add and remove elements in Linked List:")
plt.plot(range(1000), add_times, label='Add')
plt.plot(range(1000), remove_times, label='Remove')
plt.xlabel('Number of elements')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
