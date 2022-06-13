class Node:
    """
    Node creator
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linked_List:
    """
    Node Navigator and Modifier
    """
    def __init__(self, head=None):
        self.head = head

    def includes(self, value):
        current = self.head
        while current is not None:
            if value == current.value:
                return True
            current = current.next
        return False

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def __str__(self):
        current = self.head
        string = ""
        while current is not None:
            string += "{ " + f"{current.value}" + " }" + " -> "
            current = current.next
        return string + "NULL"
