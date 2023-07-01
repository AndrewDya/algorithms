def merge_sort(a, n):
	if n <= 1:
		return a

	mid = n // 2
	left = a[:mid]
	right = a[mid:]

	merge_sort(left, len(left))
	merge_sort(right, len(right))

	i = j = k = 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			a[k] = left[i]
			i += 1
		else:
			a[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		a[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		a[k] = right[j]
		j += 1
		k += 1

	return a


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(merge_sort(list_a, n))
