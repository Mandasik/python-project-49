import prompt
from brain_games import cli


def in_o(game):  # Движок Brain-games
    moniker = cli.welcome_user()
    print(game.RULES)
    for i in range(3):
        question, corr = game.logics()  # Вызов функции игры
        print(f'Question: {question}')
        ans = prompt.string('Your answer: ')
        if ans == corr:  # Проверка ответа пользователя
            print('Correct!')
        else:
            print(f'''"{ans}" is wrong answer ;(. Correct answer was "{corr}".
Let's try again, {moniker}!''')
            break
    else:
        print(f'Congratulations, {moniker}!')
