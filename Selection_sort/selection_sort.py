def selection_sort(arr, arr_len):
	for i in range(arr_len - 1):
		max_index = i
		for j in range(i + 1, arr_len):
			if arr[j] < arr[max_index]:
				max_index = j
		arr[i], arr[max_index] = arr[max_index], arr[i]
	return arr


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(selection_sort(list_a, len_list))
