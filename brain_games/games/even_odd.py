import secrets


MAX = 999999999999
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def checks_even_odd(numeric):  # Проверяет чётное ли число
    return numeric, numeric % 2 == 0


def gives_answer_question():
    numeric = secrets.randbelow(MAX)
    question, answer = checks_even_odd(numeric)
    return question, 'yes' if answer else 'no'
