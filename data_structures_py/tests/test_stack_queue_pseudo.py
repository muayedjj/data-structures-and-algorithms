import pytest
from data_structures_py.linked_list.stack_queue_pseudo import PseudoQueue


# PseudoQueue class tests
def test_enqueue():
    new_queue = PseudoQueue()
    new_queue.enqueue("A")
    actual = str(new_queue.dequeue())
    expected = "A"
    assert actual == expected


def test_dequeue_value():
    queue = PseudoQueue()
    queue.enqueue("A")
    actual = queue.dequeue()
    expected = "A"
    assert actual == expected


def test_enqueue_multi():
    queue = PseudoQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    actual = queue.dequeue()
    expected = "A"
    assert actual == expected


def test_dequeue_values():
    queue = PseudoQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    actual = queue.dequeue()
    expected = 'A'
    assert actual == expected


def test_pseudo_queue_enqueue_once():
    queue = PseudoQueue()
    queue.enqueue('1')
    actual = queue.s_1.peek()
    expected = '1'
    assert actual == expected
