def insertion_sort(arr, arr_len):
	for i in range(arr_len):
		tmp = arr[i]
		j = i - 1
		while tmp < arr[j] and j >= 0:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = tmp
	return arr


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(insertion_sort(list_a, len_list))
