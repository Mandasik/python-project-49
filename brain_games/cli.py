import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    moniker = prompt.string('May I have your name? ')
    print(f'Hello, {moniker}!')
    return moniker
