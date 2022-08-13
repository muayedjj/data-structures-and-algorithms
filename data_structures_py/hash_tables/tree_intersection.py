from data_structures_py.trees.trees import BinaryTree, TNode
from data_structures_py.hash_tables.hash_table import HashTable


def tree_intersection(bt1, bt2):
    intersections = []
    bt1n = bt1.pre_order()
    bt2n = bt2.pre_order()
    if bt1n is None or bt2n is None or len(bt1n) == 0 or len(bt2n) == 0:
        return 'No Intersections!\nHow could an empty tree have intersections with anything!?'

    hbt1 = HashTable(len(bt1n))

    for n in bt1n:
        hbt1.set(n, str(n))

    for n in bt2n:
        if hbt1.contains(n):
            intersections.append(n)

    return intersections


if __name__ == "__main__":

    bt1 = BinaryTree()
    bt1.root = TNode('A')
    bt1.root.left = TNode('B')
    bt1.root.right = TNode('C')
    bt1.root.left.left = TNode('D')
    bt1.root.left.right = TNode('E')
    bt1.root.right.left = TNode('4')
    bt1.root.right.right = TNode(1)

    bt2 = BinaryTree()
    bt2.root = TNode('1')
    bt2.root.left = TNode('B')
    bt2.root.right = TNode('c')
    bt2.root.left.left = TNode('4')
    bt2.root.left.right = TNode('E')
    bt2.root.right.left = TNode('F')
    bt2.root.right.right = TNode('G')

    bt3 = BinaryTree()

    print(tree_intersection(bt1, bt2))

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


