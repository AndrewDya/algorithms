# Сортировка выбором (Selection Sort)

Сортировка выбором - это простой алгоритм сортировки, который на каждом шаге находит наименьший (или наибольший) элемент из неотсортированной части списка и помещает его в начало (или конец) отсортированной части. Алгоритм продолжает эту операцию до тех пор, пока весь список не будет отсортирован.

## Описание алгоритма

Алгоритм сортировки выбором работает следующим образом:

1. Проходим по списку и находим наименьший (или наибольший) элемент. Пусть это будет элемент с индексом `min_index`.
2. Меняем местами найденный элемент с элементом в начале списка (или конце списка, в зависимости от порядка сортировки).
3. Увеличиваем начальный индекс и повторяем шаги 1 и 2 для оставшейся неотсортированной части списка.
4. Повторяем шаги 1-3 до тех пор, пока весь список не будет отсортирован.

## Пример использования

```python
def selection_sort(a, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
print(selection_sort(list_a, n))
```

# Временная сложность
Сортировка выбором имеет постоянную временную сложность для лучшего, худшего и среднего случаев, и она равна O(n^2), где n - размер списка. Этот алгоритм не эффективен для больших списков, но он прост в реализации и может быть полезен для небольших массивов или в случаях, когда требуется сортировка только части списка.