#!/usr/bin/env python
# -*- coding:utf-8 -*-

def subsets(s):
    result = [[]]

    for e in s:
        tmp = []
        for s in result:
            tmp.append(s + [e])
        result.extend(tmp)
        
    return sorted(result, key = lambda element: len(element)) #-pedantic
    

print((subsets([1, 2, 3, "päron"])))
print((subsets(["banan", "äpple"])))
print((subsets([1, 2, 3, 4, 5])))
print(len(subsets([1, 2, 3, 4,5,6,7,8,9,10])) == 2**10)

