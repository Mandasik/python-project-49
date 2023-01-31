import secrets


MAX = 999999999999
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game1():  # Логика игры четное-нечётное
    question = secrets.randbelow(MAX)
    if question % 2 == 0:
        corr = 'yes'
    else:
        corr = 'no'
    return question, corr
