import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    correct_answers = 0
    while correct_answers < 3:
        task_question, correct_answer = game.task()
        print(f'Question: {task_question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
