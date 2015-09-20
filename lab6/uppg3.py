#!/usr/bin/env python3
#-*- coding: utf-8 -*-


def newton(f, f_prime, x, i = 10):
    if i == 0:
        return x

    x = x - (f(x) / f_prime(x))
    
    return newton(f, f_prime, round(x, 10), i-1)

def f(x):
    return x**5 - 5

def f_prime(x):
    return 5*x**4



print(newton(f, f_prime, 1))
