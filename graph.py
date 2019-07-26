# -*- coding: utf-8 -*-

graph=[[0,1,0,0,1], #0
       [1,0,1,0,1], #1
       [1,0,0,1,0], #2
       [0,0,1,0,0], #3
       [1,1,0,0,0]] #4
    




def print_graph(graph):
    l = len(graph) 
    s = len(graph[0]) 
    for i in range(l):
        for j in range(s):
            if graph[i][j]==1:
                print i,'-',j



def add_edge(graph,vertex1,vertex2):
    l = len(graph) 
    s = len(graph[0])
    for str in graph:
        str.append(0)
    
    tmp=[]
    for i in range(l+1):
        tmp.append(0)
    graph.append(tmp)

    
    for i in range(l):
        if i==vertex1:
            graph[i][vertex2]=1
                

def del_vertex(graph,vertex):
    for str in graph:
        str[vertex]=0
    for i in range(len(graph[vertex])):
        graph[i][vertex]=0
        graph[vertex][i]=0
    
        
def friend_vertex(graph,vertex):
    l = len(graph) 
    s = len(graph[0]) 
    result=[]
    for i in range(l):
        for j in range(s):
            if i==vertex:
                if graph[i][j]==1:
                    result.append(j)
    return result


def zero(mas):
    for i in mas:
        if i==0:
            return True
    return False


    

 
print bsf(graph,3)
