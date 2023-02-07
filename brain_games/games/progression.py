import random


MIN = -99
MAX = 99
RULES = 'What number is missing in the progression?'


def generates_progression():
    position = random.randint(0, 9)  # спрятанная позиция
    progr = []
    wave = random.randint(MIN, MAX)  # шаг прогрессии
    start = random.randint(MIN, MAX)  # стартовое число
    for j in range(10):
        progr.append(str(start))
        start += wave
    progr[position] = '..'
    return progr, progr[position]


def gives_answer_question():
    progr, answer = generates_progression()
    question = ' '.join(progr)
    return question, answer
