# -*- coding: utf-8 -*-



def simple_crypt(open):
    open.lower
    res=""
    alpha="אבגדהו¸זחטיךכלםמןנסעףפץצקרשתûü‎‏ÿ"
    alpha_crypt="ו¸ךכאמדלםÿü‎‏בעףפץצקןנזחטיהסשתûרג"
    for char in open:
        char = alpha_crypt [alpha.find(char)]
        res = res + char
    outfile.write(res)
    return res

def f_alpha(close):
    from MyString import trash
    close=trash(close)
    close=close.lower()
    a=0.0
    from string import ascii_lowercase as alpha
    res=[]
    for i in range(len(alpha)):
        res.append(0.0)
    
    #alpha="אבגדהו¸זחטיךכלםמןנסעףפץצקרשתûü‎‏ÿ"
      
    for i in range(len(close)):
        for char in alpha:
            a=float(close.count(char))/len(close)
            res[alpha.find(char)]=round((a*100),5)
                              
    return round(res,4)


text = open('ord.txt','r').read() 
print f_alpha(text)

