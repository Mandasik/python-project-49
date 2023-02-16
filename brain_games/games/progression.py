import random


MIN = -99
MAX = 99
PROGRESSION_LENGTH = 10
RULE = 'What number is missing in the progression?'


def generates_progression(start, finish, step):
    progression = [str(number) for number in range(start, finish, step)]
    return progression


def gives_answer_question():
    hidden_position = random.randint(0, PROGRESSION_LENGTH - 1)
    step = random.randint(MIN, MAX)
    step = 1 if step == 0 else step
    start = random.randint(MIN, MAX)
    finish = start + step * PROGRESSION_LENGTH
    progression = generates_progression(start, finish, step)
    answer = progression[hidden_position]
    progression[hidden_position] = '..'
    question = ' '.join(progression)
    return question, answer
