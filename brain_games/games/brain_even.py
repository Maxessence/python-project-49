from random import randint

def is_even(number):
    return number % 2 == 0

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    task_question = randint(1, 100)
    correct_answer = 'yes' if is_even(task_question) else 'no'
    return task_question, correct_answer
