import secrets


MAX = 999999999999
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def checks_even_odd():  # Проверяет чётное ли число
    numeric = secrets.randbelow(MAX)
    if numeric % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return numeric, answer


def gives_answer_question():
    question, answer = checks_even_odd()
    return question, answer
