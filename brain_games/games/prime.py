import random
from brain_games import in_out


def list_simple():  # форммирует список простых чисел
    l_simple = [x for x in range(2, 3000)]
    for i in l_simple:
        for elem in l_simple[l_simple.index(i) + 1:]:
            if elem % i == 0:
                l_simple.remove(elem)
    return l_simple


def game5(moniker):  # Логика игры определить простое число
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    scroll = list_simple()
    i = 0
    while i < 3:
        question = str(random.randint(1, 3000))
        if question in scroll:
            corr = 'yes'
        else:
            corr = 'no'
        pointer = in_out.in_o(question, corr, moniker)  # Вызов функции
# взаимодействия с пользователем
        if pointer:
            i += 1
        else:
            break
    else:
        in_out.in_o(question, corr, moniker, flag=False)
