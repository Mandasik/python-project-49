import random
import math
from brain_games import in_out


def is_simple(question):  # Проверка числа
    if question % 2 == 0:
        return 'no'
    for i in range(3, round(math.sqrt(question)), 2):
        if question % i == 0:
            return 'no'
    return 'yes'


def game5(moniker):  # Логика игры определить простое число
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        question = random.randint(1, 5000)
        corr = is_simple(question)
        pointer = in_out.in_o(str(question), corr, moniker)  # Вызов функции
# взаимодействия с пользователем
        if not pointer:
            break
    else:
        in_out.in_o(question, corr, moniker, flag=False)
