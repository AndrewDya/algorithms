def cocktail_shaker_sort(a, n):
	left, right = 0, n - 1
	while left <= right:
		swapped = False

		for i in range(left, right):
			if a[i] > a[i + 1]:
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True
		right -= 1

		for i in range(right, left, -1):
			if a[i] < a[i - 1]:
				a[i], a[i - 1] = a[i - 1], a[i]
				swapped = True
		left += 1

		if not swapped:
			break
	return a


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(cocktail_shaker_sort(list_a, n))
