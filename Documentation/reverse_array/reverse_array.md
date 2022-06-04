# Reverse an Array

A function **reverseArray**, which takes an array as an argument. Without utilizing any of the built-in methods available to your language, it returns an array with elements in reversed order.

## Whiteboard Process

![whiteboard photo](./full%20visual.png)

## Approach & Efficiency

Big O for both space and time for this approach is **O(N)**, meaning that they both are directly/linearly proportional to the number of inputs.

## using *`indexing`*

Using the basic indexing method, the list is read backwards and then returned in that state.

***Notes:***

- reverse indexing is performed using no arguments for both start or end, and using the reverse step (-1) in the following syntax form:

   `list_name[start : end  : step]`

- This can be observed in the following code section.

### `The Code`

      def reverseArray(lst):
         return lst[::-1]

      print(reverseArray([-3,-2,-1,1,2,3,]))
