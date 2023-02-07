import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    moniker = prompt.string('May I have your name? ')
    print(f'Hello, {moniker}!')
    return moniker


def game_engine(game):  # Движок Brain-games
    moniker = welcome_user()
    print(game.RULES)
    for i in range(3):
        question, correct_answer = game.gives_answer_question()  # модуль игры
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')  # Запрос ответа
        if user_answer == correct_answer:  # Проверка ответа пользователя
            print('Correct!')
        else:
            print(f'''"{user_answer}" is wrong answer ;(. Correct answer was
 "{correct_answer}". Let's try again, {moniker}!''')
            break
    else:
        print(f'Congratulations, {moniker}!')
