from random import randint


MIN = -99999999999
MAX = 999999999999
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def gives_answer_question():
    question = randint(MIN, MAX)
    answer = 'yes' if is_even(question) else 'no'
    return str(question), answer
