from brain_games import in_out
import random
import math


def game3(moniker):  # Логика игры НОД
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        question = f'{a} {b}'
        corr = str(math.gcd(a, b))
        pointer = in_out.in_o(question, corr, moniker)  # Вызов функции
# взаимодействия с пользователем
        if not pointer:
            break
    else:
        in_out.in_o(question, corr, moniker, flag=False)
