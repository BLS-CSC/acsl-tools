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

        if operator == '~':
            # One operand
            add_operand(depth)
        else:
            for i in range(random.randrange(2, max_length)):
                self.add_operand(depth)
    
    def add_operand(self, depth):
        if depth < max_depth and random.random() < depth_chance ** depth:
            self.ops.append(Expression(depth + 1))
        else:
            self.ops.append(random.random() < 0.5)

    def __bool__(self):
        return lambdas[self.operator](self.ops)

    def __str__(self):
        if (self.operator == operators[2]):
            return '(' + self.operator + ('{' if latex else '') + str(self.ops[0]) + ('}' if latex else '') + ')'
        else:
            return '(' + self.operator.join(map(str, self.ops)) + ')'

e = Expression()

print(str(e))
print(bool(e))
