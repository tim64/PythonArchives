#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lineS(x,h):
    lenX = len(x)-1
    lenH = len(h)-1
    output = ''
    output2 =''
    y = []
    sum = 0
    tmp = 0
    for n in range(lenX+lenH+1):
        if n == 0:
            sum = x[n]*h[0]
            output = 'x[0]*h[0] = '+ str(x[0]) + ' * ' + str(h[0])+'  '
        else:
            output = ''
            output2 = ''
            for i in range(n+1):
                output +='x['+str(i)+']'+' * h['+str(n-i)+'] + '
                if (n-i > lenH or i > lenX):
                    tmp = 0
                    output2 += ''
                else:
                    output2 += str(x[i]) + ' * ' + str(h[n-i]) +' + '
                    tmp = x[i]*h[n - i]
                    sum += tmp
        output = output[0:-2]
        output2 = output2[0:-2]
        output = 'y['+str(n)+'] = '+ output +' = ' + output2 + ' = '+str(sum)
        print output
        y.append( '%2.4f' %(sum))
        sum=0
    print 'y = ',y
    return 0

def listplus(lst1,lst2):
    for i in lst2:
        lst1.append(i)
    return lst1

def circleS(x,h):
    lenX = len(x)-1
    lenH = len(h)-1
    lenY = lenX+lenH+1
    part =''
    result = ''
    sum = 0
    tmp = 0
    if (lenY > lenH):
        tail = lenY - lenH
        buf = [0]*tail
        h = listplus(h,buf)
    if (lenY > lenX):
        tail = lenY - lenX
        buf = [0]*tail
        x = listplus(x,buf)
    y=[0]*lenY
    N = len(y)
    for n in range(N):
        for i in range(N):
            tmp = x[i]*h[n-i]
            sum += tmp
            part += 'x['+str(i)+']'+' * h['+str(n-i)+'] + '
            result += str(x[i]) + ' * ' + str(h[n-i])+' + '
        part = 'y['+str(n)+'] = ' + part[:-2]
        part += ' = ' + result[:-2] + ' = ' + str(sum)


        print part
        part = ''
        result =''
        #output = output[0:-2]
        #output2 = output2[0:-2]
        #result = output + '='  + str(sum)
        #result = 'y['+str(n)+'] = '+ result
        #print result
        #result = ''
        y[n]='%2.4f' %(sum)
        sum=0
    print y
    return
x1=0.3
x2=-0.5
x3=0.16



def hnt(x1,x2,x3,n):
    h=[0.0]*n
    h[0]=x1
    print 'h[0] = ',h[0]
    for i in range(1,n):
        h[i] = (x2 * h[i-1]) + (x3 * h[i-2])
        print 'h[',i,'] = ('+str(x2)+' * h[',i-1,']) + ('+str(x3)+' * h[',i-2,']) = ',(x2 * h[i-1]),' + ',(x3 * h[i-2]),' = ',h[i]
    print h
    return h

h=hnt(x1,x2,x3,15)
x=[0.8, 0.1, 0.6]
circleS(x,h)

def yraz(x,n):
    y = [0.0]*n
    buf = 0.0
    for i in range(n):
        if (i>len(x)-1):
            x1=0
        else:
            x1 = x[i]
        if (i-1 <0 ):
            y1=0
        else:
            y1 = y[i-1]
        if (i-2 <0):
            y2=0
        else:
            y2 = y[i-2]

        tmp = (0.3 * x1) - (0.5 * y1) + (0.16 * y2)
        y[i] = tmp
        print 'y[',i,'] = (0.3 * x[',i,']) - (0,5 * y[',i-1,']) + (0.16 * y[',i-2,']) = ',(0.3 * x1) ,' - ',(0.5 * y1),' + ',(0.16 * y2),' = ',y[i]
    for i in range(len(y)):
        buf = '%1.3f' %(y[i])
        y[i] = buf
    print y
    return y




def quant(n,e):
    import math
    buf = 1
    bin = []
    if n > 0:
        bin.append(1)
        print n,'  1'
    else:
        bin.append(0)
        print n,'  0'
        n = abs(n)
    for i in range(e):
        n *= 2
        bin.append(int(n))
        print n,' ',int(n)
        n , integer = math.modf(n)
    n *= 2
    n = int(n)
    if n == 0:
        print bin
        return bin
    else:
        print 'add 1!'
        print bin
        return bin


def acc(n):
    bin = [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1]
    tmp = 0
    output = ''
    output2 = ''
    for i in range(1,len(bin)):
        if bin[i]==0:
            tmp= tmp
        if bin[i]==1:
            output = output + '2^('+str((-1)*i)+')+ '
            output2 = output2 + str(2**((-1)*i)) + ' + '
            tmp += 2**((-1)*i)
    output = output[0:-2]
    output2 = output2[0:-2]
    print output + '= ' + output2 + '= ' + str(tmp)
    delta = abs(n - tmp)
    print delta
    sigma = (delta/n)*100
    print '%1.4f' %(sigma),'%'
    return

def accH(old, new):
    import math
    sum=0
    sumshow =''
    deltas = []
    sigmas = []
    for i in range(len(old)):
        deltas.append(abs(new[i]-old[i]))
        print 'd[',i,'] = |',new[i],' - ',old[i],'| = ',deltas[i]
        sigmas.append((deltas[i]/old[i])*100)
        print 's[',i,'] = d[',i,'] / ',old[i],' * 100 = ',sigmas[i]
    for sig in sigmas:
        sum += sig**2
        sumshow += str(sig) +'^2 + '
    sum = math.sqrt(sum)
    print 'sqrt('+sumshow[:-2]+')'
    print 'SumSig = ',sum
    return



#accH(hnt(x1,x2,x3,15), hnt(x4,x5,x6,15))
import string

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
    "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq " \
    "rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu " \
    "ynnjw ml rfc spj."

table = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

print original.translate(table)

