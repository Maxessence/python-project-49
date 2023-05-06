import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)  # импортирование правил игры
    # успешное окончание игры - три правильный ответа, остановка - один неверный
    for _ in range(3):
        # импортирование аргументов игры
        task_question, correct_answer = game.get_task_arguments()
        print(f'Question: {task_question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.\n"
              f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")
  
        
