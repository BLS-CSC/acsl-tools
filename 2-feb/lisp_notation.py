#!/bin/env python3

import random
import operator
from functools import reduce

max_length = 3
max_depth = 3
depth_chance = 0.5

operators = '+-*/^'
lambdas = (
        sum,
        lambda l: reduce(operator.sub, l),
        lambda l: reduce(operator.mul, l),
        lambda l: reduce(operator.truediv, l),
        lambda l: reduce(operator.pow, l),
        )

class Expression:
    def __init__(self, depth=0):
        self.operator = random.choice(operators)
        self.ops = []

        for i in range(random.randrange(2, max_length)):
            if (depth < max_depth and random.random() < depth_chance ** depth):
                self.ops.append(Expression(depth + 1))
            else:
                self.ops.append(Value())
        
    def prefix(self):
        return f'({self.operator} ' +' '.join(map(lambda exp: exp.prefix(), self.ops)) + ')'

    def postfix(self):
        return '(' + ' '.join(map(lambda exp: exp.postfix(), self.ops)) + ' ' + self.operator + ')'

    def infix(self):
        return '(' + f' {self.operator} '.join(map(lambda exp: exp.infix(), self.ops)) + ')'

    def eval(self):
        return lambdas[operators.find(self.operator)](map(lambda exp: exp.eval(), self.ops))

class Value(Expression):
    def __init__(self):
        self.value = random.randrange(1, 10)
    def prefix(self):
        return str(self.value)
    postfix = prefix
    infix = prefix
    def eval(self):
        return self.value

def generate_problem():
    problem_types = ('convert', 'evaluate')
    
    ptype = random.choice(problem_types)
    e = Expression()

    reprs = (e.prefix, e.postfix, e.infix)
    repr_names = ('prefix', 'postfix', 'infix')
    from_type = random.randrange(3)

    if ptype == 'convert':
        to_type = random.randrange(3)
        while to_type == from_type:
            to_type = random.randrange(3)
        
        question = f'Convert {reprs[from_type]()} from {repr_names[from_type]} to {repr_names[to_type]}.'
        answer = reprs[to_type]()

        return (question, answer)
    if ptype == 'evaluate':
        question = f'Evaluate the {repr_names[from_type]} expression {reprs[from_type]()}.'
        answer = str(e.eval())
        return (question, answer)

question, answer = generate_problem()
print(question)
print('Press ENTER to see the answer')
input()
print(answer)
