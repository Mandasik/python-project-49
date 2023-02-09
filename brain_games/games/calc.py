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
    simbol = COMPARISON[act]
    answer = act(numeric_a, numeric_b)
    return numeric_a, numeric_b, simbol, answer


def gives_answer_question():
    numeric_a, numeric_b, simbol, answer = performs_arithmetic_operations()
    question = f'{numeric_a} {simbol} {numeric_b}'
    answer = str(answer)
    return question, answer
