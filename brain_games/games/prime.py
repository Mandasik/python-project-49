import random
import math


MIN = 1
MAX = 5000
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game5():  # Логика игры определить простое число
    question = random.randint(1, 5000)
    if question % 2 == 0:  # Проверка числа
        corr = 'no'
    else:
        for i in range(3, round(math.sqrt(question)), 2):
            if question % i == 0:
                corr = 'no'
                break
        else:
            corr = 'yes'
    return question, corr
