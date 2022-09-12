#!/bin/python3
#-*- encoding: utf-8 -*-

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a,b : a)
    
def cdr(pair):
    return pair(lambda a,b : b)

llist = cons(1, (cons(2, cons(3, 4))))

print(car(cdr(llist)))
