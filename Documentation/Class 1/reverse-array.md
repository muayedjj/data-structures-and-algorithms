# Reverse an Array
A function which takes an array as an argument. Without utilizing any of the built-in methods available to your language, it returns an array with elements in reversed order.

## Whiteboard Process
![whiteboard photo](./whiteboard.jpg)
## Approach & Efficiency
Big O for both space and time for this approach is **O(N)**, meaning that they both are direvtly/ linearly proportional to the number of inputs.

## using a *for* loop:
def reverse_array(list):
   list2 = []
   for i in range(len(list),-1,-1,-1)
   listt2.append(list[i])
return list2
print(list2)