#!/usr/bin/env python
# -*- coding: utf-8 -*-


def summator(x,h):
    lenN = len(x)-1
    lenM = len(h)-1
    sum = 0
    n=3
    if n == 0:
        tmp = x[n]*h[lenM]
    else:
        for i in range(n+1):
            if (n > lenN or n < 0):
                tmp = 0
                sum += tmp
            if (n > lenM or n < 0):
                tmp = 0
                sum += tmp
            else:
                print 'x[',i,'] * h[',n-i,']'
                tmp = x[i]*h[n - i]
                print x[i]
                print h[n-i]



    return sum

x = [2,1,3,-1]
h = [-1,1,2]

print summator(x,h)

