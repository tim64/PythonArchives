# -*- coding: utf-8 -*-

graph=[[1,1,0,1],
       [1,1,1,1],
       [0,1,1,1],
       [1,1,1,1]]
    
def vertex(graph):
    i=int(raw_input('введите вершину: '))
    for j in range(len(graph)):
        if (graph[i][j]==1) and (i<>j):
            print 'Вершина ',i,' смежна с вершиной ',j
    return 0

vertex(graph)

