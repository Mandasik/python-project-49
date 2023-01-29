import random
from brain_games import in_out


def is_even(question):
    if question % 2 == 0:
        corr = 'yes'
    else:
        corr = 'no'
    return corr


def game1(moniker):  # Логика игры четное-нечётное
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        question = random.randint(-9999999, 9999999)
        corr = is_even(question)
        pointer = in_out.in_o(str(question), corr, moniker)  # Вызов функции
# взаимодействия с пользователем
        if not pointer:
            break
    else:
        in_out.in_o(question, corr, moniker, flag=False)
