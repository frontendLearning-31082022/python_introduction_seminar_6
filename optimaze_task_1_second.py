import random


def shuffle_list(len_list):
    list_shuffle = []

    for value in range(1, len_list):
        list_shuffle.append(value)

    random.shuffle(list_shuffle)

    return list_shuffle