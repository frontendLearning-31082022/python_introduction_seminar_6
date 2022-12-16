# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта,
# сделать замеры времени, оптимизировать, вновь выполнить замеры
# и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

# Описания нужно делать в виде docstrings

from timeit import repeat, default_timer

from src_homeworks_completed_tasks.for_time_optimaze.sem_3_one_more_1 \
    import sum_odd_digits as slow_ver_sum_odd_digits
from optimaze_task_1_first \
    import sum_odd_digits as new_ver_sum_odd_digits

from src_homeworks_completed_tasks.for_time_optimaze.sem_2_one_more_3 \
    import shuffle_list as slow_ver_shuffle_list
from optimaze_task_1_second \
    import shuffle_list as new_ver_shuffle_list


class TestClass:
    count_digs = 10000

    @staticmethod
    def test_first(list_digits):
        slow_ver_sum_odd_digits(list_digits)

    @staticmethod
    def optimaze_first(list_digits):
        new_ver_sum_odd_digits(list_digits)

    @staticmethod
    def test_second(count_n_value):
        slow_ver_shuffle_list(count_n_value)

    @staticmethod
    def optimaze_second(count_n_value):
        new_ver_shuffle_list(count_n_value)


if __name__ == '__main__':
    setup = """
from __main__ import TestClass
test = TestClass()
    """

    """Генерация списка с помощью list.append
        обход всех элементов в цикле и накапливание суммы в переменную
        если остаток от деления не равен нулю
     """
    statements = ['TestClass.test_first(TestClass.count_digs)']
    print(
        f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
    #     результат 7.63 секунд для 10000 чисел

    """Во втором случае исользуем list comprehension 
    для генерация всего списка при этом пропускаем элементы с четной позицией
    """
    statements = ['TestClass.optimaze_first(TestClass.count_digs)']
    print(
        f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
    """результат 4.27 секунд для 10000 чисел"""

    """"Реализация простого алгоритма перемешивания. 
        С помощью временной переменной 
        и обмена местами между двумя элементами (случайный индекс).
        Проход с помощью цикла по всем элементам списка
    """
    statements = ['TestClass.test_second(10000)']
    print(
        f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
    """результат 13.70 секунд для 10000 элементов"""

    """использование функции Python random.shuffle для данной цели"""
    statements = ['TestClass.optimaze_second(10000)']
    print(
        f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
    """результат 5.27 секунд для 10000 элементов"""
