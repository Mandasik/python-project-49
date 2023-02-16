import operator
import random


MIN = -99
MAX = 99
RULE = 'What is the result of the expression?'
COMPARISON = {'+': operator.add, '*': operator.mul, '-': operator.sub}


def calculate(numeric_a, numeric_b, operation):
    answer = operation(numeric_a, numeric_b)
    return answer


def gives_answer_question():
    numeric_a = random.randint(MIN, MAX)
    numeric_b = random.randint(MIN, MAX)
    simbol = random.choice(list(COMPARISON.keys()))
    operation = COMPARISON[simbol]
    answer = str(calculate(numeric_a, numeric_b, operation))
    question = f'{numeric_a} {simbol} {numeric_b}'
    return question, answer
