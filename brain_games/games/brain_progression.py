from random import randint


RULES = 'What number is missing in the progression?'


def task():
    start = randint(1, 10)
    step = randint(5, 10)
    lenght = randint(5, 10)
    Arithmetic_progression = []
    for i in range(lenght):
        next_step = start + step
        step = next_step
        Arithmetic_progression.append(next_step)
    RandomIndex = randint(0, len(Arithmetic_progression) - 1)
    correct_answer = str(Arithmetic_progression[RandomIndex])
    Arithmetic_progression[RandomIndex] = ".."
    task_question = " ".join(map(str, Arithmetic_progression))
    return task_question, correct_answer
