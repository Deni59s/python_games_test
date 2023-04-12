#!/usr/bin/env python3
import random


about = 'Find the greatest common divisor of given numbers.'


def choice_game():
    number = [random.randint(1, 100) for i in range(2)]
    #  генерирует список чисел от 1 до 100
    a = number[0]  # для задачи
    b = number[1]  # для задачи
    # a = 26  # для нахождения решения
    # b = 61  # для нахождения решения
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    # return str(a + b)  # если выполняется цикл, одна из переменных равна 0
    return (f'{str(number[0])} {str(number[1])}'), str(a + b)


#  print(choice_game())
