# -*- coding: utf-8 -*-


from numpy import *
import matplotlib.pyplot as plt
from math import sqrt

def f1(x):
    return (pow(x,3)-x)**0.5

def f2(x):
    return -(pow(x,3)-x)**0.5

x = linspace(-10, 10)
y1 = f1(x)
y2 = f2(x)
plt.axis([-100, 100, -1000, 1000])
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
