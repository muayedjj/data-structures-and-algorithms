import pytest
from data_structures_py.hash_tables.hashmap_repeated_word import hashmap_repeated_word, par_3, par_2, par_1


def test_empty():
    with pytest.raises(Exception) as err:
        actual = hashmap_repeated_word('')
    expected = "Can't search without a text!"
    assert str(err.value) == expected


def test_case_one():
    expected = 'a'
    actual = hashmap_repeated_word(par_1)
    assert actual == expected


def test_case_two():
    expected = 'it'
    actual = hashmap_repeated_word(par_2)
    assert actual == expected


def test_case_three():
    expected = 'summer'
    actual = hashmap_repeated_word(par_3)
    assert actual == expected
