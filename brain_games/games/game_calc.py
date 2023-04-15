#!/usr/bin/env python3
from random import randint, choice
from operator import add, sub, mul


ABOUT = 'What is the result of the expression?'


def choice_game():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operator = choice('-+*')

    if operator == '+':
        result = add(number_1, number_2)
    elif operator == '-':
        result = sub(number_1, number_2)
    elif operator == '*':
        result = mul(number_1, number_2)

    question = '{} {} {}'.format(number_1, operator, number_2)
    correct_answer = str(result)

    return question, correct_answer


""" def choice_game():
    lst_number = [random.randint(1, 100) for i in range(2)]
    lst_sign = random.choice(['+', '-', '*'])
    if lst_sign == '+':
        game_answer = lst_number[0] + lst_number[1]
    elif lst_sign == '-':
        game_answer = lst_number[0] - lst_number[1]
    elif lst_sign == '*':
        game_answer = lst_number[0] * lst_number[1]
    number = '{} {} {}'.format(number1, symbol, number2)
    #number = f'{lst_number[0]}{lst_sign}{lst_number[1]}'
    return number, str(game_answer)

print(choice_game())"""
