# coding: utf-8

import time
import numpy as np

# start = time.time()
# time.sleep(1)
# print(time.time()-start)

def fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fab(n - 1) + fab(n-2)


def fab2(n):
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


for i in range(1, 50000):
    start = time.time()
    print(i, fab2(i), time.time()-start)



stamp = int(time.mktime(time.strptime('2020-10-10','%Y-%m-%d')))
stamp2 = int(time.mktime(time.strptime('2023-12-12','%Y-%m-%d')))
stamp2 - stamp

np.exp(stamp2/stamp)

np.log(np.exp(stamp2*0.1**8) / np.exp(stamp*0.1**8))



