# -*- coding: utf-8 -*-

import random
import time
import matplotlib.pyplot as plt

def rc4(data, key):
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]

    x = 0
    y = 0

    out = []

    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)



def graph():
    sum = 0;
    times = []
    data = open('ord.txt','r').read()
    #lens = [128,256,384,512,640,768,896,1024,1152,1280,1408,1536,1664,1792,1920,2048]
    lens=range(16,2048,16)
    #data = '13400926346449544144918997350269500821426995731447760841574280413362379687440608193568511167153008725503505749489691800433536622562264947773563259316081113'
    #data = str(random.getrandbits(1024))

    for l in lens:
        start = time.clock()
        key = str(random.getrandbits(l))
        #c = rc4(data, key)
        #d = rc4(c,key)
        elapsed = time.clock() - start
        times.append(elapsed)
    #plt.title('All operations (32-2048)' )
    plt.xlabel('Length')
    plt.ylabel('sec')
    #plt.xticks(lens)
    plt.plot(lens,times)

    plt.show()

print rc4("tim3232","ivan312")






