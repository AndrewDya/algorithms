def insertion_sort(a, n):
	for i in range(n):
		tmp = a[i]
		j = i - 1
		while tmp < a[j] and j >= 0:
			a[j + 1] = a[j]
			j -= 1
		a[j + 1] = tmp
	return a


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(insertion_sort(list_a, n))
