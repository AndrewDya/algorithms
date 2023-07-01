def quick_sort(arr, arr_len):
	if arr_len <= 1:
		return arr

	pivot = arr[arr_len // 2]
	left, middle, right = [], [], []

	for num in arr:
		if num < pivot:
			left.append(num)
		elif num == pivot:
			middle.append(num)
		else:
			right.append(num)

	return quick_sort(left, arr_len(left)) + middle + quick_sort(right, arr_len(right))


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(quick_sort(list_a, len_list))
