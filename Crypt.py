#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string
import time
import math
import Method
import sys



def ceasar_code(str,n):
    str.lower
    from string import ascii_lowercase as alpha
    res =""
    for char in str:
        if char==' ':
            res = res + char
        if char in alpha:
            char = alpha [(alpha.find(char) + n) % 26]
            res = res + char
    return res

#file = open('ord.txt','r').read()
#text = ceasar_code(file ,3)
#print text
def ceasar_decode(str,n):
    res =""
    for char in str:
        if char in alpha:
            char = alpha [(alpha.find(char) - n) % 26]
            res = res + char
    return res


#print ceasar_code(text,6)


def ceasar_hack(str):
    #dic = open('dic.txt','r').read()
    dic = open('dic_en.dic','r').read()
    res=""
    from string import ascii_lowercase as alpha
    for i in range(26):
        #tmp=ceasar_code(alpha,i)
        for char in str:
            if char in alpha:
                char = alpha [(alpha.find(char) - i) % 26]
                res = res + char
        if dic.find(res)>0:
            res=""

    return 0

#ceasar_hack('cuxrj')

#--------------------------- ----------------------------------------------------------

def fullkey(key,n): #    ost=n % len(key) #    mno=n/len(key)
    if ost==0:
        return key*mno #
    fullkey=key*int(mno)
    raz=n-len(fullkey)
    return fullkey+key[0:raz]

def vigener_code(open,key): #   from MyString import trash
    open=trash(open)
    open=open.lower()
    res=""
    from string import ascii_lowercase as alpha
    #alpha=''
    key=fullkey(key,len(open))
    i=0
    for char in key:
        n=alpha.find(char)
        tmp=alpha [(alpha.find(open[i]) + n) % 26] #   n
        res = res +tmp
        i=i+1
    return res

#text = open('ord.txt','r').read()
#print vigener_code(text,'crypto')



def vigener_decode(close,key): #
    res=""
    from string import ascii_lowercase as alpha
    key=fullkey(key,len(close))
    i=0
    for char in key:
        n=alpha.find(char)
        tmp=alpha [(alpha.find(close[i]) - n) % 26]
        res = res +tmp
        i=i+1
    return res


#-------------    --------------------------

def gen_key(open): #      import random
    key=""
    for i in range(len(open)):
        r_key=random.uniform(97,122)
        i_key=int(r_key)
        key+=chr(i_key)
    return key

def vigener_code_genkey(open): #   from MyString import trash
    open=trash(open)
    open=open.lower()
    res=""
    from string import ascii_lowercase as alpha
    key=gen_key(open)
    i=0
    for char in key:
        n=alpha.find(char)
        tmp=alpha [(alpha.find(open[i]) + n) % 26] #   n
        res = res +tmp
        i=i+1
    return res,key

def vigener_decode_genkey(open,key): #    from MyString import trash
    open=trash(open)
    open=open.lower()
    res=""
    from string import ascii_lowercase as alpha
    i=0
    for char in key:
        n=alpha.find(char)
        tmp=alpha [(alpha.find(open[i]) - n) % 26] #   n
        res = res +tmp
        i=i+1
    return res,key



#-------------  ------------------------------
#from time import *
def simple_gen():

    mno=int(raw_input(' (10-1000000) = ?'))
    key1=int(raw_input('press'))
    tmp1=clock()*key1
    key2=int(raw_input('press'))
    tmp2=clock()*key2
    key3=int(raw_input('press'))
    tmp3=clock()*key3
    res=tmp1+tmp2+tmp3
    return round(res*mno)

#print simple_gen()


#-------------  --------------------------------------------------

def simple_crypt(open):
    open.lower
    res=""
    alpha=""
    alpha_crypt=""
    for char in open:
        char = alpha_crypt [alpha.find(char)]
        res = res + char
    return res

#print simple_crypt("

#------------ ---------------------------------------------------

def f_alpha(close):
    from MyString import trash
    close=trash(close)
    close=close.lower()
    a=0.0
    from string import ascii_lowercase as alpha
    res=[]
    for i in range(len(alpha)):
        res.append(0.0)


    for i in range(len(close)):
        for char in alpha:
            a=float(close.count(char))/len(close)
            res[alpha.find(char)]=round((a*100),5)


    return res

#text = open('ord.txt','r').read() # rint f_alpha(text)




""

#------------------- ----------------------------------
#text = open('ord.txt','r').read()

def translite(text):
    res=""
    alpha_tr="abvgdeejziyklmnoprstufhcchh'i'eua"
    alpha=""
    alpha_b=""
    alpha_tr_b="ABVGDEEJZIYKLMNOPRSTUFHCCHH'I'EUA"
    for char in text:
        if alpha_b.find(char)>0:
                if not (alpha_b.find(char)>0):
                    char=char
                elif char=="":
                    char="Ch"
                elif (char=="") or (char==""):
                    char="Sh"
                elif (char==""):
                    char="Ya"
                else:
                    pos=alpha_b.find(char)
                    char=alpha_tr_b[pos]

        else:
            if not (alpha.find(char)>0):
                char=char
            elif char=="":
                char="ch"
            elif (char=="") or (char==""):
                char="sh"
            elif (char==""):
                char="ya"
            else:
                pos=alpha.find(char)
                char=alpha_tr[pos]
        res=res+char
    return res

#outfile = open("result.txt", 'w')
#outfile.write(translite(text))
#print translite("   ")


#-------------------------RSA-------------------------------------
# f secret_D(a,b,ph):
    import random
    from Method import friend
    for i in range(100):
        d=int(random.uniform(a,b))
        if friend(d,ph)==True:
            return d


def rsa_keys(p,q,e):
    openkey=[e]
    closekey.append(d)
    closekey.append(n)
    return openkey,closekey

def rsa_code(m,p,q,n,e):
    from Method import power
    n=p*q
    s=power(m,e)%n
    return s

def rsa_uncode(x,d,n):
    from Method import power
    c=power(x,d)%n
    return c



def rsa():
    m=int(raw_input('Enter open text '))
    p=int(raw_input('Enter P '))
    q=int(raw_input('Enter Q '))
    n=p*q
    print 'N = ',n
    e=int(raw_input('Enter e '))
    open,close=rsa_keys(p,q,e)
    d=close[0]
    print d
    x=rsa_code(m,p,q,n,e)
    print '.'
    print '.',x
    print '.'
    print ''
    raw_input('Press Enter')
    print rsa_uncode(x,close[0],n)
    return 0

#print rsa()
#---------------------- -------------------------------------

def verman(open):
    from MyString import asc
    s=""
    a=asc(open)
    key=gen_key(open)
    b=asc(key)
    for i in range(len(open)):
        x=((a[i]^b[i])*3)
        print x
        s+=chr(x)
    print "Key : ",key
    print "Code : ",s
    return s

#verman('tim')
#------------  -------------------------------------



def N_letter(text,n):
    i=0
    res=''
    for char in text:
        i=i+1
        if i%n==0:
            print i
            res+=char

    return res

#text = open('ord.txt','r').read()
#print N_letter(text,6)
#---------- ------------------------------

def sigma_down(text):
    import random
    sigma=[]
    n=len(text)
    for i in range(n):
        sigma.append(-1)
    k=0
    for i in range(500):
        buf=int(random.uniform(0,n))

        if sigma.count(buf)==0:
            sigma[k]=buf
            k+=1

        if sigma.count(-1)==0:
            break
    return sigma

def sigma_up(text):
    import random
    pos=[]
    n=len(text)
    for i in range(n):
        pos.append(-1)
    k=0
    for i in range(500):
        buf=int(random.uniform(0,n))

        if pos.count(buf)==0:
            pos[k]=buf
            k+=1

        if pos.count(-1)==0:
            break
    return pos

def zigzag(text):
    from MyString import listTOstr
    up=sigma_up(text)
    down=sigma_down(text)
    print up
    print down
    for char in text:
        text=text.replace(char,char+' ') #   text=text.split() #
    for i in range(len(text)):
        buf=text[up[i]]
        text[up[i]]=text[down[i]]
        text[down[i]]=buf

    return listTOstr(text)

def perestanovka(text):
    close=''
    import random
    l=len(text)
    close=zigzag(text)
    return close

#print perestanovka('janna')

#------------ ----------------------------------

def indexC(text):
    from string import ascii_lowercase as alpha
    m=[]
    c=[]
    n=len(text)
    letters=''
    a=0
    sum=0.0
    for char in alpha:
        if letters.find(char)==-1:
            letters+=char
            m.append(char)
            c.append(text.count(char))
    for i in range(25):
        a=c[i]*(c[i]-1)
        sum+=a

    index=sum/(n*(n-1))

    return round(index,4)


#text = open('ord.txt','r').read()
#print ",indexC(text)

#--------- -----------------------------

def entropia(): # 0< = H(x) <= log2(n)
    #p=[]
    n=int(raw_input(' '))
    H=0.0
    tmp=0.0
    for i in range(n):
        p=float(raw_input('P'+str(i)+' :'))
        if p==0:
            tmp=0
        tmp=p*math.log(p,2)
        H+=tmp

    print (-1)*H




#---------------------------------------------------


def mkpass(size):
    chars = []
    chars.extend([i for i in string.ascii_letters])
    chars.extend([i for i in string.digits])
    chars.extend([i for i in '\'"!@#$%&*()-_=+[{}]~^,<.>;:/?'])

    passwd = ''

    for i in range(size):
        passwd += chars[random.randint(0,  len(chars) - 1)]
        random.seed = int(time.time())
        random.shuffle(chars)

    return passwd

#print mkpass(12)

#--------------------------------------
def gen_simple(m):
    y=0
    while y<>1:
        x=random.randint(pow(2,m)/2,pow(2,m))
        return x


#print gen_simple(16)

#----------------------------------------------------------------

def el_gamal_gen(): #  | ,g,y)|
    p=gen_simple(16)
    g=Method.p_Sqrt(p)
    x=random.randint(1,p)
    y=(pow(g,x))%p
    return p,g,y,x

#print el_gamal_gen()


def el_gamal_code(m):
    p,g,y,x=el_gamal_gen()
    k=random.randint(1,p-2)
    a=pow(g,k)%p
    b=pow(y,k)%p
    return a,b,x,p

def el_gamal_decode(a,b,x,p):
    return b*pow(pow(a,x),-1)%p

print el_gamal_code(12)

def del_hel_A():
    from Method import p_Sqrt,powmod

    a=random.randint(2^256,2^512)
    p=gen_simple(128)
    g=p_Sqrt(p) # .
    A=powmod(g,a,p)

    return g,p,A

#print del_hel_A()




