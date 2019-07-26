# -*- coding: utf-8 -*-
import rsa
from rsa.bigfile import *
import random
import time
import timeit
import matplotlib.pyplot as plt
"""
(pub_key, priv_key) = rsa.newkeys(128)
infile = open('ord.txt','r')
outfile = open('result.txt','w')
encrypt_bigfile(infile, outfile, pub_key)

"""

infile = open('ord.txt','r')
outfile = open('result.txt','w')
"""
#Обычное шиФрование
times=[]
lens = [128,256,384,512,640,768,896,1024]
print lens
for i in lens:
    print i
    start = time.clock()
    (pub_key, priv_key) = rsa.newkeys(i)
    encrypt_bigfile(infile, outfile, pub_key)
    elapsed = time.clock() - start
    times.append(round(elapsed,3))
print times
plt.xlabel('Length')
plt.ylabel('sec')
plt.xticks(lens)
plt.plot(lens,times)
plt.show()
"""

def test():
    (pub_key, priv_key) = rsa.newkeys(1024)
    start = time.clock()
    print start
    infile = open('ord.txt','r')
    outfile = open('result.txt','w')
    encrypt_bigfile(infile, outfile, pub_key)
    elapsed = time.clock() - start
    print elapsed



"""
lens = [256,512,1024,2048]
times1=[7.43,14.62,21.82,28.95]
#plt.xlabel('Length, bit')
#plt.ylabel('Time, s')
plt.grid()
plt.xticks(lens)
plt.yticks(times)
plt.plot(lens,times1,'ro-')
plt.show()
"""
print 'HELLO' ^ 'KEYKE'