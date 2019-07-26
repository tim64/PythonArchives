# -*- coding: utf-8 -*-

import random
import string
import time
import math
import sys

#Лабараторная работа 1
# 1) Алгоритм быстрого возведения в степень
def mod_power(a, n, p):
    result = 1
    list = []
    item = a
    b = bin(n).replace('0b','')
    for i in b:
        list.append(item)
        item = (item * item)%p
    list.reverse()
    for i in range(len(b)):
        if b[i] == '1':
            result = (result * list[i])%p
    return result

#print 'Lab 1.1 ', mod_power(312, 287, 435)

# 2)Обобщенный алгоритм Евклида

def gcd (a, b):
    if b == 0:
        x = 1
        y = 0
        return a, x, y
    d, x1, y1 = gcd(b, a % b)
    x = y1
    y = x1 - (a / b) * y1
    return d , x, y


#d, x, y = gcd(28, 19)
#print 'Lab 1.2 GCD = ',d,' X = ',x,' Y = ',y

# 3)Система Диффи-Хэлмана

def dh_system(xa, xb, p, g):
    q = (p - 1)/2
    print q
    Xa, Xb = xa, xb
    if mod_power(g, q, p) != 1:
        Ya = mod_power(g, Xa, p)
        Yb = mod_power(g, Xb, p)
        Zab = mod_power(Yb, Xa, p)
        Zba = mod_power(Ya, Xb, p)
        return Ya, Yb, Zab, Zba
    else:
        print 'Please choose another "g"'
p = 413
g = 342
xa = 311
xb = 100
#Ya, Yb, Zab, Zba = dh_system(xa, xb, p, g)
#print 'Lab 1.3 p =',p,' g =',g,'Result: Ya=',Ya,' Yb=',Yb,' Zab=',Zab, ' Zba=',Zba

# 4) Метод "Шаги младенца, шаги гиганта"
def BGstep(a, p, y):
    baby = []
    giant = []
    m = random.randint(int(p/2),p+1)
    k = random.randint(int(p/2),p+1)
    if k*m > p:
        #Create baby-list
        for i in range (0, m):
            baby.append ((y * a ** i) % p)
        #Create giant-list
        for i in range (1, k + 1):
            giant.append ((a ** (i * m)) % p)
        #Compare baby-list and giant-list
        for i in range(len(baby)):
            for j in range(len(giant)):
                if baby[i] == giant[j]:
                    print baby[i], giant[j]
                    if i == 0:
                        i += 1
                    if j == 0:
                        j += 1
                    return i*m - j
    else:
        print 'm*k must be > p'
        return -1

def check(a,p, y, x):
    if mod_power(a,x,p) == y:
        return True
    else:
        return False

a = 230
p = 239
y = 229
result = BGstep(a, p, y)
print 'Lab 1.4 p =',p,' a =',a,'y = ',y,'x = ',result
print check(a,p,y,result)









