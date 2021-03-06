#!/bin/env python3

import random
import operator
from functools import reduce
import sys

max_length = 3
max_depth = 3
depth_chance = 0.5
num_inputs = 4
latex = '--latex' in sys.argv

operators = [' + ', '', '~']
if latex:
    operators[2] = '\\overline'
lambdas = {
        ' + ': lambda l: reduce(operator.or_, map(bool, l)),
        '': lambda l: reduce(operator.and_, map(bool, l)),
        operators[2]: operator.not_
        }

class Expression:
    def __init__(self, depth=0):
        self.operator = random.choice(operators)
        self.ops = []

        if operator == operators[2]:
            # One operand
            self.add_operand(depth)
        else:
            for i in range(random.randrange(2, max_length)):
                self.add_operand(depth)
    
    def add_operand(self, depth):
        if depth < max_depth and random.random() < depth_chance ** depth:
            self.ops.append(Expression(depth + 1))
        else:
            self.ops.append(random.choice(variables))

    def __bool__(self):
        return lambdas[self.operator](self.ops)

    def __str__(self):
        if (self.operator == operators[2]):
            return '(' + self.operator + ('{' if latex else '') + str(self.ops[0]) + ('}' if latex else '') + ')'
        else:
            return '(' + self.operator.join(map(str, self.ops)) + ')'

class Variable(Expression):
    def __init__(self, index):
        self.index = index
        self.value = random.random() < 0.5
    def __bool__(self):
        return self.value
    def __str__(self):
        return chr(ord('A') + self.index)

variables = []

def generate_problem():
    global variables
    print('Given that...')
    variables = [Variable(i) for i in range(num_inputs)]
    for var in variables:
        print(f'{str(var)} = {bool(var)}')

    print('Simplify and solve the expression below.')

    e = Expression()
    print(str(e))
    
    print('Press ENTER to find the solution')
    input()
    print(bool(e))

generate_problem()
