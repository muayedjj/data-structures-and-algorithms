import pytest

from data_structures_py.trees.trees import BinaryTree, TNode
from data_structures_py.hash_tables.hash_table import HashTable
from data_structures_py.hash_tables.tree_intersection import tree_intersection


def test_empty(empty_tree, tree_one):
    actual = tree_intersection(empty_tree, tree_one)
    expected = 'No Intersections!\nHow could an empty tree have intersections with anything!?'
    assert actual == expected


def test_int_exist(tree_one, tree_two):
    actual = tree_intersection(tree_one, tree_two)
    expected = ['B', '4', 'E', 'G']
    assert actual == expected


def test_int_do_not_exist(tree_one, tree_three):
    actual = tree_intersection(tree_one, tree_three)
    expected = []
    assert actual == expected


@pytest.fixture
def tree_one():
    tree_one = BinaryTree()
    tree_one.root = TNode('A')
    tree_one.root.left = TNode('B')
    tree_one.root.right = TNode('C')
    tree_one.root.left.left = TNode('D')
    tree_one.root.left.right = TNode('E')
    tree_one.root.right.left = TNode('4')
    tree_one.root.right.right = TNode('G')
    return tree_one


@pytest.fixture
def tree_two():
    tree_two = BinaryTree()
    tree_two.root = TNode('1')
    tree_two.root.left = TNode('B')
    tree_two.root.right = TNode('c')
    tree_two.root.left.left = TNode('4')
    tree_two.root.left.right = TNode('E')
    tree_two.root.right.left = TNode('F')
    tree_two.root.right.right = TNode('G')
    return tree_two


@pytest.fixture
def tree_three():
    tree_three = BinaryTree()
    tree_three.root = TNode(1)
    tree_three.root.left = TNode(2)
    tree_three.root.right = TNode(3)
    tree_three.root.left.left = TNode(4)
    tree_three.root.left.right = TNode(5)
    return tree_three


@pytest.fixture
def empty_tree():
    empty_tree = BinaryTree()
    return empty_tree
