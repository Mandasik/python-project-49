import random


MIN = -99
MAX = 99
RULES = 'What number is missing in the progression?'


def logics():  # Логика игры Прогрессия
    position = random.randint(0, 9)  # спрятанная позиция
    progr = []
    wave = random.randint(MIN, MAX)  # шаг прогрессии
    start = random.randint(MIN, MAX)  # стартовое число
    for j in range(10):
        progr.append(str(start))
        start += wave
    corr = progr[position]
    progr[position] = '..'
    question = ' '.join(progr)
    return question, corr
