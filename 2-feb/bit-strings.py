#!/bin/env python3

import random

string_length = 4
max_depth = 3
depth_chance = 0.5

operators = ['&', '|', '^', '~', 'SHIFT', 'CIRC']
lambdas = {
        '&': lambda a, b: ''.join(str(int(i) & int(j)) for i,j in zip(a, b)),
        '|': lambda a, b: ''.join(str(int(i) | int(j)) for i,j in zip(a, b)),
        '^': lambda a, b: ''.join(('1' if i == j else '0') for i,j in zip(a, b)),
        '~': lambda s: ''.join(str(1 - int(i)) for i in s),
        'SHIFT': lambda s, n: '0'*n + s[:-n] if n > 0 else s[-n:] + '0'*(-n),
        'CIRC': lambda s, n: (s[-n:] + s[:-n]) if n > 0 else (s[n:] + s[:n])
        }

class Expression:
    def __init__(self, depth=0):
        self.operator = random.choice(operators)
        self.ops = []

        if self.operator == '~':
            # One operand
            self.add_operand(depth)
        else:
            self.add_operand(depth)
            if self.operator == 'SHIFT':
                self.ops.append(random.randrange(-string_length, string_length))
            elif self.operator == 'CIRC':
                self.ops.append(random.randrange(-15, 15))
            else:
                self.add_operand(depth)
    
    def add_operand(self, depth):
        if depth < max_depth and random.random() < depth_chance ** depth:
            self.ops.append(Expression(depth + 1))
        else:
            self.ops.append(''.join(str(random.randrange(2)) for i in range(string_length)))

    def solve(self):
        solved = []
        for op in self.ops:
            if 'Expression' in str(type(op)):
                solved.append(op.solve())
            else:
                solved.append(op)
        return lambdas[self.operator](*solved)

    def __str__(self):
        if self.operator == '~':
            return self.operator + str(self.ops[0])
        if self.operator in ('SHIFT', 'CIRC'):
            if self.ops[1] > 0:
                return '(R' + self.operator + '-' + str(self.ops[1]) + ' ' + str(self.ops[0]) + ')'
            else:
                return '(L' + self.operator + '-' + str(-self.ops[1]) + ' ' + str(self.ops[0]) + ')'
        return '(' + f' {self.operator} '.join(map(str, self.ops)) + ')'

def generate_problem():
    e = Expression()
    print('Solve the expression')
    print(str(e))
    print('Press ENTER to see the solution')
    input()
    print(e.solve())

generate_problem()
