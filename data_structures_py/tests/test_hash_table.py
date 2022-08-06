from data_structures_py.hash_tables.hash_table import *


def test_hash_method():
    hash_t = HashTable()
    expected = 652
    actual = hash_t._HashTable__hash('d')

    assert expected == actual


def test_exists():
    assert HashTable


def test_hash_create():
    ht = HashTable()
    assert ht


def test_size_default():
    ht = HashTable()
    actual = ht._HashTable__size
    expected = 1024
    assert actual == expected


def test_hash():
    ht = HashTable()
    index = ht._HashTable__hash("A")
    assert 0 <= index < ht._HashTable__size


def test_set():
    ht = HashTable()
    ht.set("C", "B")
    c_index = ht._HashTable__hash("C")
    actual = ht._HashTable__buckets[c_index]
    expected = ("C", "B")
    assert actual.head.value == expected


def test_collisions():
    ht = HashTable()
    ht.set("A", "K")
    ht.set("Y", "T")
    ht.set("T", "U")

    assert ht.get("A") == "K"
    assert ht.get("Y") == "T"
    assert ht.get("T") == "U"


def test_get():
    ht = HashTable()
    ht.set("C", "B")
    actual = ht.get("C")
    expected = "B"
    assert actual == expected


def test_contains():
    ht = HashTable()
    ht.set("C", "B")
    ht.set("E", 1)
    ht.set("S", True)
    ht.set("G", "H")
    actual = ht.contains("G")
    expected = True
    assert actual == expected


def test_contains_not():
    ht = HashTable()
    ht.set("C", "B")
    ht.set("E", 1)
    ht.set("S", True)
    ht.set("G", "H")
    actual = ht.contains("J")
    expected = False
    assert actual == expected


def test_contains_two_deep():
    ht = HashTable()
    ht.set("A", "B")
    ht.set("T", 1)
    actual = ht.contains("T")
    expected = True
    assert actual == expected


def test_key():
    ht = HashTable()
    ht.set("C", "B")
    ht.set("D", "B")
    actual = ht.key()
    expected = ["C", "D"]
    assert actual == expected


def test_key_collisions():
    ht = HashTable()
    ht.set("A", "B")
    ht.set("T", 1)
    actual = ht.key()
    expected = ["A", "T"]
    assert actual == expected
