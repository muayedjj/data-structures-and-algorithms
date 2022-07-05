from data_structures_py.trees.trees import BinaryTree, TNode, Queue, Node


def breadth_first(bt):
    """
    Write a function called breadth first
        - Arguments: tree
        - Return: list of all values in the tree, in the order they were encountered
    """

    if not bt.root:
        return bt.root
    output = []
    queue = Queue()
    queue.enqueue(bt.root)
    while not queue.is_empty():
        front = queue.dequeue()
        output.append(front.value)

        if front.left:
            queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

    return output


if __name__ == "__main__":

    # tree = BinaryTree()
    # tree.root = TNode('A')
    # tree.root.left = TNode('B')
    # tree.root.right = TNode('C')
    # tree.root.left.left = TNode('D')
    # tree.root.left.right = TNode('E')
    # tree.root.right.left = TNode('F')
    # tree.root.right.right = TNode('G')
    # tree.root.right.right.right = TNode('H')
    # tree.root.right.right.right.right = TNode('I')
    # tree.root.right.right.right.right.right = TNode('J')
    tree = BinaryTree()
    tree.root = TNode(5)
    tree.root.left = TNode(4)
    tree.root.right = TNode(3)
    tree.root.left.left = TNode(2)
    tree.root.left.right = TNode(1)
    tree.root.right.left = TNode(0)

    print('pre_order_iter')

    print(breadth_first(tree))


"""
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
#
# bst = BinaryTree()
# # bst.root = TNode(10)
# # bst.root.left = TNode(50)
# # bst.root.right = TNode(150)
# # bst.root.left.left = TNode(1)
# # bst.root.left.right = TNode(7)
# # bst.root.right.left = TNode(12)
# # bst.root.right.right = TNode(100)
#
# print(bst.find_maximum_value().__repr__())

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
