import pytest
from data_structures_py.linked_list.stack_and_queue import Node, Stack, Queue


def test_instantiated():
    stack = Stack()
    expected = None
    actual = stack.top
    assert actual == expected


def test_new_push():
    new_stack = Stack()
    new_stack.push('Kartoffel')
    actual = new_stack.top.value
    expected = 'Kartoffel'
    assert actual == expected


def test_push():
    stack = Stack()
    stack.push('A')
    actual = stack.top.value
    expected = 'A'
    assert actual == expected


def test_push_many():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    actual = stack.top.value
    expected = 'C'
    assert actual == expected


def test_pop():
    stack = Stack()
    stack.push("A")
    actual = stack.pop()
    expected = "A"
    assert actual == expected


def test_pop_all():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected


def test_peek_once():
    stack = Stack()
    stack.push("A")
    actual = stack.peek()
    expected = "A"
    assert actual == expected


def test_emptiness_check():
    stack = Stack()
    stack.push("A")
    stack.push("B")
    actual = stack.is_empty()
    expected = False
    assert actual == expected


def test_peek_empty():
    stack = Stack()
    with pytest.raises(BaseException) as err:
        stack.peek()
    assert str(err.value) == "Error! Empty Stack"


def test_pop_empty():
    stack = Stack()
    with pytest.raises(BaseException) as err:
        stack.pop()
    assert str(err.value) == "Error! Empty Stack"


# Queue class tests
def test_enqueue():
    new_queue = Queue()
    new_queue.enqueue("A")
    actual = new_queue.front.value
    expected = "A"
    assert actual == expected


def test_dequeue_value():
    queue = Queue()
    queue.enqueue("A")
    actual = queue.dequeue()
    expected = "A"
    assert actual == expected


def test_peek_into_value():
    queue = Queue()
    queue.enqueue("A")
    actual = queue.peek()
    expected = 'A'
    assert actual == expected


def test_peek_into_empty():
    queue = Queue()
    with pytest.raises(BaseException) as err:
        queue.peek()

    assert str(err.value) == "Error! Empty Queue"


def test_enqueue_once():
    queue = Queue()
    queue.enqueue("A")
    actual = queue.peek()
    expected = "A"
    assert actual == expected


def test_enqueue_two():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)

    actual = queue.peek()
    expected = 1
    assert actual == expected


def test_dequeue_when_empty():
    queue = Queue()
    with pytest.raises(BaseException) as err:
        queue.dequeue()

    assert str(err.value) == "Error! Empty Queue"


def test_dequeue_values():
    queue = Queue()
    queue.enqueue("A")
    queue.enqueue("B")
    actual = queue.dequeue()
    expected = 'A'
    assert actual == expected


def test_is_empty():
    queue = Queue()
    with pytest.raises(BaseException) as err:
        queue.peek()

    assert str(err.value) == "Error! Empty Queue"
