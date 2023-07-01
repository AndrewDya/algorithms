def bubble_sort(arr, arr_len):
    for i in range(arr_len):
        for j in range(arr_len - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(bubble_sort(list_a, len_list))
