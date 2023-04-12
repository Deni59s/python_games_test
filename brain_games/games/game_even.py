from random import randint
# import prompt

about = 'Answer "yes" if the number is even, otherwise answer "no".'


""" def do_check(x):
    return 'yes' if x % 2 == 0 else 'no'

def generation():
    x_question = randint(1, 1000) # генерирует число от 1 до 1000
    number =str(x_question)
    game_answer = do_check(x_question)
    return number, game_answer """


def choice_game():  # функция
    x_question = randint(1, 1000)  # генерирует число от 1 до 1000
    number = str(x_question)
    if x_question % 2 == 0:  # если четное и ответ "да"
        return number, 'yes'
    elif x_question % 2 != 0:  # если нечетное и ответ "нет"
        return number, 'no'
    else:
        return number

    # return number. game_answer
