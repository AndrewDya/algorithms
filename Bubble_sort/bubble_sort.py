def bubble_sort(a, n):
	for i in range(n):
		for j in range(n - 1 - i):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
	return a


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(bubble_sort(list_a, n))
