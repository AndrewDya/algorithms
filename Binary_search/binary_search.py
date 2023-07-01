def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False  # Если элемент не найден


# Пример использования
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_num = 6
result = binary_search(list_a, search_num)

if result:
    print(f"Элемент {search_num} найден в индексе {result}")
else:
    print("Элемент не найден")

