import random


MIN = -99
MAX = 99
RULES = 'What number is missing in the progression?'


def generates_progression():
    position = random.randint(0, 9)  # спрятанная позиция
    progression = []
    wave = random.randint(MIN, MAX)  # шаг прогрессии
    start = random.randint(MIN, MAX)  # стартовое число
    for j in range(10):  # генерация прогрессии
        progression.append(str(start))
        start += wave
    answer = progression[position]  # определение ответа
    progression[position] = '..'  # сокрытие позиции вопроса
    return progression, answer


def gives_answer_question():
    progression, answer = generates_progression()
    question = ' '.join(progression)
    return question, str(answer)
