from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_task_arguments():
    # 1, не является простым числом, игнорируется
    number = randint(2, 100)
    # проверка числа на простоту, 1 игнорируется
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            correct_answer = "no"
            break
        else:
            correct_answer = "yes"
    task_question = number
    # передача значений в модуль логики игры
    return task_question, correct_answer
