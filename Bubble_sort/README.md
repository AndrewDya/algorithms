## Сортировка пузырьком (Bubble Sort)

Сортировка пузырьком (Bubble Sort) является простым алгоритмом сортировки, который применяется для упорядочивания элементов в списке. Алгоритм получил свое название из-за того, что на каждом проходе самый большой элемент "всплывает" на правильную позицию, подобно пузырьку, поднимающемуся на поверхность жидкости.

### Описание алгоритма

Алгоритм сортировки пузырьком основан на сравнении и обмене пар соседних элементов списка до тех пор, пока список полностью не будет отсортирован. На каждом проходе по списку самый большой элемент "всплывает" на правильную позицию в конце списка.

1. Начинаем сравнивать элементы списка попарно, начиная с первых двух элементов. Если порядок элементов неправильный (текущий элемент больше следующего), то меняем их местами.
2. Переходим к следующей паре элементов и продолжаем сравнивать их.
3. Проходим по списку до конца, повторяя шаги 1 и 2.
4. После первого прохода самый большой элемент будет находиться в конце списка.
5. Повторяем проходы по списку, исключая уже отсортированные элементы, до тех пор, пока весь список не будет отсортирован.

### Пример работы алгоритма

Для наглядности приведем пример работы алгоритма на списке чисел: [4, 9, 0, 17, 23, 4, 1, 0]

1. Первый проход:
   - Сравниваем 4 и 9, меняем местами (список: [4, 9, 0, 17, 23, 4, 1, 0])
   - Сравниваем 9 и 0, не меняем местами (список: [4, 9, 0, 17, 23, 4, 1, 0])
   - Сравниваем 0 и 17, не меняем местами (список: [4, 9, 0, 17, 23, 4, 1, 0])
   - Сравниваем 17 и 23, не меняем местами (список: [4, 9, 0, 17, 23, 4, 1, 0])
   - Сравниваем 23 и 4, меняем местами (список: [4, 9, 0, 17, 4, 23, 1, 0])
   - Сравниваем 23 и 1, меняем местами (список: [4, 9, 0, 17, 4, 1, 23, 0])
   - Сравниваем 23 и 0, меняем местами (список: [4, 9, 0, 17, 4, 1, 0, 23])

2. Второй проход:
   - Сравниваем 4 и 9, не меняем местами (список: [4, 9, 0, 17, 4, 1, 0, 23])
   - Сравниваем 9 и 0, меняем местами (список: [4, 0, 9, 17, 4, 1, 0, 23])
   - Сравниваем 9 и 17, не меняем местами (список: [4, 0, 9, 17, 4, 1, 0, 23])
   - Сравниваем 17 и 4, меняем местами (список: [4, 0, 9, 4, 17, 1, 0, 23])
   - Сравниваем 17 и 1, меняем местами (список: [4, 0, 9, 4, 1, 17, 0, 23])
   - Сравниваем 17 и 0, меняем местами (список: [4, 0, 9, 4, 1, 0, 17, 23])

3. Третий проход:
   - Сравниваем 4 и 0, меняем местами (список: [0, 4, 9, 4, 1, 0, 17, 23])
   - Сравниваем 4 и 9, не меняем местами (список: [0, 4, 9, 4, 1, 0, 17, 23])
   - Сравниваем 9 и 4, меняем местами (список: [0, 4, 4, 9, 1, 0, 17, 23])
   - Сравниваем 9 и 1, меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])

4. Четвертый проход:
   - Сравниваем 0 и 4, не меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])
   - Сравниваем 4 и 4, не меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])

5. Пятый проход:
   - Сравниваем 0 и 4, не меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])

6. Шестой проход:
   - Сравниваем 0 и 4, не меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])

7. Седьмой проход:
   - Сравниваем 0 и 4, не меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])

8. Восьмой проход:
   - Сравниваем 0 и 4, не меняем местами (список: [0, 4, 4, 1, 9, 0, 17, 23])

После восьми проходов список полностью отсортирован: [0, 0, 1, 4, 4, 9, 17, 23].

### Сложность алгоритма

Алгоритм сортировки пузырьком имеет временную сложность O(n^2), где n - количество элементов в списке. Это значит, что время выполнения алгоритма увеличивается квадратично с ростом размера списка. В худшем случае, когда список уже отсортирован в обратном порядке, потребуется n проходов и n сравнений на каждом проходе.

### Реализация на Python

```python
def bubble_sort(arr, arr_len):
    for i in range(arr_len):
        for j in range(arr_len - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Пример использования
list_a = [4, 9, 0, 17, 23, 4, 1, 0]
len_list = len(list_a)
print(bubble_sort(list_a, len_list))
```

# Временная сложность
Временная сложность сортировки пузырьком в худшем и среднем случаях составляет O(n^2), где n - количество элементов в списке. Это связано с тем, что внешний цикл выполняется n раз, а внутренний цикл в худшем случае также выполняется n раз для каждой итерации внешнего цикла.