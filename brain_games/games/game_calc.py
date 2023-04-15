#!/usr/bin/env python3
import random


ABOUT = 'What is the result of the expression?'


def choice_game():
    lst_number = [random.randint(1, 100) for i in range(2)]
    lst_sign = random.choice(['+', '-', '*'])
    if lst_sign == '+':
        game_answer = lst_number[0] + lst_number[1]
    elif lst_sign == '-':
        game_answer = lst_number[0] - lst_number[1]
    elif lst_sign == '*':
        game_answer = lst_number[0] * lst_number[1]
    number = f'{lst_number[0]}{lst_sign}{lst_number[1]}'
    return number, str(game_answer)

#  print(choice_game())
