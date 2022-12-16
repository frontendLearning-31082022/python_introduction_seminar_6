# 4) Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def find_big_number_in_digit(digit):
    uniq_digits=set(digit)
    max_num = max(uniq_digits)

    return max_num

def run():
    # int_positive = int(main.input_int(True))
    int_positive=6

    max_num=find_big_number_in_digit(int_positive)
    print("Max value in inputed number " + str(max_num))
