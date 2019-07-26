# -*- coding: utf-8 -*-

from string import ascii_lowercase as alpha
indexes = range(25)



def oneletter(text, letter):
    return text.count(letter)

def friq(text):
    f_text = []
    from MyString import trash
    text=trash(text)
    text=text.lower()
    size = len(text)
    from string import ascii_lowercase as alpha
    for let in alpha:
        f_text.append(((oneletter(text,let)*1.0)/size)*100)
    return f_text



text = open('ord.txt','r').read()
print friq(text)