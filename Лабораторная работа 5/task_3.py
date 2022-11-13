from random import randint


def get_unique_list_numbers() -> list[int]:
    min_ = -10
    max_ = 10
    width = 15
    list_ = []
    while len(set(list_)) != width:
        num = randint(max_, min_)
        if num not in list_:
            list_.append(num)
    return list(set(list_))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
