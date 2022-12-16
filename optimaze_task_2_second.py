# 4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


def split_line_text_by_space(inputed):
    max_characters_in_word = 10

    list_words = [i[0:max_characters_in_word] for i in inputed.split(" ") if
                  len(i)>0]

    for i in range(0,len(list_words)) :
        print(f"{i} {list_words[i]}")


if __name__ == '__main__':
    print("Input several words by space character separator")
    inputed = input()
    split_line_text_by_space(inputed)
