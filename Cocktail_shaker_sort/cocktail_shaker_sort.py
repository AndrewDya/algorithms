def cocktail_shaker_sort(arr, arr_len):
    left, right = 0, arr_len - 1
    while left <= right:
        swapped = False

        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        right -= 1

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        left += 1

        if not swapped:
            break
    return arr


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(cocktail_shaker_sort(list_a, len_list))
