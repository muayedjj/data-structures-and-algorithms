def insertion_sort(arr):
    if arr is []:
        return []
    else:
        for i in range(1, len(arr)):

            chk = arr[i]

            j = i - 1
            while j >= 0 and chk < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = chk


arr_1 = [8, 4, 23, 42, 16, 15]
arr_2 = []
insertion_sort(arr_1)
print(arr_1)