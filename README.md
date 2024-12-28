
# Скорость разных типов алгоритмических сортировок

В данном коде представлены алгоритмические сортировки разных типов.
Также реализованы таймеры выполнения и процентное сравнение времени всех сортировок.

* Возможность автоматического заполнения списков для сортировок с параметризацией.
* Экспоненциальный рост количества элементов.

## Представленные виды сортировок:

1. Пузырьковая сортировка
2. Сортировка перемешиванием
3. Сортировка вставками
4. Сортировка слиянием
5. Гномья сортировка
6. Быстрая сортировка
7. Пирамидальная сортировка

## Основной класс

Методы вызываются с помощью экземпляра класса `SortingVariables()`.

```python
SortingVariables()
```

## Параметры методов

### Автоматическое заполнение списков:

```python
<ClassObject>.make_array_list(
    self,
    min_num: int = 0,
    max_num: int = 10,
    list_range: int = 10,
    exponential_step: int = 2,
    count: int = 3,
    **args
)
```

**Параметры**:
- `min_num, max_num`: Диапазон значений списка.
- `list_range`: Длина первого списка.
- `exponential_step`: Экспоненциальный рост длины с увеличением количества списков.
- `count`: Общее количество созданных списков.

### Результаты сортировок:

```python
<ClassObject>.get_result(self, full: bool = False)
```

**Параметры**:
- `full=True`: Вывод всех отсортированных списков.

### Вызов методов с собственными списками

Методы принимают переменную типа `list`. Ожидается список со списками.

```python
<ClassObject>.bubble_sort(self, array_list: list = [])
```

Если параметр не передан, подставляется `array_list`, созданный при вызове `make_array_list()`.

## Список доступных методов:

### 1. Пузырьковая сортировка
```python
<ClassObject>.bubble_sort(self, array_list: list = [])
```

### 2. Сортировка перемешиванием
```python
<ClassObject>.shaker_sort(self, array_list: list = [])
```

### 3. Сортировка вставками
```python
<ClassObject>.insertion_sort(self, array_list: list = [])
```

### 4. Сортировка слиянием
```python
<ClassObject>.merge_sort(self, array_list: list = [])
```

### 5. Гномья сортировка
```python
<ClassObject>.gnome_sort(self, array_list: list = [])
```

### 6. Быстрая сортировка
```python
<ClassObject>.quick_sort(self, array_list: list = [])
```

### 7. Пирамидальная сортировка
```python
<ClassObject>.heap_sort(self, array_list: list = [])
```

---

### Как использовать:

1. Инициализируйте объект класса `SortingVariables`:
   ```python
   sorter = SortingVariables()
   ```

2. Используйте метод для создания списков с параметризацией:
   ```python
   sorter.make_array_list(min_num=0, max_num=100, list_range=10, exponential_step=2, count=5)
   ```

3. Запустите сортировку для вашего списка:
   ```python
   sorter.bubble_sort(array_list=your_list)
   ```

4. Получите результаты сортировки:
   ```python
   sorter.get_result(full=True)
   ```

---

## Примечания

- Все сортировки поддерживают параметр `array_list`, который позволяет передавать собственный список для сортировки. Если список не передан, будет использоваться тот, что был создан с помощью метода `make_array_list()`.
- Программа поддерживает замеры времени для каждой сортировки и отображает их в процентном соотношении.
