import operator
import random
from brain_games import in_out


def game2(moniker):  # Логика игры калькулятор
    print('What is the result of the expression?')
    oper = [operator.add, operator.mul, operator.sub]
    comparison = {operator.add: '+', operator.mul: '*', operator.sub: '-'}
    i = 0
    while i < 3:
        a = random.randint(-99, 99)
        b = random.randint(-99, 99)
        act = random.choice(oper)
        question = f'{a} {comparison[act]} {b}'
        corr = str(act(a, b))
        pointer = in_out.in_o(question, corr, moniker)  # Вызов функции
# взаимодействия с пользователем
        if pointer:
            i += 1
        else:
            break
    else:
        in_out.in_o(question, corr, moniker, flag=False)
