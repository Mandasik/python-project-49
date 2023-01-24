import prompt

def welcome_user():
    moniker = prompt.string('May I have your name? ')
    print(f'Hello, {moniker}!')
