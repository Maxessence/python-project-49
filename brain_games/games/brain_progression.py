from random import randint


RULES = 'What number is missing in the progression?'


def get_task_arguments():
    # первый член арифметической прогрессии, в результате не отображается
    start = randint(1, 10)
    # разность арифметической прогрессии
    step = randint(5, 10)
    # рандомная длина арифметической прогрессии
    lenght = randint(5, 10)
    arithmetic_progression = []
    for i in range(lenght):
        next_step = start + step
        step = next_step
        arithmetic_progression.append(next_step)
    # создается рандомный индекс по которому будет происходит замена значения
    random_index = randint(0, len(arithmetic_progression) - 1)
    correct_answer = str(arithmetic_progression[random_index])
    # замена рандомного значения для сокрытия числа, которое нужно отгадать
    arithmetic_progression[random_index] = ".."
    # перевод списка в строку (join работает только с str)
    task_question = " ".join(map(str, arithmetic_progression))
    # передача значений в модуль логики игры
    return task_question, correct_answer
