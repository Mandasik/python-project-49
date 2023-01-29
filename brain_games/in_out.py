import prompt


def in_o(question, corr, moniker, flag=True):  # flag=True - сигнал
    # о продолжении игры
    if not flag:  # оповещает данную функцию о том, что игра завершилась
        print(f'Congratulations, {moniker}!')
        return False
    print(f'Question: {question}')
    ans = prompt.string('Your answer: ')
    if corr == ans:
        print('Correct!')
        return True  # оповещает игру о правильном ответе
    else:
        print(f'''"{ans}" is wrong answer ;(. Correct answer was "{corr}".
Let's try again, {moniker}!
               ''')
        return False  # оповещает игру об ошибочном ответе
