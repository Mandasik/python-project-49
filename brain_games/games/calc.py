import operator
import random


MIN = -99
MAX = 99
RULE = 'What is the result of the expression?'
COMPARISON = {'+': operator.add, '*': operator.mul, '-': operator.sub}


def calculate(number_a, number_b, operation):
    answer = operation(number_a, number_b)
    return answer


def gives_answer_question():
    number_a = random.randint(MIN, MAX)
    number_b = random.randint(MIN, MAX)
    simbol = random.choice(list(COMPARISON.keys()))
    operation = COMPARISON[simbol]
    answer = str(calculate(number_a, number_b, operation))
    question = f'{number_a} {simbol} {number_b}'
    return question, answer
