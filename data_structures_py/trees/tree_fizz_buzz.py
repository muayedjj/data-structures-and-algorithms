from data_structures_py.trees.trees import BinaryTree, TNode, Queue, Node


class KTNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []


class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def kary_tree_node_values(self):
        nodes = []

        def walk(node):
            nodes.append(node.value)

            if node.children:
                for child in node.children:
                    walk(child)

        walk(self.root)

        return nodes


def fizz_buzz_tree(kary_tree):
    def traverse(node):
        if node.children:
            for child in node.children:
                node.value = str(node.value)
                if child.value % 3 == 0 and child.value % 5 == 0:
                    child.value = "FizzBuzz"
                elif child.value % 3 == 0:
                    child.value = "Fizz"
                elif child.value % 5 == 0:
                    child.value = "Buzz"
                else:
                    child.value = str(child.value)

    traverse(kary_tree.root)


if __name__ == "__main__":
    tree = KaryTree()
    expected = ["FizzBuzz" if (i % 5 == 0 and i % 3 == 0) else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 30)]
    print(expected)
    # tree.root = KTNode('A')
    # tree.root.left = KTNode('B')
    # tree.root.right = KTNode('C')
    # tree.root.left.left = KTNode('D')
    # tree.root.left.right = KTNode('E')
    # tree.root.right.left = KTNode('F')
    k_tree = KaryTree()
    k_tree.root = KTNode(1)
    nodes = []

    for val in range(2, 50):
        nodes.append(KTNode(val))

    for node in nodes:
        k_tree.root.children.append(node)
    fizz_buzz_tree(k_tree)
    actual = k_tree.kary_tree_node_values()

    print(actual)

