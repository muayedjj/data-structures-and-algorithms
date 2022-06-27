class Node:
    """
    Node creator
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Stack creator
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        if self.is_empty():
            self.top = Node(value)
        else:
            new_top = Node(value)
            new_top.next = self.top
            self.top = new_top

    def pop(self):
        if self.is_empty():
            raise Exception('Error!')
        val = self.top.value
        self.top = self.top.next
        return val

    def peek(self):
        if self.is_empty():
            raise Exception('Error!')
        else:
            return self.top.value

    def is_empty(self):
        return self.top is None


class Queue:
    """
    Queue creator
    """
    node = Node()

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, value):
        if self.is_empty():
            self.front = Node(value)
        else:
            self.back = Node(value)
            self.front.next = self.back

    def dequeue(self):
        if self.is_empty():
            raise Exception('Error!')
        val = self.front.value
        self.front = self.front.next
        return val

    def peek(self):
        if self.is_empty():
            raise Exception('Error!')
        return self.front.value

    def is_empty(self):
        return self.front is None
