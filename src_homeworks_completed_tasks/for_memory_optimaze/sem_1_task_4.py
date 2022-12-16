# 4) Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def find_big_number_in_digit(digit):
    array_digits = list(digit)

    iter = len(array_digits) - 1
    max_num = int(array_digits[iter])

    while (iter > -1):
        dig_current = array_digits[iter]
        if int(dig_current) > max_num:
            max_num = int(dig_current)
        iter -= 1

    return max_num


def run():
    # int_positive = int(main.input_int(True))
    int_positive = 6

    max_num = find_big_number_in_digit(int_positive)
    print("Max value in inputed number " + str(max_num))
