# -*- coding: utf-8 -*-
import string, codecs

turns = []

def parse(data):
    f
    f=codecs.open('parserresult.txt', 'w',"cp1251")
    index = 0

    for head in headers:
        """
        name = data[head+1].replace('MissionName=','')#Name
        giver = data[head+5].replace('MissionGiver=','') #Giver
        desc = data[head+2].replace('MissionDescription=','') #Desc
        summ = data[head+4].replace('MissionSummary=','')#Summ
        turn = data[head+3].replace('TurnInDescription=','')

        """
        name = data[head+3].replace('MissionName=','')#Name
        giver = data[head+2].replace('MissionGiver=','') #Giver
        desc = data[head+1].replace('MissionDescription=','') #Desc
        summ = data[head+4].replace('MissionSummary=','')#Summ
        turn = data[turns[index]].replace('TurnInDescription=','')

        f.write(u'{{Миссия|Название='+name)
        f.write(u'|Изображение=|Локация=|')
        f.write(u'Даёт=[['+giver+']]|')
        f.write(u'Игра=[[Borderlands]]}}')
        f.write(name)
        f.write(u'Задание в [[Borderlands]], которое выдает '+giver)
        f.write(u'Цель -' + summ)
        f.write(u'Описание - ' + desc)
        f.write(u'Сообщение при сдаче -' + turn)
        f.write(u'[[Категория:Borderlands|{{PAGENAME}}]]')
        f.write(u'[[Категория:Задания Borderlands|{{PAGENAME}}]]')
        f.write(u'END')
        index += 1
    f.close()


import string
filename = 'Missions.txt'
f = codecs.open(filename, 'r',"utf-8")
res = codecs.open('new1.txt','wb',"utf-8")
data = f.readlines()
for i in data:
    if 'MissionName' in i:
        name = i.replace('MissionName=','').replace("\r\n",'') + u' - Задание в Borderlands 2' + "\r\n"
    if 'MissionDescription' in i:
        print i
        desc = i.replace('MissionDescription=',u'==Описание==\r\n')
        res.write(desc)
    if 'MissionSummary' in i:
        summ = i
        #res.write(i)
    if 'MissionGiver' in i:
        giver = i
        #res.write(i)

res.close
f.close



print

