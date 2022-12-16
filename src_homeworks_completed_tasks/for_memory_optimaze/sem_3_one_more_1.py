# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randrange


def sum_odd_digits(count_digits):
    list_numbers = []
    for i in range(1, count_digits):
        list_numbers.append(randrange(100))

    sum_result = 0
    iterator = 0
    for dig in list_numbers:
        if not iterator % 2 == 0:
            sum_result = sum_result + dig
        iterator += 1
    return sum_result


if __name__ == '__main__':
    print(f"Result {sum_odd_digits(100)}")
