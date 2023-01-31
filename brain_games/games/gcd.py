import random
import math


MIN = 1
MAX = 1000
RULES = 'Find the greatest common divisor of given numbers.'


def game3():  # Логика игры НОД
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    question = f'{a} {b}'
    corr = str(math.gcd(a, b))
    return question, corr
