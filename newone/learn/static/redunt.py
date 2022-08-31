##
# This is a Python program that will generate randomised questions
# on various topics relating to maths.
# 26/5/2022
#
# By Ziggy Reddit

import random
from dataclasses import dataclass

@dataclass
class answ_e():
    number_1: int
    number_2: int
    x_num_1: int
    x_num_2: int
    # operation_1: str
    # operation_2: str

    def equation(self)-> str:

        # self.equation = f"({self.x_num_1}x{self.operation_1}{self.number_1})({self.x_num_2}x{self.operation_2}{self.number_2})"
        if self.number_1 > 0:
            a = f"({self.x_num_1}x+{self.number_1})"
        else:
            a = f"({self.x_num_1}x{self.number_1})"
        if self.number_2 > 0:
            b = f"({self.x_num_2}x+{self.number_2})"
        else:
            b = f"({self.x_num_2}x{self.number_2})"
        self.equation = f"{a}{b}"

    def answer(self)-> str:

        if self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1 > 0:
            p_2 = f"+{self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1}"
        else:
            p_2 = f"{self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1}"

        if self.number_1 * self.number_2 > 0:
            p_3 = f"+{self.number_1 * self.number_2}"
        else:
            p_3 = str(self.number_1 * self.number_2)

        x_num = self.x_num_1 * self.x_num_2
        if x_num != 1 and x_num != 0:
            self.answer = f"{x_num}x²{p_2}x{p_3}"
        elif x_num != 0:
            self.answer = f"x²{p_2}x{p_3}"
        else:
            self.answer = f"{p_2}x{p_3}"
        # if self.operation_1 == '-':
        #     self.number_1 *= -1
        # if self.operation_2 == '-':
        #     self.number_2 *= -1

        # if self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1!= 0:
        #     if self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1 < 0:
        #         ans_p1 = str(self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1) + 'x'
        #     else:
        #         ans_p1 = '+' + str(self.number_1 * self.x_num_2 + self.number_2 * self.x_num_1) + 'x'
        # else: ans_p1 = ''

        # if self.number_1 * self.number_2 != 0:
        #     if self.number_1 * self.number_2 < 0:
        #         ans_p2 = str(self.number_1 * self.number_2)
        #     else:
        #         ans_p2 = '+' + str(self.number_1 * self.number_2)
        # else: ans_p2 = ''
        # x_num = self.x_num_1 * self.x_num_2
        # self.answer = f"{x_num}x²{ans_p1}{ans_p2}"

    # def equation(self):
    #     self.equation = f"(x {self.operation_1} {self.number_1})(x {self.operation_2} {self.number_2})"
    #     print(f"(x {self.operation_1} {self.number_1})(x {self.operation_2} {self.number_2})")



def basic_equations(): #number):
    """Function that provides a question and answer with random numbers,
    and returns them both."""

    question_string = ''
    question = ''
    number_list = []
    added = False
    # For chaning amount of numbers to use.
    # if number > 2:
    #     for i in range(0, number):
    #         number_list.append(random.randint(1, 10))
    # else:
    #     number_list.append(random.randint(1, 10))
    #     number_list.append(random.randint(1, 10))

    # Uses default 3 numbers for basic operations.
    for i in range(0, 2):
        number_list.append(random.randint(1, 10))

    # Makes an equation without spaces and an equation that will be displayed to users.
    for values in number_list:
        add_mult = random.choice(['add', 'mult'])
        question_string += str(values)
        question += str(values)

        if values != number_list[len(number_list)-1]:
            if added == False:
                added = True
                plus_minus = str(random.choice(['*', '/']))
                question_string += ' ' + plus_minus + ' '
                question += plus_minus
            else:  
                plus_minus = str(random.choice(['+', '-']))
                question_string += ' ' + plus_minus + ' '
                question += plus_minus



    answer = eval(question)
    return question_string, answer







def expanding():
    """Generates random expression that need to be expaned."""

    # equation = ''
    # for i in range(0, 2):
    #     plus_minus = random.choice(['+', '-'])
    #     number = str(random.randint(1, 10))
    #     equation += f"(x {plus_minus} {number})"
    
    # question = equation
    # answer = 2

    question = answ_e(random.randint(-10, 10), random.randint(-10, 10), random.randint(1,3), random.randint(1,3))
    question.equation()
    question.answer()
    return question

def factorising():
    question = 1
    answer = 2
    return question, answer

# x = basic_equations()
# print(f"Question {x[0]}, and the answer is {x[1]}")
#x = expanding()
#print(x[0])


x = expanding()

print(x.equation)
#print(x.answer)
u_answer = input("What is the answer?: ").lower()
#print(u_answer.answer)
if u_answer == x.answer:
    print("Correct")
else:
    print(f"Wrong the answer was {x.answer}")