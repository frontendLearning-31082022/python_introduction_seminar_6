# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randrange


def sum_odd_digits(count_digits):
    generator_not_even = (randrange(100) for i in range(1, count_digits) if
                    i % 2 != 0)

    listt=list(generator_not_even)
    return sum(listt)


if __name__ == '__main__':
    print(f"Result {sum_odd_digits(100)}")
