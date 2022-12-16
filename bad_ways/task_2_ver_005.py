# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта,
# сделать замеры памяти, оптимизировать, вновь выполнить замеры
# и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

# Описания нужно делать в виде docstrings
import random
import string

from memory_profiler import profile

import optimaze_task_2_first
import optimaze_task_2_second
import optimaze_task_2_third

from src_homeworks_completed_tasks.for_memory_optimaze.sem_3_one_more_1 import \
    sum_odd_digits
from src_homeworks_completed_tasks.for_memory_optimaze.sem_2_task_4 import \
    split_line_text_by_space
from src_homeworks_completed_tasks.for_memory_optimaze.sem_1_task_4 import \
    find_big_number_in_digit




class TestClass:

    @staticmethod
    @profile
    def test_first(count_digits):
        sum_result=sum_odd_digits(count_digits)
        # print(sum_result)

    @staticmethod
    def optimaze_first(count_digits):
        sum_result = optimaze_task_2_first.sum_odd_digits(count_digits)
        # print(sum_result)

    @staticmethod
    @profile
    def old_and_optimazed_second(words_by_one_line):
        # Исходные данные 100000 слов

        # При исходной версии - использование конкретенации строк
        # и использование цикла для печати в консоль -
        # программа использует 1.5 MiB RAM
        split_line_text_by_space(words_by_one_line)

        # В новой версии метода используется list comprehension
        # для split строки и фильтрации слов более 10 символов
        # программа использует 1.0 MiB RAM
        optimaze_task_2_second.split_line_text_by_space(words_by_one_line)

    @staticmethod
    @profile
    def old_and_optimazed_third():
        digit_for_tests =get_large_number()
        find_big_number_in_digit(digit_for_tests)
        optimaze_task_2_third.find_big_number_in_digit(digit_for_tests)



def get_random_word(max_letters):
    letters = string.ascii_letters
    word = "".join(random.sample(letters, random.randrange(max_letters)))
    return word
def get_large_number():

    list_types_digits=list(string.digits)
    large_dig=str(random.choice(string.digits))
    for i in range(35):
        random.shuffle(list_types_digits)
        large_dig=f"{large_dig}" \
                  f"{''.join(list_types_digits)}" \
                  f"{large_dig[len(large_dig)//2:len(large_dig)]}"

    return large_dig



if __name__ == '__main__':
    # TestClass.test_first(1000000)
    # #     результат  2.0 MiB  потрачено на функцию

    # TestClass.optimaze_first(100)
    # TestClass.optimaze_first(1000000)

    # 2
    # random_words_list = [get_random_word(max_letters=10) for i in range(1, 100000)]
    # words_one_line = " ".join(random_words_list)
    # TestClass.old_and_optimazed_second(words_one_line)


    TestClass.old_and_optimazed_third()

#     TestClass.list_digits = [randrange(100) for i in range(1, 100000)]
#     statements = ['TestClass.test_first(TestClass.list_digits)']
#     print( f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# #     результат 7.180608901999676
#
#     statements = ['TestClass.optimaze_first(TestClass.list_digits)']
#     print(f'{statements[0]}, {min(repeat(statements[0], setup, default_timer, 3, 100))}')
# #     результат 0.0720014909998099
