# Реализуйте алгоритм перемешивания списка.
import random


def shuffle_list(len_list):
    list_shuffle = []

    for value in range(1, len_list):
        list_shuffle.append(value)

    for value in list_shuffle:
        random_pos = random.randint(0, len(list_shuffle) - 1)
        temp_val = value
        value = list_shuffle[random_pos]
        list_shuffle[random_pos] = temp_val
    return list_shuffle


if __name__ == '__main__':
    print(shuffle_list(100))
