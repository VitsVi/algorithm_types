import time
import random
from decimal import Decimal, getcontext
"""
В данном коде представлены алгоритмические сортировки разных типов.
Также таймеры выполнения и процентное сравнение времени всех сортировок.
Возможность автоматического заполнения списков для сортировок с параметрамизацией:
С экспотенциальным ростом количества элементов.

Представленные ниже виды сортировок:

    Пузырьковая сортировка
    Сортировка перемешиванием
    Сортировка вставками
    Сортировка слиянием
    Гномья сортировка
    Быстрая сортировка
    Пирамидальная сортировка

"""
getcontext().prec = 30

class SortParameters():
    """Класс статистических данных по сортировкам."""

    def __init__(self):
        self.list_array:list = [] # списки для сортировки
        self.lists_sorted_dict:dict  = {}
        self.sorting_time:dict = {} # запись данных по скорости сортировки
        self.time_procent: dict = {}
        self.sorting_time_all:float = 0

    def make_array_list(
            self,
            min_num:int=0,
            max_num:int=10,
            list_range:int=10,
            exponential_step:int=2,
            count:int=3,
            **args
        ):
        """Создать списки автоматически."""
        try:
            self.list_array = [
                [random.randint(
                    min_num,max_num*exponential_step**i
                ) for _ in range(list_range*(exponential_step**i))]
                 for i in range(count)
                ]
            print('Списки успешно созданы.')
            # for list in self.list_array:
            #     print(list)
        except Exception as error:
            print(f"Ошибка создания списков.\n {error}")


    def get_result(self, full:bool=False):
        """Результаты сортировок."""
        sorting_time_all = Decimal(str(self.sorting_time_all))
        if self.sorting_time:
            for key, value in self.sorting_time.items():
                value_decimal = Decimal(str(value))
                percent = (value_decimal/sorting_time_all)*100
                value *= 1000 # мс
                print(
                    f"{key}: {value:.8f} мс, {percent:.2f}%"
                )
            self.sorting_time_all *= 1000 # мс
            print(f"\nОбщее время сортировок: {self.sorting_time_all:.8f} мc")
            if full==True:
                print('\nОтсортированные списки:\n')
                for key, value in self.lists_sorted_dict.items():
                    print(
                        f"{key}: \n{value}"
                    )
            
        else:
            return "Сортировка ещё не запущена. Нет статистики времени."


    def __str__(self):
        return "Параметры и статистика сортировки"


class SortingVariables(SortParameters):
    """Виды сортирок."""

    def sorting_process(self, array_list:list=[],sort_function=None):
        """Общие процессы для всех сортировок."""

        if array_list == []:
            array_list = self.list_array
        else:
            self.list_array += array_list

        for array in array_list:
            time_count_start = time.perf_counter()  

            sort_function(array)

            time_count_end = time.perf_counter()
            sort_name = sort_function.__name__
            sort_name = sort_name.replace('_algorithm', '').replace('_wrapper','')
            self.sorting_time[
                f"{sort_name}_{str(len(array))}"
            ] = time_count_end - time_count_start
            self.sorting_time_all += time_count_end - time_count_start
            self.lists_sorted_dict[
                f"{sort_name}_{str(len(array))}"
            ] = array
        #print(*self.list_array, sep='\n')


    def bubble_sort(self, array_list:list=[]):
        """Сортировка пузырьком."""

        def bubble_sort_algorithm(array):

            loocking_range = len(array)

            for current_id in range(len(array)):
                max_item_id = 0

                for item_id in range(loocking_range - current_id):
                    if array[item_id] > array[max_item_id]:
                        max_item_id = item_id

                last_index = loocking_range - current_id - 1
                array[max_item_id], array[last_index] = \
                    array[last_index], array[max_item_id]
        
        self.sorting_process(array_list, bubble_sort_algorithm)


    def shaker_sort(self, array_list:list=[]):
        """Сортировка перемешиванием."""

        def shaker_sort_algorithm(array):
            current_item_index = 0
            item_index = 0
            left_field = 0
            right_field = len(array)
            right_move = True
            while left_field < right_field:
                if right_move==True:
                    if array[item_index] > array[current_item_index]:
                        current_item_index = item_index
                    if current_item_index + 1 == right_field:
                        right_move = False
                    else:
                        current_item_index += 1
                        right_field -= 1
                else:
                    if array[item_index] < array[current_item_index]:
                        current_item_index = item_index
                    if current_item_index - 1 == left_field:
                        right_move = True
                    else:
                        current_item_index -= 1
                        left_field += 1

        self.sorting_process(array_list, shaker_sort_algorithm)


    def insertion_sort(self,array_list:list=[]):
        """Сортировка вставками."""

        def insertion_sort_algorithm(array):

            for item_index in range(1,len(array)):
                current_item_index = item_index
                while current_item_index > 0 and array[current_item_index] < array[current_item_index-1]:
                    array[current_item_index], array[current_item_index - 1] = \
                        array[current_item_index-1], array[current_item_index]
                    current_item_index -=1
        
        self.sorting_process(array_list, insertion_sort_algorithm)


    def merge_sort(self, array_list:list=[]):
        """Сортировка слиянием."""

        def merge_sort_algorithm(array):
            if len(array) <= 1:
                return array
            mid = len(array) // 2
            left_part = merge_sort_algorithm(array[:mid])
            right_part = merge_sort_algorithm(array[mid:])
            return merge(left_part,right_part)
        
        def merge(left,right):

            merged = []
            left_index, right_index = 0, 0
            while left_index < len(left) and right_index < len(right):
                if left[left_index] <= right[right_index]:
                    merged.append(left[left_index])
                    left_index +=1
                else:
                    merged.append(right[right_index])
                    right_index +=1

            merged.extend(left[left_index:])
            merged.extend(right[right_index:])

            return merged
        
        def merge_sort_wrapper(array):
            
            sorted_array = merge_sort_algorithm(array)
            array[:] = sorted_array
        
        self.sorting_process(array_list, merge_sort_wrapper)


    def gnome_sort(self, array_list:list=[]):
        """Гномья сортировка."""

        def gnome_sort_algorithm(array):
            item_index = 0
            while item_index < len(array) - 1:
                if array[item_index] <= array[item_index+1]:
                    item_index +=1
                elif array[item_index] > array[item_index+1]:
                    array[item_index], array[item_index+1] \
                        = array[item_index+1], array[item_index]
                    if item_index !=0:
                        item_index -=1

        self.sorting_process(array_list, gnome_sort_algorithm)


    def quick_sort(self, array_list:list=[]):
        """Быстрая сортировка."""

        def quick_sort_algorithm(array):

            if len(array) <= 1:
                return array
            field = array[-1]
            left = [i for i in array[:-1] if i <= field]
            right = [i for i in array[:-1] if i > field]
            return quick_sort_algorithm(left) + [field] + quick_sort_algorithm(right)


        def quick_sort_wrapper(array):
            try:
                sorted_array = quick_sort_algorithm(array)
                array[:] = sorted_array
            except Exception as error:
                print('ERROR. ', error)

        self.sorting_process(array_list, quick_sort_wrapper)


    def heap_sort(self, array_list: list = []):
        """Пирамидальная сортировка."""

        def heapify_sort(array, heap_len, largest_index):
            largest = largest_index
            left = 2 * largest_index + 1
            right = 2 * largest_index + 2

            if left < heap_len and array[left] > array[largest]:
                largest = left

            if right < heap_len and array[right] > array[largest]:
                largest = right

            if largest != largest_index:
                array[largest_index], array[largest] = array[largest], array[largest_index]

                heapify_sort(array, heap_len, largest)

        def heap_sort_algorithm(array):
            arr_len = len(array)

            for i in range(arr_len // 2 - 1, -1, -1):
                heapify_sort(array, arr_len, i)

            for i in range(arr_len - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                heapify_sort(array, i, 0)

            return array

        def heap_sort_wrapper(array):
            sorted_array = heap_sort_algorithm(array)
            array[:] = sorted_array

        self.sorting_process(array_list, heap_sort_wrapper)



if __name__ == "__main__":
    test = SortingVariables()
    test.make_array_list(
        min_num=0,
        max_num=10,
        list_range=10,
        exponential_step=2,
        count=6,
    )
    test.bubble_sort()
    test.shaker_sort()
    test.insertion_sort()
    test.merge_sort()
    test.gnome_sort()
    test.quick_sort()
    test.heap_sort()
    test.get_result()


"""
Списки успешно созданы.
bubble_sort_10: 0.01230000 мс, 0.15%    
bubble_sort_20: 0.01570000 мс, 0.19%    
bubble_sort_40: 0.04520000 мс, 0.56%    
bubble_sort_80: 0.15350000 мс, 1.89%    
bubble_sort_160: 0.56190000 мс, 6.93%   
bubble_sort_320: 1.37650000 мс, 16.99%  
shaker_sort_10: 0.00330000 мс, 0.04%    
shaker_sort_20: 0.00310000 мс, 0.04%    
shaker_sort_40: 0.00560000 мс, 0.07%    
shaker_sort_80: 0.01010000 мс, 0.12%    
shaker_sort_160: 0.02080000 мс, 0.26%   
shaker_sort_320: 0.04230000 мс, 0.52%   
insertion_sort_10: 0.00270000 мс, 0.03% 
insertion_sort_20: 0.00160000 мс, 0.02% 
insertion_sort_40: 0.00210000 мс, 0.03% 
insertion_sort_80: 0.00390000 мс, 0.05% 
insertion_sort_160: 0.00760000 мс, 0.09%
insertion_sort_320: 0.01650000 мс, 0.20%
merge_sort_10: 0.01720000 мс, 0.21%     
merge_sort_20: 0.01550000 мс, 0.19%     
merge_sort_40: 0.02770000 мс, 0.34%     
merge_sort_80: 0.05660000 мс, 0.70%     
merge_sort_160: 0.12370000 мс, 1.53%    
merge_sort_320: 0.27080000 мс, 3.34%    
gnome_sort_10: 0.00220000 мс, 0.03%     
gnome_sort_20: 0.00260000 мс, 0.03%     
gnome_sort_40: 0.00490000 мс, 0.06%     
gnome_sort_80: 0.00960000 мс, 0.12%     
gnome_sort_160: 0.01910000 мс, 0.24%    
gnome_sort_320: 0.04490000 мс, 0.55%
quick_sort_10: 0.01460000 мс, 0.18%
quick_sort_20: 0.02300000 мс, 0.28%
quick_sort_40: 0.06440000 мс, 0.79%
quick_sort_80: 0.26090000 мс, 3.22%
quick_sort_160: 0.81240000 мс, 10.03%
quick_sort_320: 3.22300000 мс, 39.77%
heap_sort_10: 0.01810000 мс, 0.22%
heap_sort_20: 0.01760000 мс, 0.22%
heap_sort_40: 0.03750000 мс, 0.46%
heap_sort_80: 0.08710000 мс, 1.07%
heap_sort_160: 0.20540000 мс, 2.53%
heap_sort_320: 0.45980000 мс, 5.67%

Общее время сортировок: 8.10330000 мc
"""