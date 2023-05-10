from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return "no"
    return "yes"


def get_task_arguments():
    number = randint(2, 100)
    task_question = number
    correct_answer = is_prime(number)
    return task_question, correct_answer
