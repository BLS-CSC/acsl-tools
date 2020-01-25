#!/bin/env python3

import operator
import sys

operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
        }

print('This tool is extremely simple. Place a single space between each item and do not include parentheses.')
print('Include the -y option to skip prompts')

in_expr = input()
exprs = in_expr.split()
i = 0
print()

operand_stack = []

for expr in exprs:
    print(in_expr)
    print(' '*i + '^')
    print(f'Reading expression {expr}')
    if expr in operators.keys():
        print(f'{expr} is an operator, so we pop two items off the stack.')
        op1 = operand_stack.pop()
        print(f'Operand 1 is {op1}')
        op2 = operand_stack.pop()
        print(f'Operand 2 is {op2}')
        
        res = operators[expr](op1, op2)
        print(f'Our result is {res}, which we push onto the stack.')
        operand_stack.append(res)
    else:
        print(f'{expr} is an operand, so we add it to the stack.')
        operand_stack.append(int(expr))
    print(f'Our stack is now: {operand_stack}')
    i += len(expr) + 1
    
    if ('-y' not in sys.argv):
        print('Press ENTER to continue.')
        input()

print(f'Our answer is {operand_stack[0]}')
