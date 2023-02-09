import operator
import random


MIN = -99
MAX = 99
RULES = 'What is the result of the expression?'


def performs_arithmetic_operations():
    comparison = {operator.add: '+', operator.mul: '*', operator.sub: '-'}
    numeric_a = random.randint(MIN, MAX)
    numeric_b = random.randint(MIN, MAX)
    act = random.choice(list(comparison.keys()))
    simbol = comparison[act]
    answer = act(numeric_a, numeric_b)
    return numeric_a, numeric_b, simbol, answer


def gives_answer_question():
    numeric_a, numeric_b, simbol, answer = performs_arithmetic_operations()
    question = f'{numeric_a} {simbol} {numeric_b}'
    answer = str(answer)
    return question, answer
