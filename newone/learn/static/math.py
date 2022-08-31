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
    #operation: str
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


