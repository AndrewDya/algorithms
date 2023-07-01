def selection_sort(a, n):
	for i in range(n - 1):
		max_index = i
		for j in range(i + 1, n):
			if a[j] < a[max_index]:
				max_index = j
		a[i], a[max_index] = a[max_index], a[i]
	return a


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(selection_sort(list_a, n))
