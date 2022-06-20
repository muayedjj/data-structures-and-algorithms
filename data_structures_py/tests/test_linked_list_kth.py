from data_structures_py.linked_list.linkedlist import Node, LinkedList


def test_instantiate():
    actual = LinkedList().head
    expected = None
    assert actual == expected


def test_insert():
    link_list = LinkedList()
    link_list.insert(11)
    expected = 11
    actual = link_list.head.value
    assert actual == expected


def test_insert_multiple():
    nod_1 = "M"
    nod_2 = "J"
    nod_3 = "S"
    nod_4 = "MJJ"
    linked_list = LinkedList(nod_1)
    linked_list.insert(nod_2)
    linked_list.insert(nod_3)
    linked_list.insert(nod_4)
    actual = linked_list.head.value
    expected = "MJJ"
    assert actual == expected


def test_str():
    link_list = LinkedList()
    link_list.insert("c")
    link_list.insert("b")
    link_list.insert("a")
    actual = str(link_list)
    expected = "{ a } -> { b } -> { c } -> NULL"
    assert actual == expected
