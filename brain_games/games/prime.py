import random
from math import sqrt, ceil


MIN = -100
MAX = 100000000
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1 or number != 2 and number % 2 == 0 \
            or number != 3 and number % 3 == 0:
        return False
    potentially_prime = (
        divider for divider in range(4, ceil(sqrt(number)))
        if divider % 2 != 0 or divider % 3 != 0)
    for i in potentially_prime:
        if number % i == 0:
            return False
    return True


def gives_answer_question():
    question = random.randint(MIN, MAX)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
