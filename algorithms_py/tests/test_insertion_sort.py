from algorithms_py.sorting.insertion.insertion_sort import insertion_sort


def test_insertion_sort():
    arr_1 = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(arr_1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_empty():
    arr_2 = []
    actual = insertion_sort(arr_2)
    expected = []
    assert actual == expected

