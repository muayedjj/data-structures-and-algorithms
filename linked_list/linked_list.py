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
        """
         Node finder
        """

        current = self.head
        while current is not None:
            if value == current.value:
                return True
            current = current.next
        return False

    def insert(self, value):
        """
         Node pusher
        """

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

    def append(self, value):
        """
         Node adder
        """

        node = Node(value)
        current = self.head
        if self.head is None:
            self.head = node
            return
        while current.next is not None:
            current = current.next
        current.next = node

    def insert_before(self, value, new_value):
        """
         Node inserter
        """

        current = self.head
        if current.value == value:
            self.insert(new_value)
            return
        while current is not None:
            if current.next.value == value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next
        raise Exception(f"{{value}} Node non-existent, sorry")

    def insert_after(self, value, new_value):
        """
         Node inserter
        """

        current = self.head
        while current is not None:
            if current.value is value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next

        raise Exception(f"{{value}} Node non-existent, sorry")
