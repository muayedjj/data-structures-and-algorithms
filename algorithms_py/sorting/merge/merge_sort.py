def merge_sort(arr):
    if len(arr) > 1:

        mid = int(len(arr) / 2)

        left = arr[:mid]

        rt = arr[mid:]

        merge_sort(left)

        merge_sort(rt)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(rt):
            if left[i] < rt[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = rt[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(rt):
            arr[k] = rt[j]
            j += 1
            k += 1

        return arr

    else:
        return []


if __name__ == "__main__":

    arr_1 = [8, 4, 23, 42, 16, 15]
    arr_2 = []
    merge_sort(arr_1)
    print(arr_1)
    print(merge_sort(arr_2))