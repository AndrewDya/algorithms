def quick_sort(a, n):
	if n <= 1:
		return a

	pivot = a[n // 2]
	left = []
	middle = []
	right = []

	for num in a:
		if num < pivot:
			left.append(num)
		elif num == pivot:
			middle.append(num)
		else:
			right.append(num)

	return quick_sort(left, len(left)) + middle + quick_sort(right, len(right))


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(quick_sort(list_a, n))
