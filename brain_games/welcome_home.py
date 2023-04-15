import prompt


def welcome_name(games):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(games.ABOUT)
    count = 0
    while count < 3:
        number, game_answer = games.choice_game()
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if game_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f" Correct answer was '{game_answer}'. "
                f"\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
