from Crypto.Cipher import AES
import base64
import os
import random
import time
import matplotlib.pyplot as plt
from numpy import *



def crypt(data, key, mode):
    encryptor = AES.new(1,key, mode)
    ciphertext = encryptor.encrypt(data)
    return ciphertext

def test():
    import random
    t=0
    mode = AES.MODE_CBC
    data = '123456789'*1024
    keys = ['1t4t68jio1y56fnc','gutmbdrqvhty6716409nutlf','tujfnrhesyjkurhndbxtyzvaq675890y']
    lens = [16,24,32]
    #lens=range(32,1024,16)
    #m = random.getrandbits(256)
    times = []

    for key in keys:
        for i in range(100):
            start = time.clock()
            crypted_text = crypt(data, key, mode)
            elapsed = time.clock() - start
            print t
            t += elapsed
        print t
        times.append(round((t/100)*1000,3))
        t = 0



    #print times
    plt.xlabel('Length, byte')
    plt.ylabel('Time, s')
    plt.grid()
    plt.xticks(lens)
    plt.yticks(times)
    plt.plot(lens,times)
    plt.show()

test()
