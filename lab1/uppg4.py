#!/usr/bin/env python
# -*- coding:utf-8 -*-

import itertools
from uppg3 import *

def satisfiable(formula):
    """Return true if formula is satisfiable"""

    exprVars = list(set(formula.getVars())) #Returns all variables in use
    combs = list(itertools.product(*[exprVars, [True, False]]))
    combs = list(itertools.permutations(combs, len(exprVars)))

    uniqueCombs = []
    #Remove all combinations which does not use all vars
    for comb in combs:
        allVars = []
        for v in comb:
            allVars.append(v[0])
        if len(set(allVars)) == len(exprVars):
            uniqueCombs.append(list(comb))

    #Test satisfiable
    for comb in uniqueCombs:
        vBools = {}
        for v in comb:
            vBools[v[0]] = v[1]
        if formula.value(vBools):
            return True
    return False


print("\n"*2)
print("Satisfiables")
print("="*13, end="\n\n")

print("a AND b AND c AND d")
print(satisfiable(Conj(Var("a"), Conj(Var("b"), Conj(Var("c"), Var("d"))))))
print()

print("a AND b AND c AND False")
print(satisfiable(Conj(Var("a"), Conj(Var("b"), Conj(Var("c"), False)))))
print()

print("a AND False")
print(satisfiable(Conj(Var("a"), False)))
print()

print("(False and False) OR b")
print(satisfiable(Dis(Conj(False, False), Var("b"))))
print()

print("(False Cond a) Cond b")
print(satisfiable(Cond(False, Cond(Var("a"), Var("b")))))
print()

print("(a AND b) AND b")
print(satisfiable(Conj(Conj(Var("a"), Var("b")), Var("b"))))
print()

print("NOT(a AND b) OR ((a AND b) and c)")
print(satisfiable(Dis(Neg(Conj(Var("a"), Var("b"))), Conj(Conj(Var("a"), Var("b")), Var("c")))))
print()
