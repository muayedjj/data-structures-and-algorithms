## Python 3

# **Data Structures: Hash Tables**

## Code Challenge 29

## Problem Domain: Implementation Of A Hash Table

> **Create a hash table implementation that allows adding, getting values, checking if a given key exists, and
   actually hashing a key.**


1. **`set()`**
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.

2. **`get()`**
- Arguments: key
- Returns: Value associated with that key in the table

3. **`contains()`**
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.


4. **`keys()`**
- Returns: Collection of keys


5. **`hash()`**
- Arguments: key
- Returns: Index in the collection for that key

# 

## Approach & Efficiency

**All of the methods above exist in the Hashtable class. The hash table is instantiated with 1024 buckets that have
a default value of None. Collisions are handled with the linked list data structure. Efficiency:** 

### Big (O)

- **Performance** =>
    - For `hash()` method: **O(1)**
    - For `set()` method: **O(1)**.
    - For `get()` method: **O(N)**.
    - For `key()` method: **O(1)**.
    - For `contains()` method: **O(N)**.

- **Space** => 
    - For `hash()` method: **O(N)**
    - For `set()` method: **O(N)**.
    - For `get()` method: **O(1)**.
    - For `key()` method: **O(N)**.
    - For `contains()` method: **O(1)**.


[//]: # ( using a *`While`* Loop & *`If-elif-else`* statements)

[//]: # (Keeping it as simple as possible, the floor division &#40;`//`&#41; was used to determine where the middle
of the original/input list is, and compare the key with the item at that index.)

## **The Code**

### [**`Code`**](../../data_structures_py/hash_tables/hash_table.py)

### [**`Tests`**](../../data_structures_py/tests/test_hash_table.py)

