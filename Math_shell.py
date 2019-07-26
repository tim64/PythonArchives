#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pt import*
from Method import *
from Keys import *

#------------------ Menu 1------------------------------
def Com():
    while 1:
        print """Please select operation:
        [1] A(n,m)
        [2] C(n,m)
        [3] P(n)
        [4] Menu"""
        x=keypress()
        if x == ord('1'): f1()
        if x == ord('2'): f2()
        if x == ord('3'): f3()
        if x == ord('4'): return 0
    return 0
        

def f1():
    print "Enter m and n. n>m."
    m=int(raw_input("m? "))
    n=int(raw_input("n? "))
    if n<m:
        print "Error! N<M!"
        return 0
    else:
        print "A(",m,",",n,")= ", A(m,n)

def f2():
    print "Enter m and n. n>m."
    m=int(raw_input("m? "))
    n=int(raw_input("n? "))
    if n<m:
        print "Error! N<M!"
        return 0
    else:
        print "C(",m,",",n,")= " ,C(m,n)

def f3():
    print "Enter m"
    m=int(raw_input("m? "))
    print "P(",m,")= ",P(m)
   

#---------------------------------------------------------------

#------------------------Menu 2-------------------------------------
def Characters():
    while 1:
        print """Please select operation:
        [1] M(x)
        [2] D(x)
        [3] S(x)
        [4] Menu"""
        x=keypress()
        if x == ord('1'): f4()
        if x == ord('2'): f5()
        if x == ord('3'): f6()
        if x == ord('4'): return 0
    return 0
    

def f4():
    x=[]
    p=[]
    print "Mat.ojidanie"
    n=int(raw_input("Enter kol-vo elementov"))
    print "Enter X"
    for i in range(n):
        x.append(int(raw_input("X ?")))
    print "Enter P"
    for i in range(n):
        p.append(float(raw_input("P ?")))
    print "M(",x,") = ", matO(x,p)
    
def f5():
    x=[]
    p=[]
    print "Dispersia"
    n=int(raw_input("Enter kol-vo elementov"))
    print "Enter X"
    for i in range(n):
        x.append(int(raw_input("X ?")))
    print "Enter P"
    for i in range(n):
        p.append(float(raw_input("P ?")))
    print "D(",x,") = ", desp(x,p)
    
def f6():
    x=[]
    p=[]
    print "Otclonenie"
    n=int(raw_input("Enter kol-vo elementov"))
    print "Enter X"
    for i in range(n):
        x.append(int(raw_input("X ?")))
    print "Enter P"
    for i in range(n):
        p.append(float(raw_input("P ?")))
    print "S(",x,") = ", sred(x,p)
        

#------------------------------Menu 3---------------------------------------

def Raspred():
    while 1:
        print """Please select operation:
        [1] Puasson
        [2] Binomial
        [3] Menu"""
        x=keypress()
        if x == ord('1'): f7()
        if x == ord('2'): f8()
        if x == ord('3'): return 0

    return 0

def f7():
    print "Puasson raspredelenie"
    l=float(raw_input("Lambda ?"))
    t=float(raw_input("T ?"))
    m=float(raw_input("Mat. O ?"))
    print puas(m,l,t),2


def f8():
    print "Binomial"
    n=int(raw_input("Kol-vo ?"))
    p=float(raw_input("P ?"))
    binom(n,p)


#-------------------------------Menu 4-------------------------------------

def odc():
    print "ODC"
    a=int(raw_input("a ?"))
    b=int(raw_input("b ?"))
    print nod(a,b)

#-----------------------------Menu 5---------------------------------

def simple():
    print "Simple count"
    n=int(raw_input("N?"))
    print erator(n)

#------------------------------Menu 6----------------------------------

def factor():
    print "Factorial"
    n=int(raw_input("N?"))
    print fact(n)

    
#------------------- MAIN----------------------------------------

if __name__ == '__main__':          
    while 1:
        print """Please select one from the menu:
        [1] Combinators (A,C,P).
        [2] Mx,Dx,Sx.
        [3] Binomial,Puasson
        [4] ODC
        [5] Simple count
        [6] Factorial"""
        x=keypress()
        if x == ord('1'): Com()
        if x == ord('2'): Characters()
        if x == ord('3'): Raspred()
        if x == ord('4'): odc()
        if x == ord('5'): simple()
        if x == ord('6'): factor()
        print 'Press q to quit.\n'
        if keypress() in map(ord,'qQ'):
            break
        else:
            continue
  

