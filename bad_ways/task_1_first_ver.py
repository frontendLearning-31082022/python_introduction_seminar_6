# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта,
# сделать замеры времени, оптимизировать, вновь выполнить замеры
# и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

# Описания нужно делать в виде docstrings

import optimaze_task_1_first
from optimaze_task_1_first import sum_odd_digits

import optimaze_task_1_second
import src_homeworks_completed_tasks.for_time_optimaze.sem_2_one_more_3
from bad_ways.sem_3_one_more_1 import sum_odd_digits


class TestClass:
    list_digits = None

    @staticmethod
    def test_first(list_digits):
        sum_odd_digits(list_digits)

    @staticmethod
    def optimaze_first(list_digits):
        optimaze_task_1_first.sum_odd_digits(list_digits)

    @staticmethod
    def test_second(count_n_value):
        src_homeworks_completed_tasks.for_time_optimaze.sem_2_one_more_3.shuffle_list(
            count_n_value)

    @staticmethod
    def optimaze_second(count_n_value):
        optimaze_task_1_second.shuffle_list(count_n_value)


if __name__ == '__main__':
    setup = """
from __main__ import TestClass
test = TestClass()
    """

#     TestClass.list_digits = [randrange(100) for i in range(1, 100000)]
#     statements = ['TestClass.test_first(TestClass.list_digits)']
#     print( f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# #     результат 7.180608901999676
#
#     statements = ['TestClass.optimaze_first(TestClass.list_digits)']
#     print(f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# #     результат 0.0720014909998099


# использование функции Python random.shuffle
# statements = ['TestClass.optimaze_second(10000)']
# print(f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# # #     результат 5.272738862999859


# statements = ['TestClass.optimaze_first(10000)']
# print(
#     f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# # результаты стандартной функции 10.344907774999683

#     statements = ['TestClass.test_second(10000)']
#     print(f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# #     результат 13.707259643000043

# использование функции Python random.shuffle
# statements = ['TestClass.optimaze_second(10000)']
# print(f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# # #     результат 5.272738862999859
