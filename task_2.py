# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта,
# сделать замеры памяти, оптимизировать, вновь выполнить замеры
# и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

# Описания нужно делать в виде docstrings

from memory_profiler import profile
import random
import string

from src_homeworks_completed_tasks.for_memory_optimaze.sem_3_one_more_1 \
    import sum_odd_digits as ram_big_ver_sum_odd_digits
from optimaze_task_2_first \
    import sum_odd_digits as ram_new_ver_sum_odd_digits

from src_homeworks_completed_tasks.for_memory_optimaze.sem_2_task_4 \
    import split_line_text_by_space as ram_big_ver_split_line
from optimaze_task_2_second \
    import split_line_text_by_space as ram_new_ver_split_line

from src_homeworks_completed_tasks.for_memory_optimaze.sem_1_task_4 \
    import find_big_number_in_digit as ram_big_ver_find_big_number_in_digit
from optimaze_task_2_third \
    import find_big_number_in_digit as ram_new_ver_find_big_number_in_digit


class TestClass:
    @staticmethod
    @profile
    def old_and_optimazed_first():
        count_digits = 100000

        """Формирования списка с помощью list.append 
            и накапливание суммы элементов на нечетной позиции
            в цикле. 
            """
        sum_result = ram_big_ver_sum_odd_digits(count_digits)
        """Затраты памяти 0.9 MiB для 100000 цифр"""

        """В новой версии использование генератора для формирования 
        необходимой совокупности чисел"""
        sum_result = ram_new_ver_sum_odd_digits(count_digits)
        """В новой версии Затраты памяти 0.0 MiB для 100000 цифр"""

    @staticmethod
    @profile
    def old_and_optimazed_second():
        random_words_list = [get_random_word(max_letters=10) for i
                             in range(1, 100000)]
        words_one_line = " ".join(random_words_list)

        """Вводится строка из слов, необходимо разделить их по пробелу.
        Пронумеровать слова, ограничить длину если больше 10 
        и вывести в консоль списком. Исходные данные 100000 слов"""

        """В старой версии - используется конкретенации строк
         и используется цикл для печати в консоль"""
        ram_big_ver_split_line(words_one_line)
        """Программа использует 1.5 MiB RAM"""

        """В новой версии метода используется list comprehension
        для split строки и фильтрации слов более 10 символов,
        а также f строки для печати в консоль"""
        ram_new_ver_split_line(words_one_line)
        """Программа использует 1.0 MiB RAM"""

    @staticmethod
    @profile
    def old_and_optimazed_third():
        digit_for_tests = get_large_number()

        """Число делится на цифры, необходимо найти наибольшую"""

        """В первой версии производится разбивка числа на массив цифр,
            который хранится в RAM во время выполнения, 
            далее итеративно ищется большее число
            """
        ram_big_ver_find_big_number_in_digit(digit_for_tests)
        """Результат использования RAM 0.1 MiB для числа 
        длиной 31151566 цифр"""

        """Во втором случае число преобразуется в список уникальных
        цифр с помощью структуры set и занимает гораздо меньший объем RAM"""
        ram_new_ver_find_big_number_in_digit(digit_for_tests)
        """Результат использования RAM 0.0 MiB для числа 
        длиной 31151566 цифр"""


def get_random_word(max_letters):
    letters = string.ascii_letters
    word = "".join(random.sample(letters, random.randrange(max_letters)))
    return word


def get_large_number():
    list_types_digits = list(string.digits)
    large_dig = str(random.choice(string.digits))
    for i in range(35):
        random.shuffle(list_types_digits)
        large_dig = f"{large_dig}" \
                    f"{''.join(list_types_digits)}" \
                    f"{large_dig[len(large_dig) // 2:len(large_dig)]}"

    return large_dig


if __name__ == '__main__':
    TestClass.old_and_optimazed_first()
    TestClass.old_and_optimazed_second()
    TestClass.old_and_optimazed_third()
