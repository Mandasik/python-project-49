import secrets


MAX = 999999999999
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def checks_even_odd():  # Проверяет чётное ли число
    numeric = secrets.randbelow(MAX)
    return numeric, numeric % 2 == 0


def gives_answer_question():
    question, answer = checks_even_odd()
    return question, 'yes' if answer else 'no'
