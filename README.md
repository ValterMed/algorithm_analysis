# Homework
This repository is only for uploading homework.

# Greatest subset
## Description
This Python script is designed to identify the greatest non-negative subset from a randomly generated list of integers. It iterates through the list, extracting subsets of non-negative integers and comparing them to find the subset with the largest sum. In the end, it graphs the time of execution against the readings of the mainset.

## How it works
1. The script generates a list `mainset` containing 1000 random integers between -100 and 100.
2. It initializes several lists and variables to keep track of subsets and their sums.
3. It iterates through each element of `mainset`, adding non-negative integers to `lastsubset` while measuring the time it takes to do each iteration.
4. When encountering a negative integer, it checks if there's more than one negative integer in a row.
5. If the current `lastsubset` has a greater sum than the previously identified greatest subset, it updates `greatestsubset`.
6. Finally, it prints the `greatestsubset` and the sum of its elements in addition to the graphing of reads vs time.

## Usage
1. Ensure you have Python installed on your system as well as the library matplotlib.
2. Copy the provided code into a Python file (e.g., `greatest_subset.py`).
3. Run the script using a Python interpreter.
4. View the output to see the greatest non-negative subset and the sum of its elements.

## Example Output
~~~Python
[-54, -17, 57, -63, 22, 86, -15, 81, -97, 33, -33, 35, -92, -25, -12, 6, -20, -9, 58, -52, 57, -77, -81, -41, -93, -32, -87, -35, 28, -16, 33, 8, -69, -58, -31, -58, -26, -35, -51, 27, 72, 77, -5, -24, 29, -12, 14, -92, -80, -77, -12, -24, 22, -2, 58, 33, -48, -58, -20, 3, -2, 52, 44, -68, -95, 64, 12, 20, 80, -5, 68, -17, 28, 32, 59, 6, 37, -82, 66, 52, 56, -15, 14, -74, -36, -53, -3, 13, -41, 59, -49, 100, 66, -87, 92, -6, -99, -46, 23, -31]
[27, 72, 77]
176
~~~
![Screenshot 2024-04-04 082056](https://github.com/JoaquinMO17/Homework/assets/157546675/51b3e817-6418-4fea-a18f-e1c46cd34a49)
## Dependencies
- Python 3.x
- `random` module (built-in)
- `matplotlib` module

## Author
This script was written by Murguia Ortiz Joaquin de Jesus.

# Linked list vs Numpy array
## Description
The script consists of two main components:

1. Linked List Implementation:
The script defines a Node class for linked list nodes and a LinkedList class to handle linked list operations such as adding nodes at the front or end and printing the list.
2. Speed Comparison Function:
The script includes a function compare_speed(n) to compare the speed of writing data to a linked list and a NumPy array of length n.
Inside compare_speed(n), instances of linked list and NumPy array are created, data is written into them, and the time taken is measured.

## How it works
1. A linked list is implemented in the script.
2. The script then proceeds to write 10000 elements on each the linked list and a numpy array.
3. Finally, it compares the times of writing by graphing them side by side.

## Usage
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., `listvsnumpy.py`).
3. Run the script using a Python interpreter.
4. View the output.

## Example Output
![Screenshot 2024-04-04 085757](https://github.com/JoaquinMO17/Homework/assets/157546675/9d80b2e1-6f33-4dc2-b269-47e4e1067d34)

## Dependencies
- Python 3.x
- `Numpy` module
- `matplotlib` module

## Author
This script was written by Murguia Ortiz Joaquin de Jesus.

# Binary Tree Implementation in Python
## Description
This Python script provides an implementation of a binary tree data structure, along with methods to insert nodes, perform traversals, search for specific nodes, and print subtrees rooted at specific nodes.

##Features
BinaryTree Class: Represents the binary tree and includes methods for insertion, traversal, search, and printing subtrees.
TreeNode Class: Represents a node in the binary tree.
Insertion: Method to insert new nodes into the binary tree.
Inorder Traversal: Method to perform an inorder traversal of the binary tree.
Node Search: Method to search for a node with a specific value in the tree.
Print Subtree: Method to print the subtree rooted at a specific node.

## How it works
1. The `insert` method allows adding new nodes to the binary tree. When a node is inserted, it is placed in the appropriate position based on its value. If the value is less than the current node's value, it is inserted into the left subtree; if it's greater, it goes into the right subtree.
2. The `inorder_traversal` method performs an inorder traversal of the binary tree. In this traversal, nodes are visited in the order left subtree, current node, right subtree. This results in the values being printed in sorted order.
3. The `search_node` method allows searching for a node with a specific value in the binary tree. It performs a recursive search starting from the root node and traversing left or right based on the comparison of values until the target node is found.
4. The `print_subtree` method prints the subtree rooted at a specific node. It performs an inorder traversal starting from the given node, printing the values of the nodes in the subtree.

## Usage
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., `binarytree.py`).
3. Run the script using a Python interpreter or change the example values to make your own binarytree.
4. View the output.

## Example Output
![Screenshot 2024-04-04 183355](https://github.com/JoaquinMO17/Homework/assets/157546675/65ea753a-c9fd-409c-b769-4f86d678d601)

## Dependencies
- Python 3.x

## Author
This script was written by Murguia Ortiz Joaquin de Jesus.
