import random
import math


MIN = 1
MAX = 1000
RULE = 'Find the greatest common divisor of given numbers.'


def finds_gcd(numeric_a, numeric_b):  # Находит наибольший делитель
    answer = math.gcd(numeric_a, numeric_b)
    return answer


def gives_answer_question():
    numeric_a = random.randint(MIN, MAX)
    numeric_b = random.randint(MIN, MAX)
    answer = finds_gcd(numeric_a, numeric_b)
    question = f'{numeric_a} {numeric_b}'
    return question, str(answer)
