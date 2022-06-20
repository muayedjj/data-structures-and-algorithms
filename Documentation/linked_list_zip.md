## Python 3

# **linked_list_zip**

## Code Challenge 08

A function called `linked_list_zip` which takes in two linked lists and merges them together in alternating fashion.
    - Arguments:
        1. lin_lst_1 (A singly-linked Linked List).
        2. lin_lst_2 (A singly-linked Linked List).
    - Output:
        1. A mutated version of one of the input linked lists in the form of
           a new linked list made up of the alternating node values from both of the two input arguments.

## Whiteboard Process

![whiteboard photo](--------)

## Approach & Efficiency

The Linked lists are looped through while:

1. Pointing the next pointer of one element/Node to the value of the corresponding Node in the other list.
2. Doing the reverse by pointing the next pointer of the previous Node in the second list to the next Node in the first list. 

- ignoring the second list if the head.next poiner equals None.
- ignoring the first list if the head.next poiner equals None.

- Big O for space is **O(1)**, because no new lists are created, and the variables used are constand in number
  regardless of the number of nodes in either list.
- Bog O for time for this approach is **O(N)**, because an increasing (linearly) amount of time is needed the more nodes
  the inputs have.


[//]: # ( using a *`While`* Loop & *`If-elif-else`* statements)

[//]: # (Kepping it as simple as possible, the floor division &#40;`//`&#41; was used to determine where the middle of the original/input list is, and compare the key with the item at that index.)

## **`The Code`**
### [**`Code`**](https://github.com/muayedjj/data-structures-and-algorithms/blob/7c57a74c25242890409bb5b573e4da3963773ade/data_structures_py/linked_list/linked_list_zip.py)

### [**`Tests`**](https://github.com/muayedjj/data-structures-and-algorithms/blob/7c57a74c25242890409bb5b573e4da3963773ade/data_structures_py/tests/test_linked_list_zip.py)
