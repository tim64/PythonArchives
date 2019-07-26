# -*- coding: utf-8 -*-

def simgen(start):
    x = start
    a=8
    b=32
    m=100
    for i in range(20):
        x = (a*x + b)%m
        print x
    return 0

simgen(4)