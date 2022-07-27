from algorithms_py.sorting.insertion.insertion_sort import insertion_sort


def test_insertion_sort_pos_int():
    arr_1 = [8, 4, 23, 42, 16, 15]
    actual = insertion_sort(arr_1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_insertion_sort_inc_neg_int():
    arr_1 = [8, -4, 23, -42, -16, 15]
    actual = insertion_sort(arr_1)
    expected = [-42, -16, -4, 8, 15, 23]
    assert actual == expected


def test_insertion_sort_inc_zero():
    arr_1 = [8, 4, 23, 42, 16, 15, 0]
    actual = insertion_sort(arr_1)
    expected = [0, 4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_insertion_sort_inc_floats():
    arr_1 = [8, 4, 23.0, 42, 15.5, 15.2]
    actual = insertion_sort(arr_1)
    expected = [4, 8, 15.2, 15.5, 23.0, 42]
    assert actual == expected


def test_empty():
    arr_2 = []
    actual = insertion_sort(arr_2)
    expected = []
    assert actual == expected

