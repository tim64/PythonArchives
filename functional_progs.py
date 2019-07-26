# -*- coding: utf-8 -*-

#Время функции с помощью декоратора

import time

def timer(f):
    def tmp(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        print "Worktime: %f" % (time.time()-start)
        return res

    return tmp

@timer
def fac(n):
     if n == 0:
          return 1
     return fac(n-1) * n

fac(100) # Print worktime



