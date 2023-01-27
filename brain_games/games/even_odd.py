import random
from brain_games import in_out


def game1(moniker):  # Логика игры четное-нечётное
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question = random.randint(-9999999, 9999999)
        if question % 2 == 0:
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
