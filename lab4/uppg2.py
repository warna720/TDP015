#!/usr/bin/env python
# -*- coding:utf-8 -*-

import itertools

def subgraphs(n, s):
    combinations = [[]]
    
    for amount in range(1, len(s)+1):
        combinations.extend(list(itertools.combinations(s,amount)))

    #make everything a list instead of a generator
    combinations = list(map(lambda comb: list(comb), combinations))
    
    return combinations

g = subgraphs(5, {(0,1), (0, 4), (1, 2), (2, 3), (2, 4), (3, 0)})
print(g)

#g = subgraphs(3, {(0,1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)})
#print(len(g))

#subgraphs(4, {(0, 1), (1, 2), (2, 0)})
#g = subgraphs(4, {(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)})
#print(g)
