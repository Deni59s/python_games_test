#!/usr/bin/env python3
from random import randint

import prompt


def main():
    generate()  # вызов фунции с запросом имени из дир-ии brain_games/


if __name__ == '__main__':
    main()


answer = ''
lst = []


def generate():
    name = prompt.string('May I have your name? ')
    number = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for x in range(3):
        lst.append(randint(1, 1000))
    for random_number in lst:
        print('Question:', random_number)
        answer = prompt.string('Your answer:')
        if (random_number % 2 == 0 and answer == 'yes') or \
           (random_number % 2 != 0 and answer == 'no'):
            print('Correct!')
            number = number + 1
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            number = number + 1
        else:
            print(
                "'yes' is wrong answer ;(."
                "Correct answer was 'no'.\n"
                f"Let's try again, {name}!")
            return
    if number == 3:
        print(f'Congratulations, {name}!')
    else:
        return None
