# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pt import*
from Keys import *

def form_stack(tasks):
    for t in tasks:
        t.append(t[2]*5+t[3])
        t.append('')
    return tasks

n=10
V=16
H=12
a=[]
timing=-1
#state = work,ready,skip,ok
#tasks=[n,v,h,t,q*h+t,state]
data = [ [1,1,3,50], [2,1,3,50] , [3,5,0,30],[4,3,4,90] ,[5,1,3,50],[6,1,3,50],[7,5,0,30],[8,3,4,90],[9,1,3,50] ,[10,1,3,50]]
stack=[0,0,0,0,0,0,0,0,0,0]
#data = [ [1,4,1,10], [2,4,1,10] , [3,5,0,30], [4,4,6,30],[5,4,6,30],[6,4,6,30],[7,4,6,40],[8,6,2,70],[9,3,4,90] ,[9,3,4,90] ]
tasks=form_stack(data)
outfile = open("result.txt", 'w')
cordX=0

"""
def add():
    global n
    while 1:
        print Please select operation:
        [1] Enter lenght stack tasks
        [2] Enter task
        [3] Menu
        x=keypress()
        if x == ord('1'): enter_n()
        if x == ord('2'): data_form()
        if x == ord('3'): return 0
    return 0


def enter_n():
    global n
    n=int(raw_input('Enter N'))
    return n

def data_form():
    data=[]
    for i in range(n):
        buf=int(raw_input('Enter N task'))
        data[i][0].append(buf)
        buf=int(raw_input('Enter need RAM'))
        data[i][1].append(buf)
        buf=int(raw_input('Enter need HDD'))
        data[i][2].append(buf)
        buf=int(raw_input('Enter need CPU burst'))
        data[i][3].append(buf)
    return data
 """

def calc():

    global stack,cordX,outfile,V,H,timing,tasks,a

    text=''
    q=5
    skip=False
    end=True
    timing=timing+1
   #Проходим по очереди определяем завершившихся
        #Сначала освобождаем ресурсы по возможности
    for t in tasks:
        if (t[5]=='work') and (timing>=t[4]):
            t[5]='ok'
            H=H+t[2]
            V=V+t[1]
            text='Такт '+str(t[4])+' Ресурсы: RAM '+str(V)+' HDD '+str(H)+' Задача '+str(t[0])+' Завершилась \n'
            print text
            outfile.write(text)
            text=''
        if t[5]<>'ok':
            outfile.close
            end=False
    #Проверяем возможность ввода задачи
    for t in tasks:

        if (t[5]=='') and (((H-t[2])<0) or ((V-t[1])<0)) and (not skip):
            print t
            text='Такт '+str(timing)+' Ресурсы: RAM '+str(V)+' HDD '+str(H)+' Задача '+str(t[0])+' В очередь \n'
            print text
            outfile.write(text)
            text=''
            t[5]='skip'
            skip=True
        if ((t[5]=='') or (t[5]=='skip')) and ((H-t[2])>=0) and ((V-t[1])>=0) and (not skip):
            if t[5]=='skip':
                text= 'Такт '+str(timing)+' Задача'+str(t[0])+' Вышла из очереди \n'
                stack[t[0]-1]=timing

                print text
                outfile.write(text)
                text=''
            t[4]=t[4]+timing #Добавляем к таймеру время уже прошедьшее
            if t[2]<>0: #hhd <> 0
                t[5]='ready'
                text='Такт '+str(timing)+' Ресурсы: RAM '+str(V)+' HDD '+str(H)+' Задача '+str(t[0])+' Запущена \n'
                print text
                outfile.write(text)
                text=''
            else:
                t[5]='work'
                text='Такт '+str(timing)+' Задача '+str(t[0])+' Выполнение \n'
                print text
                outfile.write(text)
                text=''
            H=H-t[2]
            V=V-t[1]
            skip=True
        #Если задача активна и время ввода завершилось - запуск выполнения

        if (t[5]=='ready')and(timing>=(t[4]-t[3]))and (not skip):
            t[5]='work'
            text='Такт '+str(timing)+' Задача '+str(t[0])+' Выполнение \n'
            print text
            outfile.write(text)
            text=''
            skip=True

    if not(end):
        calc() #Рекурсия. Опять.
    else:
        #Вывод графика


        #hlines(y, xmin, xmax, colors='k', linestyles='solid', label='', **kwargs)

        for i in range(10):
            hq=tasks[i][4]-tasks[i][3]
            t=tasks[i][4]
            wait=stack[i]
            plt.hlines(i+1, [0],wait  ,colors='r', lw=2)
            plt.hlines(i+1, wait,hq  ,colors='b', lw=2)
            plt.hlines(i+1, hq , t ,colors='g', lw=2)
            plt.plot(wait,i+1, 'b^')
            plt.plot(t,i+1, 'b^')
            plt.plot(hq,i+1, 'b^')


        #axus [xmin, xmax, ymin, ymax]
        plt.axis([0, 300, 0, 11])
        plt.grid(True)
        plt.ylabel('N task')
        plt.xlabel('time ')
        plt.title('FIFO')
        plt.show()
        #plt.savefig('diag.png', dpi=200)
        #Окончен вывод

calc()




"""
if __name__ == '__main__':
    while 1:
        print Please select one from the menu:
        [1] Default test.
        [2] Enter tasks
        x=keypress() добавь опострофы
        if x == ord('1'): calc()
        if x == ord('2'): add()
        if keypress() in map(ord,'qQ'):
            break
        else:
            continue
"""