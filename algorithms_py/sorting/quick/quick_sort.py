def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)

        quick_sort(arr, pivot + 1, high)

    return arr


if __name__ == "__main__":

    arr_1 = [8, 4, 23, 42, 16, 15]
    # arr_2 = []

    low_1 = 0
    high_1 = len(arr_1) - 1
    quick_sort(arr_1, low_1, high_1)
    print(arr_1)

    # print(quick_sort(arr_2))
