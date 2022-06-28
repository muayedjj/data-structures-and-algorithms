import pytest as pytest

from data_structures_py.linked_list.stack_queue_animal_shelter import Animal, AnimalShelter


def test_enqueue_once(dog1):
    AnimalShelter.enqueue(dog1)
    expected = 'dog'
    actual = AnimalShelter.dequeue(dog1)
    assert expected == actual


def test_enqueue_once(dog1, dog2, cat1, cat2):
    AnimalShelter.enqueue(cat1)
    AnimalShelter.enqueue(dog2)
    AnimalShelter.enqueue(dog1)
    AnimalShelter.enqueue(cat2)
    expected = 'cat'
    actual = AnimalShelter.dequeue(cat1)
    assert expected == actual


def test_enqueue_once(dog1):
    AnimalShelter.enqueue(cat1)
    AnimalShelter.enqueue(dog1)
    AnimalShelter.dequeue(cat1)
    expected = 'dog'
    actual = AnimalShelter.dequeue(dog1)
    assert expected == actual


def test_enqueue_once(dog1, dog2, cat1, cat2):
    AnimalShelter.enqueue(cat1)
    AnimalShelter.enqueue(dog2)

    AnimalShelter.dequeue(cat1)
    AnimalShelter.dequeue(dog2)

    AnimalShelter.enqueue(dog1)
    AnimalShelter.enqueue(cat2)

    AnimalShelter.dequeue(dog1)
    actual = AnimalShelter.dequeue(cat1)
    expected = 'cat'
    assert expected == actual





@pytest.fixture
def dog1():
    dog = Animal()
    return dog.dog()


@pytest.fixture
def dog2():
    dog = Animal()
    return dog.dog()


@pytest.fixture
def cat1():
    cat = Animal()
    return cat.cat()


@pytest.fixture
def cat2():
    cat = Animal()
    return cat.cat()
