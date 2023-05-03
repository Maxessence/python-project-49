from random import randint

RULES = "Find the greatest common divisor of given numbers."


def task():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    task_question = f"{number1} {number2}"
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    correct_answer = str(number1 + number2)
    return task_question, correct_answer
