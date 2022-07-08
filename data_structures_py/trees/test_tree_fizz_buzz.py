# import pytest
from data_structures_py.trees.tree_fizz_buzz import KaryTree, KTNode, fizz_buzz_tree
# from data_structures_py.trees.trees import BinaryTree, TNode, Queue, Node


def test_fizzbuzz():
    k_tree = KaryTree()
    k_tree.root = KTNode(1)
    nodes = []

    for val in range(2, 30):
        nodes.append(KTNode(val))

    for node in nodes:
        k_tree.root.children.append(node)

    fizz_buzz_tree(k_tree)

    expected = ["FizzBuzz" if (i % 5 == 0 and i % 3 == 0) else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 30)]
    actual = k_tree.kary_tree_node_values()

    assert actual == expected
