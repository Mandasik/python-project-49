import random


MIN = -100
MAX = 100
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in (divider for divider in range(2, number)):
        if number % i == 0:
            return False
    return True


def gives_answer_question():
    question = random.randint(MIN, MAX)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer
