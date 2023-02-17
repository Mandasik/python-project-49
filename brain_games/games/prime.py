import random
from math import sqrt, ceil


MIN = -100
MAX = 4000
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0 or number % 3 == 0 or number <= 1:
        return False
    for i in (divider for divider in range(3, ceil(sqrt(number)), 2)):
        if number % i == 0:
            return False
    return True


def gives_answer_question():
    question = random.randint(MIN, MAX)
    answer = 'yes' if question == 2 or is_prime(question) else 'no'
    return str(question), answer
