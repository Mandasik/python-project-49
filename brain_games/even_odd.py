import random
import prompt


def correct():  # Генерирует случайное число и определяет правильный ответ
    question = random.randint(-9999999, 9999999)
    if question % 2 == 0:
        corr = 'yes'
    else:
        corr = 'no'
    return question, corr


def game1(moniker):  # Модуль с игрой четное-нечётное
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question, corr = correct()
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        if ans == corr:
            print('Correct!')
            i += 1
        else:
            print(f'''"{ans}" is wrong answer ;(. Correct answer was "{corr}".
Let's try again, {moniker}!
                  ''')
            break
    else:
        print(f'Congratulations, {moniker}!')
