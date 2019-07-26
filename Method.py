#!/usr/bin/env python
# -*- coding: utf-8 -*-


from numpy import *
import matplotlib.pyplot as plt
import random as random_number
import time

def nod(a,b):
    if (a%2<>0) and (b%2<>0):
        if (a%2==0) and (b%2<>0):
            a=a/2

    if (a%2<>0) and (b%2==0):
        b=b/2

    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


def nod_b(a,b):
    g=1
    while (a%2==0) and (b%2==0):
        a=a/2
        b=b/2
        g=2*g
    while a<>0:
        while a%2==0:
            a=a/2
        while b%2==0:
            b=b/2
        if a>=b:
            a=(a-b)/2
        else:
            b=(b-a)/2

    return g*b


def powmod(a,k,n):
    res=1
    while(k):
        if k%2==0:
            k/=2
            a = (a*a)%n
        else:
            k-=k
            res = (res*a)%n
            return res


def miller_rabin_pass(a, n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    a_to_power = powmod(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def miller(n):
    import random, sys
    if (n%2==0) or (n%3==0) or (n%7==0) or (n%5==0) or (n%11==0):
        return False
    for repeat in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, n):
            return False
    return True

def ferma_test(n):
    if n%2==0:
        print n
        return 0
    if (n%3==0) or (n%7==0) or (n%5==0) or (n%11==0):
        print n
        return 0
    import random as random_number
    a = int(round(random_number.uniform(1, n-1),0))
    p=pow(a,n-1)
    if nod(a,n)==1:
        if ((p-1)%n)==0:
            print n
    else:
        print n

    return 0


def friend(a,b):
    if nod(a,b)==1:
        return True
    else:
        return False


def f_eiler(n):
    c=0
    for i in xrange(n):
        if friend(i,n)==True:
            c+=1
    return c

def phi(p,q):
    return (p-1)*(q-1)


def DtoB(x):
    n=[]
    while x > 0:
        y = x % 2
        n.append(y)
        x = x / 2
    return n




def gen(a,n):
    for i in range(n):
        a[i] = i
        a[1] = 0
    return a

def erator(n):
    a = [0] * n
    gen(a,n)
    m=2
    while m < n:
        if a[m] != 0:
            while j<n:
                a[j]=0
                j=j+m
        m +=1
    b=[]
    for i in a:
        if a[i] !=0:
            b.append(a[i])

    return b




def XorSwap(x,y):
    x=x^y
    y=y^x
    x=x^y
    return x,y


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)



def MCint(f, a, b, n):
    s = 0
    for i in range(n):
        x = random_number.uniform(a, b)
        s += f(x)
    I = (float(b-a)/n)*s
    return round(I,1)

def f1(x):
    return 2+3*x



def mod(a,b,n):
    if (a-b)%n==0:
        return True
    else:
        return False
    return 0



def factor_simple(n):
    res=[]
    i=2
    from math import sqrt
    while i<n:
        e=0
        if n%i==0:
            while n%i==0:
                e=e+1
                n=n/i
                res.append(i)
        i += 1
    return res

print factor_simple(11111111111111111111111111111111111111111111111111111111111111)

def p_Sqrt(m):
    f=f_eiler(m)
    for g in xrange(0,m):
        for l in xrange(0,f-1):
            if mod(pow(g,f),1,m)==True:
                if mod(pow(g,l),1,m)==False:
                    return g
    return 0





def simpson(a,b,eps):
    n=1
    s=0.0
    work=True
    while (work == True):
        s0=s
        n=n*2
        h=(b-a)/n
        s=fun(a)+fun(b)
        for i in range(1,n):
            s=s+2*(1+i % 2)*fun(a+i*h)
        s=(s*h)/3
        if (abs(s-s0) <= eps):
            break
    return s




def trapec(a,b,eps):
    n=2
    s0=0
    s=0
    x=a
    work=True
    while (work == True):
        h=(b-a)/n
        s=fun(a)+fun(b)
        for i in range(1,n):
            s=s+2*fun(a+i*h)
        s = s*h/2
        if (abs(s-s0) <= eps):
            break
        else:
            s0=s
            n=2*n
    return s


def fun(x):
    return (6*x)/(sqrt(x**2+1))
def dx(x0):
    h=0.000001
    return (-fun(x0+2*h) + 8*fun(x0+h) - 8*fun(x0-h) + fun(x0-2*h))/(12*h)


valuesX=[0, 2, 4]
valuesY=[0, 4, 16]

def L(x, px, n, i):
    chis = 1
    znam = 1


    for k in range(n):
        if k == i:
            continue
        chis = chis * (px - x[k])


    for i in range(n):
        if x[i] == x[k]:
            continue
        znam = znam * (x[i] - x[k])


    return chis/znam


def interpolationL(px,x,y):
    n = len(x)
    result = []
    l = 0
    for i in range(n):
        l += y[i] * L(x,px,n,i)

    return l


def jacobi(a,b):

    exit = False
    if nod(a,b) != 1:
        return 0
    r=1
    if a<0:
        a = -a
        if b%4 == 3:
            r = -r
    while (exit == False):
        t=0
        while (a%2 == 0):
            t += 1
            a /= 2
        if t%2 != 0:
            if (b%8 == 3) or (b%8 == 5):
                r = -r
        if (a%4 == 3) and (b%4 == 3) :
            r = -r
        c = a
        a = b%c
        b = c
        if (a == 0):
            return r


def mypowmod(a, x, p):
    res= 1
    ind = 1
    setx = DtoB(x)
    trash, t = math.modf(math.log(x,2))
    for i in setx:
        if i==1:
            res = (res * (a**ind) % p) % p
        ind = ind * 2
    return res

def BGstep(y, a, p):
    P1 = []
    P2 = []
    M = int(raw_input("Enter M"))
    K = int(raw_input("Enter K"))
    if M*K > p:
        for m in range(M):
            P1.append( ((a**m) * y) % p )
        for k in range(1,K+1):
            P2.append( (a**(k*m)) % p)
            print (a**(k*m)) % p
        print P1
        print P2
        for i in range(len(P1)):
            for j in range(len(P2)):
                if P1[i] == P2[j]:
                    iP1 = i+1
                    iP2 = j+1
                    print iP1-1,' ',iP2-1
                    x = iP1*M - iP2
                    return x
    else:
        print "M*K must > p!"
        return 0




