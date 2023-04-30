from random import randint
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def game_is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        correct_answer = 'yes' if is_even(number) else 'no'
        if answer == correct_answer:
            print('Correct!')
            correct_answers = correct_answers + 1
        else:
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
