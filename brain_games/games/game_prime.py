#!/usr/bin/env python3
import random


about = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Условие:
# Простые числа — это числа, которые делятся только на себя и на 1.
# Все остальные числа называются составными числами.


def choice_game():
    number = random.randint(2, 1000)  # генерируем число
    list_x = []
    for x in range(2, int(number ** 0.5 + 1)):
        list_x.append(x)  # создаем список от 2 до 1000
    # ниже, в цикле перебираем каждый элемент списка и сравниваем
    # остаток от деления
        if number % x == 0:
            return number, 'no'
            # если выполнилось  условие, возвращаем число и
            # его значение в виде строки
# проверяем все делители, если не прошли условие, то возвращаем число
# и ответ, что число простое
    return number, 'yes'

# print(choice_game())


""" import random

about = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def choice_game():
    number = random.randint(2, 1000)  # генерируем число
# в цикле перебираем каждый элемент списка и сравниваем number с ним
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:  # проверка на наличие остатка
            return number, 'no'
        return number, 'yes'
        # вернули "да", когда проверили все i и не нашли делителей
print(choice_game())"""
