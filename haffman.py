# -*- coding: utf-8 -*-


def f_alpha(text):
    from MyString import trash,strTOlist
    close=trash(text)
    close=close.lower()
    a=0.0
    letters=[]
    from string import ascii_lowercase as alpha
    res=[]
    for i in range(len(alpha)):
        res.append(0.0)
    
    #alpha="אבגדהו¸זחטיךכלםמןנסעףפץצקרשתûü‎‏ÿ"
    
    al=strTOlist(alpha)
    for i in range(len(text)):
        for char in alpha:
            letters.append(char)
            a=text.count(char)
            res[alpha.find(char)]=a
                
                
    return res

text = open('ord.txt','r').read() 


def form_graph(massive):
    massive = massive.sort
    print massive
    """
    for i in massive:
        first=min(massive)
        massive.remove(first)
        second=min(massive)
        massive.remove(second)
        new=first+second
       """ 
form_graph(f_alpha(text))