import prompt


def in_o(greetings, game, rules):  # Движок Brain-games
    moniker = greetings()
    print(rules)
    for i in range(3):
        question, corr = game()  # Вызов функции игры
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
