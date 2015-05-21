#!/usr/bin/env python
# -*- coding:utf-8 -*-

tree = (('1', '*', '2'), '+', (('3', '+', '4'), '*', '5'))

def pre_order(tree):
    if isinstance(tree, tuple):
        return tree[1] + pre_order(tree[0]) + pre_order(tree[2])
    return tree

print(pre_order(tree))

def post_order(tree):
    if isinstance(tree, tuple):
        return post_order(tree[0]) + post_order(tree[2]) + tree[1]
    return tree

print(post_order(tree))

def in_order(tree):
    if isinstance(tree, tuple):
        return in_order(tree[0]) + tree[1] + in_order(tree[2])
    return tree

print(in_order(tree))
