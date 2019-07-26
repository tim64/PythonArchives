#!/usr/bin/env python
# -*- coding: utf-8 -*-


def strTOlist(str):
    list=[]
    for i in range(len(str)):
        list.append(str[i])
    return list


def  listTOstr(list):
    s=""
    for i in range(len(list)):
        s+=str(list[i])
    return s



def asc(str):
    res=[]
    for i in str:
        res.append(bin(ord(i)))
    return res



def trash(text):
    sings="'\n !@#$-%^&*:-()_+""�;:?=-{}[]:"";,./\|''"
    text=text.replace(' ','')
    for char in text:
        if sings.find(char)>-1:
            text=text.replace(char,'')
    return text


