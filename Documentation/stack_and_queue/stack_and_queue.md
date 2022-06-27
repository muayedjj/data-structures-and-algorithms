
## Python 3

# **Stacks & Queues: Linked List Variants**

## _[Code Challenge 10](https://canvas.instructure.com/courses/4839248/assignments/30188572)_

## **## Problem Domain:**

### **Node**
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

### **Stack**
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- This object should be aware of a default empty value assigned to top when the stack is created.
- The class should contain the following methods:
     - push
          - Arguments: value
          - Adds a new node with that value to the top of the stack with an O(1) Time performance.

     - pop
          - Arguments: none
          - Returns: the value from node from the top of the stack
          - Removes the node from the top of the stack
          - Should raise exception when called on empty stack

     - peek
          - Arguments: none
          - Returns: Value of the node located at the top of the stack
          - Should raise exception when called on empty stack

     - is empty
          - Arguments: none
          - Returns: Boolean indicating whether or not the stack is empty.

          - 
### **Queue**
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- This object should be aware of a default empty value assigned to front when the queue is created.
- The class should contain the following methods:
     - enqueue
          - Arguments: value
          - adds a new node with that value to the back of the queue with an O(1) Time performance.

     - dequeue
          - Arguments: none
          - Returns: the value from node from the front of the queue
          - Removes the node from the front of the queue
          - Should raise exception when called on empty queue

     - peek
          - Arguments: none
          - Returns: Value of the node located at the front of the queue
          - Should raise exception when called on empty stack

     - is empty
          - Arguments: none
          - Returns: Boolean indicating whether or not the queue is empty


## Whiteboard Process

_Not required for this challenge._

[//]: # (![whiteboard photo]&#40;./&#41;)


## Approach & Efficiency
- By design, stacks and queues do not require iterating through their contents to perform any of the base operations 
a single time, which makes things much simpler as we only need concern ourselves with:
    - The `top` of a **Stack**.
    - The `front` and `rear/back` of a **Queue**.

- A check to make sure a stack is not empty before trying to pop or peek into its top is necessary, and will raise an exception.

- A check to make sure a queue is not empty before trying to dequeue or peek into its front is necessary, and will raise an exception.

### Big oh for both classes: `class Stack & class Queue`
- _Performance/Time_ complexity **(Big O)** for both classes is **O(1) - Constant Time**, because unlike standard linked lists, iterating through the 
   nodes in not required to `pop` or `push` or perform any of the other operations coded in this challenge on either **stacks** or **queues**.

- _time_ requirements **(Big O)** is **O(N) - Linear Proportion between data and space** when `pushing` into **stacks** or `enqueuing` in **queues**,
   because just like standard linked lists, as more data is added, new `nodes` are created, and memory is used.
   on the other hand, all other operations don't use space at all.

[//]: # ( using a *`While`* Loop & *`If-elif-else`* statements)

[//]: # (Kepping it as simple as possible, the floor division &#40;`//`&#41; was used to determine where the middle
of the original/input list is, and compare the key with the item at that index.)

## **`The Code`**

### [**`Code`**](../../data_structures_py/linked_list/stack_and_queue.py)

### [**`Tests`**](../../data_structures_py/tests/test_stack_and_queue.py)


