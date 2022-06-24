from abc import ABC


class Node(ABC):
    """
    Node creator
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @classmethod
    def doubly_linked_attributes_constructor(cls, previous):
        """
        To code later, still thinking...
        :param previous:
        :return:
        """
        pass


class LinkedList:
    """
    Linked List Initiator, Node Navigator and Modifier, and then some more
    """

    def __init__(self, head=None):
        self.head = head

    def includes(self, value):
        """
        Node finder
        This method looks for a value within a linked list (in the Node Values)
        and returns True if it exists of False if it does not.
        Args:
            1. value to find
        Output:
            2. Boolean value indicating the existence of the input value in the Linked List or the Lack of it.
        """

        current = self.head
        while current is not None:
            if value == current.value:
                return True
            current = current.next
        return False

    def get(self, index):
        if index > self.length():
            print('Out of range')
            return None
        else:
            current_index = 0
            current = self.head
            while current_index != index:
                current = current.next
                current_index += 1
            return current.value

    def insert(self, value):
        """
         Node pusher
         This method takes a value for a new node to be inserted at the beginning of the Linked List (new head)
         Args:
             1. value
        """

        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def length(self):
        """
         Linked List Length Calculator
         This method counts the Nodes of the Linked List and returns its Length
         Args: None
         Output:
            1. The length of the Linked List as an integer.
        """

        current = self.head
        length = 1
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def __str__(self):
        """
         List Displayer (For Built-in Print())
         This method iterates through the nodes of the Linked List and returns it as a string of nones.
         Args: None
         output:
            1. The Linked List as astring of Node Values in the form of
               "{ a } -> { b } -> { c } -> NULL"
        """

        current = self.head
        string = ""
        while current is not None:
            string += "{ " + f"{current.value}" + " }" + " -> "
            current = current.next
        return string + "NULL"

    def __repr__(self):
        """
         List Displayer (For Interpreter)
         This method iterates through the nodes of the Linked List and returns it as a string of nones.
         Args: None
         output:
            1. The Linked List as a string of Node Values in the form of
               "{ a } -> { b } -> { c } -> NULL"
        """

        current = self.head
        string = ""
        while current is not None:
            string += "{ " + f"{current.value}" + " }" + " -> "
            current = current.next
        return repr(string) + "NULL"

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


#
# def if_palindrome(lin_lst):
#     """
#     A work in progress
#     Should take a linked list and output a boolean value indicating whether it resembles a palindrome or not
#     """
#     val = []
#
#     curr = lin_lst.head
#     nxt = lin_lst.head.next
#
#     if lin_lst.head.value is None and nxt is None:
#         raise Exception('Error! List is Empty')
#
#     if lin_lst.head.value is not None and nxt is None:
#         return True
#
#     while nxt is not None:
#         current = current.next
#
#     if val == val[::-1]:
#         return True
#

if __name__ == "__main__":
    list_one = LinkedList()
    list_one.append('A')
    list_one.append('B')
    list_one.append('C')
    list_one.append('D')
    list_one.append('E')
    #
    # print(list_one.get(0))
    # print(list_one.get(4))
    # print(list_one.length())
    # print(list_one.__str__())
    # print(list_one.includes(4))
    # print(list_one.includes('C'))
    #
    # print(str(list_one))
    # print(repr(list_one))

    print(if_palindrome(list_one))
