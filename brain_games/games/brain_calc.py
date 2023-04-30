import random
from operator import add, sub, mul

operators = {"+": add, "-": sub, "*": mul}
keys = list(operators)

RULES = 'What is the result of the expression?'

def task():
   number1 = random.randint(1, 20)
   number2 = random.randint(1, 20)
   operator = random.choice(keys)
   task_question = "{} {} {}".format(number1,operator, number2)
   correct_answer = str(operators[operator](number1, number2))
   return task_question, correct_answer