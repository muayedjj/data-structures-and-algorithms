class EmptyQueueException:
    def __init__(self, err: str):
        self.err = err
        print(self.err)
        raise EmptyQueueException


class TNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        if not self.root:
            return self.root
        output = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        if not self.root:
            return self.root

        output = []

        def _walk(root):
            output.append(root.value)

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        if not self.root:
            return self.root

        output = []

        def _walk(root):

            if root.left:
                _walk(root.left)

            output.append(root.value)

            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def pre_order_iter(self):
        if not self.root:
            return self.root

        stack = Stack()
        stack.push(self.root)

        output = []
        while not stack.is_empty():
            top = stack.pop()
            output.append(top.value)

            if top.right:
                stack.push(top.right)

            if top.left:
                stack.push(top.left)
        return output

    def post_order(self):
        if not self.root:
            return self.root

        output = []

        def _walk(root):

            if root.left:
                _walk(root.left)

            if root.right:
                _walk(root.right)
            output.append(root.value)

        _walk(self.root)
        return output

    def find_maximum_value(self):
        """
        This function is meant to be called on a binary tree to the find maximum value in that tree object
        Arguments: none
        Returns: number
        """

        if not self.root:
            self.root = TNode()
            return self.root

        temp = self.root

        def _walk(root):
            nonlocal temp

            if root.left:
                if root.left.value > temp.value:
                    temp.value = root.left.value
                _walk(root.left)

            if root.right:
                if root.right.value > temp.value:
                    temp.value = root.right.value
                _walk(root.right)

        _walk(self.root)

        return temp.value


class BinarySearchTree(BinaryTree):
    def add(self, value=None):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        """
        temp = TNode(value)
        curr = self.root

        if not self.root:
            self.root = TNode(value)
            return

        if self.root == TNode(value):
            return

        while curr is not None:

            if temp.value < curr.value:

                if curr.left is None:
                    curr.left = temp
                    break

                curr = curr.left

            else:

                if curr.right is None:
                    curr.right = temp
                    break

                curr = curr.right

    def contains(self, value=None):
        """
        Argument: value
        Returns: boolean indicating whether the value is in the tree or not at least once.
        """

        curr = self.root

        while curr:
            if value == curr.value:
                return True

            elif value < curr.value:
                curr = curr.left

            elif value > curr.value:
                curr = curr.right

        return False


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        It will insert a node to the queue
        """
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise Exception("Empty Queue, you can't dequeue from")
        else:
            temp_node = self.front
            self.front = self.front.next
            return temp_node.value

    def is_empty(self):
        return False if self.front else True


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Takes the vlaue and make a node and append it to the top of the stack
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def is_empty(self):
        return False if self.top else True

    def pop(self):
        if self.is_empty():
            raise Exception
        """
        a method to pop the top value of the stack
        input: no input
        output:
        the value popped from the stack
        """
        temp = self.top.value
        self.top = self.top.next
        return temp


if __name__ == "__main__":
    """
    tree = Tree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')
    print('pre_order_iter')

    print(tree.pre_order_iter())
    print('pre_order')

    print(tree.pre_order())
    print('post_order')
    print(tree.post_order())
    print('in_order')
    print(tree.in_order())
    # tree.pre_order()
    # print("+++++++++++++++++")
    # tree.pre_order_iter()
    # --------------------------------
    """

    """
    bst.root = TNode(10)
    bst.root.left = TNode(2)
    bst.root.right = TNode(60)
    bst.root.left.left = TNode(1)
    bst.root.left.right = TNode(3)
    # bst.root.right.left = TNode(12)
    bst.add(5)
    bst.add(7)
    bst.add(65)
    bst.add(59)
    """

    bst = BinaryTree()
    # bst.root = TNode(10)
    # bst.root.left = TNode(50)
    # bst.root.right = TNode(150)
    # bst.root.left.left = TNode(1)
    # bst.root.left.right = TNode(7)
    # bst.root.right.left = TNode(12)
    # bst.root.right.right = TNode(100)

    print(bst.find_maximum_value().__repr__())

    """
    tree = BinarySearchTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')
    print(tree.contains())
    """
