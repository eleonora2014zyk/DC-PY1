def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
str_dict_ = {}
def get_count_char(str_):
    str_ = "".join(str_.lower().split())
    for words_ in str_:
        if words_. isalpha() and words_ not in str_dict_:
            str_dict_[words_] = 1
        else:
            if words_.isalpha() and words_ in str_:
                str_dict_[words_] += 1
    return str_dict_

def new_dict_(str_dick_):
    sum_ = sum(str_dick_.values())
    for i in str_dict_:
        str_dict_[i] = round ((str_dick_[i]/sum_) * 100, 3)
    print(sum(str_dick_.values()))
    return str_dict_

print(get_count_char(main_str))
