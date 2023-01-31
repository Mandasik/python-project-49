import random
import math


MIN = 1
MAX = 5000
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simply(question):  # Проверка числа
    if question % 2 == 0:
        return 'no'
    for i in range(3, round(math.sqrt(question)), 2):
        if question % i == 0:
            return 'no'
    return 'yes'


def game5():  # Логика игры определить простое число
    question = random.randint(MIN, MAX)
    corr = is_simply(question)
    return question, corr
