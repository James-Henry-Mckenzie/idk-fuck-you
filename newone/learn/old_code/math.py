from dataclasses import dataclass
import random
from sympy import *


# x, y, z = symbols('x,y,z')
# print(((x + y)*(x - y)).expand(simple=True))
# p = str(((4*x+5)*(2*x-4)).expand(simple=True))
# p = p.replace("**", "^")
# p = p.replace("*", '')

#print(p)

powers = {'^':'**','**0':'⁰', '**1':'¹', '**2':'**²', '**3':'³', '**4':'⁴', '**5':'⁵', '**6':'⁶', '**7':'⁷', '**8':'⁸', '**9':'⁹', '*':'', 'x':'𝑥'}


def fixe(fixer):
    for chars in powers:
        fixer = fixer.replace(chars, powers[chars])
    fixer = fixer.replace(" ", "")
    return fixer

@ dataclass
class Equation():
    num_1: int
    num_2: int
    num_4: int
    num_3: int

    

    def answer(self):
        temp_2 = ''
        while len(temp_2) <= 10:
            x = symbols('𝑥')
            #print((self.num_1*x + self.num_2)*(self.num_3 * x - self.num_4))
            temp = ((self.num_1*x + self.num_2)*(self.num_3 * x - self.num_4)).expand(simple=True)
            #print(temp, 'temp')
            temp_2 = str(factor(((self.num_1*x + self.num_2)*(self.num_3 * x - self.num_4))))
            if len(temp_2) <= 10:
                self.num_2 += 1
                self.num_4 += 1

        #print(temp_2, 'temp2\n')
        temp = str(temp)
        for stuff in powers:
            temp = temp.replace(stuff, powers[stuff])
            temp_2 = temp_2.replace(stuff, powers[stuff])
        self.question = temp_2
        self.answer = temp


# def exp_fac(x):
#     high_low = [-2, 2]
#     low_high = [-10, 10]
#     if x ==0:
#         high_low = [-1, 2]
#         low_high = [-4, 6]

#     prob = Equation(random.randint(high_low[0], high_low[1]), random.randint(low_high[0], low_high[1]), random.randint(high_low[0], high_low[1]), random.randint(low_high[0], low_high[1]))
#     prob.answer()
#     return prob    

# def exp():
#     equ = exp_fac(1)
#     print(f"Fully expand the expression {equ.question}")
#     x = equ.answer.replace(' ', '')
#     print(x)
#     u_answer = input(": ").lower()
#     u_answer = u_answer.replace(' ', '')
#     for stuff in powers:
#         u_answer = u_answer.replace(stuff, powers[stuff])

#     #print(u_answer, x)
#     if u_answer == x:
#         print("Correct")
#         score = 1
#     else:
#         print(f"Wrong the answer was {equ.answer}")
#         score = 0
#     return score

# def fac():
#     equ = exp_fac(0)
#     print(f"Fully factorise the expression {equ.answer}")
#     x = equ.question.replace(" ", '')
#     print(x)
#     u_answer = input(": ").lower()
#     u_answer = u_answer.replace(' ', '')
#     for stuff in powers:
#         u_answer = u_answer.replace(stuff, powers[stuff])
#     if u_answer == x:
#         print("Correct")
#         score = 1
#     else:
#         print(f"Wrong the answer was {equ.question}")
#         score = 0
#     return score


# def main():
#     again = ''
#     points = 0
#     while again != 'no':
#         print(points)
#         choice = int(input("1) Expanding\n2) Factorising\n:"))
#         if choice == 1:
#             for i in range(0, 3):
#                 points += exp()
#         elif choice == 2:
#             for i in range(0, 3):
#                 points += fac()


# def get_siz(n1, n2, n3, n4):
#     x = Equation(n1, n2, n3, n4)
#     x.answer()
#     return x.answer, x.question, x

