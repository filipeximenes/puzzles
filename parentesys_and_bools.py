# -*- coding: utf-8 -*- 
# source: http://dojopuzzles.com/problemas/exibe/parenteses-booleanos/

# Parentesys and booleans

# Given a boolean expression, containing the symbols: 'True', 'False', 'and', 'or', 'xor',
# write a program that counts how many whays are there to return a True value
# using parentesys

# Example from the source:
# 'True and False xor True' should return 1
# this is probably mistaken since:
# '(True and False) xor True'
# and
# 'True and (False xor True)'
# both return True therefore the answer should be 2

import itertools


def get_item_pos(exp, pos):
    for j, tup in enumerate(exp):
        if tup[0] == pos: return j


def do_op(op, bool1, bool2):
    if op == 'and': return eval(bool1) and eval(bool2)
    elif op == 'or': return eval(bool1) or eval(bool2)
    elif op == 'xor': return eval(bool1) != eval(bool2)


def operate(exp, item):
    i = get_item_pos(exp, item)
    if i:
        _, exp1 = exp.pop(i-1)
        _, op = exp.pop(i-1)
        _, exp2 = exp.pop(i-1)
        exp.insert(i-1, (-1, str(do_op(op, exp1, exp2))))

    return exp


def count_par(exp, v=False):
    count = 0

    exp = exp.split()
    exp = zip(range(len(exp)), exp)

    ops = [pos for pos, item in exp[1::2]]
    ops = itertools.permutations(ops, len(ops))

    if v: print exp; print 'precedence order:';

    for sequence in ops:
        aux_exp = list(exp)
        for op in sequence:
            aux_exp = operate(aux_exp, op)

        _, res = aux_exp[0]
        if res == 'True': 
            count += 1
            if v: print sequence

    return count

print count_par("True and False or True or False", v=True)
print count_par("True and False or True or False and False", v=True)
print count_par("True and False or True or False and False or True", v=True)
print count_par("True and False or True or False and False and True", v=True)
print count_par("False and False and False and False", v=True)
print count_par("True and False xor True", v=True)
