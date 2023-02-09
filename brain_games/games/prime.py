import random
import math


MIN = 1
MAX = 5000
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simply(question):  # Проверка числа
    if question % 2 == 0:
        return False
    for i in range(3, round(math.sqrt(question)), 2):
        if question % i == 0:
            return False
    return True


def gives_answer_question():
    question = random.randint(MIN, MAX)
    return str(question), 'yes' if is_simply else 'no'
