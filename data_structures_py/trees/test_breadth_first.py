import pytest
from data_structures_py.trees.breadth_first import breadth_first
from data_structures_py.trees.trees import BinaryTree, TNode


def test_breadth_first():
    tree = BinaryTree()
    tree.root = TNode('A')
    tree.root.left = TNode('B')
    tree.root.right = TNode('C')
    tree.root.left.left = TNode('D')
    tree.root.left.right = TNode('E')
    tree.root.right.left = TNode('F')
    tree.root.right.right = TNode('G')
    tree.root.right.right.right = TNode('H')
    tree.root.right.right.right.right = TNode('I')

    actual = breadth_first(tree)
    expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    assert actual == expected


def test_breadth_first_again():
        tree = BinaryTree()
        tree.root = TNode(5)
        tree.root.left = TNode(4)
        tree.root.right = TNode(3)
        tree.root.left.left = TNode(2)
        tree.root.left.right = TNode(1)
        tree.root.right.left = TNode(0)

        actual = breadth_first(tree)
        expected = [5, 4, 3, 2, 1, 0]
        assert actual == expected
