def merge_sort(arr, arr_len):
	if arr_len <= 1:
		return arr

	mid = arr_len // 2
	left = arr[:mid]
	right = arr[mid:]

	merge_sort(left, len(left))
	merge_sort(right, len(right))

	i = j = k = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1

	return arr


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(merge_sort(list_a, len_list))
