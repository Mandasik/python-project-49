from random import randint


MIN = -99999999999
MAX = 999999999999
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def checks_even_odd(number):
    return number % 2 == 0


def gives_answer_question():
    question = randint(MIN, MAX)
    answer = checks_even_odd(question)
    return question, 'yes' if answer else 'no'
