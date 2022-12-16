# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def n_multipl(dig):
    list_result = [1]
    for i in range(1, dig):
        list_result.append(list_result[i - 1] * (i + 1))
        i += 1
    return list_result

if __name__ == '__main__':
    # dig = console_methods.input_digit(True)
    dig=5
    list_result=n_multipl(dig)
    print(f"Result digits {list_result}")
