from brain_games import in_out
import random


def game4(moniker):  # Логика игры Прогрессия
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        wave = random.randint(-8, 8)  # шаг прогрессии
        start = random.randint(-99, 99)  # стартовое число
        position = random.randint(0, 10)  # спрятанная позиция
        progr = []
        for j in range(10):  # генерация прогрессии
            progr.append(str(start))
            start += wave
        corr = progr[position]
        progr[position] = '..'
        question = ' '.join(progr)
        pointer = in_out.in_o(question, corr, moniker)  # Вызов функции
# взаимодействия с пользователем
        if pointer:
            i += 1
        else:
            break
    else:
        in_out.in_o(question, corr, moniker, flag=False)
