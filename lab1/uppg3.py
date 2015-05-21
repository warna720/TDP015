#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Var:
    def __init__(self, value):
        self.v = value
        
    def value(self, kv):
        return kv[self.v]

    def getVars(self):
        return self.v
        

class General(object):

    """Set 'a' and 'b' to str or object reference"""
    def __init__(self, a, b):
        self.vars = []
        for v in [a, b]:
            self.vars.append(v)

    """Fetch value"""
    def value(self, kv):
        result = []
        for v in self.vars:
            if isinstance(v, bool):
                result.append(v)
            else:
                result.append(v.value(kv))
        return result

    def getVars(self):
        result = []
        for v in self.vars:
            if not isinstance(v, bool):
                result.append(v.getVars())
        flattened = [val for sublist in result for val in sublist]
        return flattened
        


#Conjuction
class Conj(General):
    def value(self, kv):
        a,b = super().value(kv)
        return a and b

#Disjunction
class Dis(General):
    def value(self, kv):
        a,b = super().value(kv)
        return a or b

#Negation
class Neg:
    def __init__(self, a):
        self.a = a

    def value(self, kv):
        if isinstance(self.a, bool):
            a = self.a
        else:
            a = self.a.value(kv)
        return not a

    def getVars(self):
        if not isinstance(self.a, bool):
            return self.a.getVars()
        return None

#Conditional
class Cond(General):
    def value(self, kv):
        a,b = super().value(kv)
        return not (a and not b)

#Equivalent
class Equ(General):
    def value(self, kv):
        a,b = super().value(kv)
        return a == b


expr1 = Var('a')
expr2 = Neg(expr1)
expr3 = Dis(expr1, expr2)
assignment = {'a' : True, 'b': False, 'x' : False}
flip_assignment = {'a' : False, 'b': True, 'x' : True}

assert expr1.value(assignment)
assert not expr1.value(flip_assignment)
assert expr2.value(flip_assignment)
assert not expr2.value(assignment)
assert expr3.value(assignment)

