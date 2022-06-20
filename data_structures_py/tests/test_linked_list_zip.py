from data_structures_py.linked_list.linkedlist import Node, LinkedList
from data_structures_py.linked_list.linked_list_zip import zip_lists
import pytest


def test_zip_lists(create_list_one, create_list_two):
    expected = "{ A } -> { 1 } -> { B } -> { 2 } -> { C } -> { 3 } -> { D } -> { 4 } -> { E } -> { 5 } -> NULL"
    actual = zip_lists(create_list_one, create_list_two)

    assert expected == actual


def test_one_shorter(list_one_short, create_list_two):
    expected = "{ 1 } -> { A } -> { 2 } -> { B } -> { 3 } -> { C } -> { 4 } -> { 5 } -> NULL"
    actual = zip_lists(list_one_short, create_list_two)

    assert expected == actual


def test_two_shorter(create_list_one, list_two_short):
    expected = '{ A } -> { 1 } -> { B } -> { 2 } -> { C } -> { 3 } -> { D } -> { E } -> NULL'
    actual = zip_lists(create_list_one, list_two_short)

    assert expected == actual


def test_one_empty(list_one_empty, create_list_two):
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> NULL'
    actual = zip_lists(list_one_empty, create_list_two)

    assert expected == actual


def test_two_empty(create_list_one, list_two_empty):
    expected = '{ A } -> { B } -> { C } -> { D } -> { E } -> NULL'
    actual = zip_lists(create_list_one, list_two_empty)

    assert expected == actual


@pytest.fixture
def create_list_one():
    list_one = LinkedList()
    list_one.append('A')
    list_one.append('B')
    list_one.append('C')
    list_one.append('D')
    list_one.append('E')

    return list_one


@pytest.fixture
def create_list_two():
    list_two = LinkedList()
    list_two.append('1')
    list_two.append('2')
    list_two.append(3)
    list_two.append(4)
    list_two.append(5)

    return list_two


@pytest.fixture
def list_two_short():
    list_two = LinkedList()
    list_two.append('1')
    list_two.append('2')
    list_two.append(3)

    return list_two


@pytest.fixture
def list_one_short():
    list_one = LinkedList()
    list_one.append('A')
    list_one.append('B')
    list_one.append('C')

    return list_one


@pytest.fixture
def list_one_empty():
    list_one = LinkedList()

    return list_one


@pytest.fixture
def list_two_empty():
    list_two = LinkedList()

    return list_two

