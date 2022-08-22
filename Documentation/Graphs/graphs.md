
# **Data Structures: Hash Tables**

## Python 3

## Code Challenge 34 - 35

## **Problem Domain: Graphs**

## Code Challenge 34: Implementing a graph class

> **Implement your own Graph. The graph should be represented as an adjacency list,\
and should include the following methods:**

- add node 
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
  
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
  
- get nodes
  - Arguments: none
  - Returns all the nodes in the graph as a collection (set, list, or similar)
  
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
  
- size
  - Arguments: none
  - Returns the total number of nodes in the graph


## Code Challenge 34: Extending implementation

### Write the following method for the Graph class:

- **`breadth_first()`**
  - Arguments: Node
  - Return: A collection of nodes in the order they were visited.
  - Display the collection
  - Structure and Testing

## **Whiteboard Process**

## **Approach & Efficiency**

### Big (O)

- **Performance** =>
    - For `add_node()` method: **O(1)**
    - For `get_nodes()` method: **O(N)**.
    - For `add_edge()` method: **O(1)**.
    - For `get_neighbors()` method: **O(N)**.
    - For `size()` method: **O(1)**.
    - For `breadth_first()` method: **O(N)**, _worst case_, only if the graph is **connected**.

[//]: # (    - For `breadth_first&#40;&#41;` method: **O&#40;N<sup>2</sup>&#41;**.)

- **Space** => 
    - For `add_node()` method: **O(N)**
    - For `get_nodes()` method: **O(N)**.
    - For `add_edge()` method: **O(N)**.
    - For `get_neighbors()` method: **O(N)**.
    - For `size()` method: **O(1)**.
    - For `breadth_first()` method: **O(N)**; as the space occupied by the output corresponds to the number of vertices.



[//]: # (    - For `breadth_first&#40;&#41;` method: **O&#40;N&#41;**.)


[//]: # ( using a *`While`* Loop & *`If-elif-else`* statements)

[//]: # (Keeping it as simple as possible, the floor division &#40;`//`&#41; was used to determine where the middle
of the original/input list is, and compare the key with the item at that index.)

## **The Code**

### [**`Code`**](../../data_structures_py/graphs/graphs.py)

### [**`Tests`**](../../data_structures_py/tests/test_graphs.py)
