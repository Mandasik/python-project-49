import prompt


NUMBER_OF_ROUNDS = 3


def calls_game(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.RULE)
    for i in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.gives_answer_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"\"{user_answer}\" is wrong answer ;(. Correct answer was\n"
                  f"\"{correct_answer}\". Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
