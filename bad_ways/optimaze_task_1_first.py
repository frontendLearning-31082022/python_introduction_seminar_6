# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math
from functools import reduce


def n_multipl(dig):
    listtt = []

    mygenerator = createGenerator()
    for i in mygenerator:
        listtt.append(i)
        if i==dig:
            break
    return listtt

def createGenerator() :
        iter=1
        res=1
        while True:
            res=res*iter
            iter=iter+1
            yield res

if __name__ == '__main__':
    # dig = console_methods.input_digit(True)
    dig = 12
    list_result = n_multipl(dig)
    print(f"Result digits {list_result}")
