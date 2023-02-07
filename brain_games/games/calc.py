import operator
import random


MIN = -99
MAX = 99
RULES = 'What is the result of the expression?'
COMPARISON = {operator.add: '+', operator.mul: '*', operator.sub: '-'}


def performs_arithmetic_operations():
    numeric_a = random.randint(MIN, MAX)
    numeric_b = random.randint(MIN, MAX)
    act = random.choice(list(COMPARISON.keys()))
    return numeric_a, numeric_b, act


def gives_answer_question():
    numeric_a, numeric_b, act = performs_arithmetic_operations()
    question = f'{numeric_a} {COMPARISON[act]} {numeric_b}'
    answer = str(act(numeric_a, numeric_b))
    return question, answer
