## Python 3

# **Data Structures: Trees**

## Code Challenge 15-16

## Problem Domain: Implementation of Trees

### Code challenge 15: **`add()`** & **`contains()`**

1. **Node**
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Binary Tree
Create a Binary Tree class
Define a method for each of the depth first traversals:
- pre-order
- in order
- post order which returns an array of the values, ordered appropriately.

2. **Binary Search Tree**
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
- Add
   - Arguments: value
   - Return: nothing
   Adds a new node with that value in the correct location in the binary search tree. 

- Contains
  - Argument: value
  Returns: boolean indicating whether the value is in the tree at least once.
  Structure and Testing
  Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

Any exceptions or errors that come from your code should be contextual, descriptive, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom error that describes what went wrong in calling the methods you wrote for this lab.

Write tests to prove the following functionality:

Can successfully instantiate an empty tree
Can successfully instantiate a tree with a single root node
For a Binary Search Tree, can successfully add a left child and right child properly to a node
Can successfully return a collection from a preorder traversal
Can successfully return a collection from an inorder traversal
Can successfully return a collection from a postorder traversal
Returns true or false for the contains method, given an existing or non-existing node value

### Code challenge 16: **`find_maximum_value()`**

Define a function, `find_maximum_value()` that is meant to be called on a binary tree to the find maximum
value in that tree object.
- Arguments: none
- Returns: number

#

## Whiteboard Process

### Code challenge 15: **`add()`** & **`contains()`**

![find_max_method](./find_max_value.png)

# 

## Approach & Efficiency

### Code challenge 15: **`add()`** & **`contains()`**

_Keeping it simple, multiple classes and methods are implemented in order to handle different tasks._
Create a `Node` class that has properties for the value stored in the node, the left child node, and the right child node
Create a Binary `Tree` class
Define a method for each of the depth first traversals called `pre_order`, `in_order`, and `post_order`
which returns an **array** of the values, ordered appropriately.
Create a `BinarySearchTree` class
Define a method named `add` that accepts a value, and adds a new node with that value in the correct 
location in the binary search tree.
Define a method named `contains` that accepts a value, and returns a boolean indicating 
whether the value is in the tree at least once.

### Code challenge 16: **`find_maximum_value()`**

Define `find_maximum_value()` method to _methodically_ traverse through the nodes of the tree comparing values
with that of the root, and assigning any that are greater to a temporary object until all the nodes are 
checked, finally returning the last value assigned the temporary placeholder.


### Big (O)

- **Performance** =>
    - For `add()` method: **O(N)** for _node insertion_. (log N for most cases, but O(N) for the worst case scenario)
    - For `contains()` method: **O(N)**.
    - For `find_maximum_value()` method: **O(N)**.
  

- **Space** => 
    - For `add()` method: **O(N)** for _node insertion_.
    - For `contains()` method: **O(1)** for _searching_ for a specific node. (The only space needed is for method objects)
    - For `find_maximum_value()` method: **O(1)** for _searching_ for a specific node. (The only space needed is for method objects)


[//]: # ( using a *`While`* Loop & *`If-elif-else`* statements)

[//]: # (Keeping it as simple as possible, the floor division &#40;`//`&#41; was used to determine where the middle
of the original/input list is, and compare the key with the item at that index.)

## **The Code**

### [**`Code`**](../../data_structures_py/trees/trees.py)

### [**`Tests`**](../../data_structures_py/trees/test_trees.py)

