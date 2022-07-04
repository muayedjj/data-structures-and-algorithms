import pytest
from data_structures_py.trees.trees import BinarySearchTree, TNode, BinaryTree


def test_instantiate():
    bst = BinarySearchTree()
    actual = bst.root
    expected = None
    assert actual == expected


def test_ins_single():
    bst = BinaryTree(20)
    # bs = BinarySearchTree(bst)
    assert bst.root == 20


def test_left_right():
    t = BinaryTree(2)
    bst = BinarySearchTree(t)

    bst.root.left = 1
    bst.root.right = 3

    assert bst.root.left == 1 and bst.root.right == 3


def test_pre_order():
    tree = BinaryTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')

    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert actual == expected


def test_in_order():
    tree = BinaryTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')

    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'F', 'C', 'G']
    assert actual == expected


def test_post_order():
    tree = BinaryTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')

    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'F', 'G', 'C', 'A']
    assert actual == expected


def test_contains_negative():
    tree = BinarySearchTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')

    actual = tree.contains('K')
    expected = False
    assert actual == expected


def test_contains_affirmative():
    tree = BinarySearchTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')

    actual = tree.contains('G')
    expected = True
    assert actual == expected


def test_add_multiple():
    bst = BinarySearchTree()
    bst.root = TNode(10)
    bst.root.left = TNode(5)
    bst.root.right = TNode(15)
    bst.root.left.left = TNode(1)
    bst.root.left.right = TNode(7)
    bst.root.right.left = TNode(12)
    bst.add(20)
    bst.add(19)
    bst.add(11)

    actual = bst.contains(0)
    expected = False
    assert actual == expected


def test_add_multiple_further():
    bst = BinarySearchTree()
    bst.root = TNode(10)
    bst.root.left = TNode(5)
    bst.root.right = TNode(15)
    bst.root.left.left = TNode(1)
    bst.root.left.right = TNode(7)
    bst.root.right.left = TNode(12)
    bst.add(21)
    bst.add(19)
    bst.add(11)

    actual = bst.contains(19) and bst.contains(7)
    expected = True
    assert actual == expected


def test_find_maximum_value():
    bt = BinaryTree()
    bt.root = TNode(10)
    bt.root.left = TNode(50)
    bt.root.right = TNode(150)
    bt.root.left.left = TNode(1)
    bt.root.left.right = TNode(7)
    bt.root.right.left = TNode(12)
    bt.root.right.right = TNode(100)

    actual = bt.find_maximum_value()
    expected = 150
    assert actual == expected

