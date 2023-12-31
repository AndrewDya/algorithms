# Быстрая сортировка (Quick Sort)

Быстрая сортировка - это эффективный алгоритм сортировки, основанный на принципе "разделяй и властвуй". Он выбирает опорный элемент из списка и разделяет остальные элементы на две группы: элементы, меньшие опорного, и элементы, большие опорного. Затем он рекурсивно применяет ту же операцию к двум группам, пока не достигнет базового случая, когда размер группы становится меньше или равен 1.

## Описание алгоритма

Алгоритм быстрой сортировки работает следующим образом:

1. Если размер списка `n` меньше или равен 1, возвращаем список (базовый случай).
2. Выбираем опорный элемент из списка. Обычно в качестве опорного элемента выбирают средний элемент, но его выбор может быть разным.
3. Создаем три пустых списка: `left`, `middle` и `right`.
4. Проходим по каждому элементу списка и добавляем его в соответствующий список:
   - Если элемент меньше опорного, добавляем его в список `left`.
   - Если элемент равен опорному, добавляем его в список `middle`.
   - Если элемент больше опорного, добавляем его в список `right`.
5. Рекурсивно вызываем функцию `quick_sort` для списка `left` и `right`.
6. Объединяем отсортированные списки `left`, `middle` и `right` в один отсортированный список.
7. Возвращаем отсортированный список.

## Пример использования

```python
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

```

# Временная сложность
Быстрая сортировка в среднем случае имеет временную сложность O(n log n), где n - размер списка. Однако, в худшем случае, время работы может быть O(n^2). Возможны различные методы выбора опорного элемента, которые могут повлиять на производительность алгоритма.