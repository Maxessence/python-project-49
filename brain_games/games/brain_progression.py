from random import randint


RULES = 'What number is missing in the progression?'


def get_task_arguments():
    start = randint(1, 10)
    step = randint(5, 10)
    lenght = randint(5, 10)
    arithmetic_progression = []
    for i in range(lenght):
        next_step = start + step
        step = next_step
        arithmetic_progression.append(next_step)
    random_index = randint(0, len(arithmetic_progression) - 1)
    correct_answer = str(arithmetic_progression[random_index])
    arithmetic_progression[random_index] = ".."
    task_question = " ".join(map(str, arithmetic_progression))
    return task_question, correct_answer
