import random


MIN = -99
MAX = 99
RULE = 'What number is missing in the progression?'


def random_generation():
    hid_position = random.randint(0, 9)  # спрятанная позиция
    wave = random.randint(MIN, MAX)  # шаг прогрессии
    start = random.randint(MIN, MAX)  # стартовое число
    return hid_position, wave, start


def generates_progression():
    hid_position, wave, start = random_generation()
    progression = []
    for j in range(10):  # генерация прогрессии
        progression.append(str(start))
        start += wave
    return progression


def gives_answer_question():
    hid_position, wave, start = random_generation()
    progression = generates_progression()
    answer = progression[hid_position]  # определение ответа
    progression[hid_position] = '..'  # сокрытие позиции вопроса
    question = ' '.join(progression)
    return question, str(answer)
