# -*- coding: utf-8 -*-

graph=[[1,1,0,1],
       [1,1,1,1],
       [0,1,1,1],
       [1,1,1,1]]

a=[[1,2,3],
   [4,1,0],
   [2,1,2]]

b=[[2,4,5],
  [0,1,0],
  [1,2,1]]   

def vertex(graph):
    i=int(raw_input('введите вершину: '))
    for j in range(len(graph)):
        if (graph[i][j]==1) and (i<>j):
            print 'Вершина ',i,' смежна с вершиной ',j
    return 0

def show_matrix(a):
    for i in range(len(a)):
            print a[i],'\n'
            
def plus(a,b):
    if len(a)<>len(b):
        print 'Must A=B!'
        return 0
    c=a
    for i in range(len(a)):
        for j in range(len(b)):
            c[i][j]=a[i][j]+b[i][j]
    show_matrix(c)
    return c


def minus(a,b):
    if len(a)<>len(b):
        print 'Must A=B!'
        return 0
    c=a
    for i in range(len(a)):
        for j in range(len(b)):
            c[i][j]=a[i][j]-b[i][j]
    show_matrix(c)
    return c


def trans(a):
    square=False
    for i in a:
        if len(a)==len(i):
            square=True
    if square==True:
        for i in range(len(a)):
            for j in range(i):
                buf=a[i][j]
                a[i][j]=a[j][i]
                a[j][i]=buf      
    show_matrix(a)
    return a




