import random
import math


MIN = 1
MAX = 1000
RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(number_a, number_b):
    answer = math.gcd(number_a, number_b)
    return answer


def gives_answer_question():
    number_a = random.randint(MIN, MAX)
    number_b = random.randint(MIN, MAX)
    answer = str(find_gcd(number_a, number_b))
    question = f'{number_a} {number_b}'
    return question, answer
