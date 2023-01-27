import prompt


def in_o(question, corr, moniker, flag=True):
    if not flag:
        print(f'Congratulations, {moniker}!')
        return False
    print(f'Question: {question}')
    ans = prompt.string('Your answer: ')
    if corr == ans:
        print('Correct!')
        return True
    else:
        print(f'''"{ans}" is wrong answer ;(. Correct answer was "{corr}".
Let's try again, {moniker}!
               ''')
        return False
