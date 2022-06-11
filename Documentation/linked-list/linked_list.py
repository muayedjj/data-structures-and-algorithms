class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        self.head = node

    def includes(self, value):
        current = self.head
        if current.value == value:
            return True
        else:
            return False

    def to_string(self):
        current = self.head
        string = ""
        while current is not None:
            string = string + f"{current.value} -> "
            current = current.next

        return string + "Null"
