import operator
import random


MIN = -99
MAX = 99
RULES = 'What is the result of the expression?'


def game2():  # Логика игры калькулятор
    comparison = {operator.add: '+', operator.mul: '*', operator.sub: '-'}
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    act = random.choice(list(comparison.keys()))
    question = f'{a} {comparison[act]} {b}'
    corr = str(act(a, b))
    return question, corr
