# coding: utf-8

import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

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

np.log(np.exp(stamp2*0.1**8) / np.exp(1602259200*0.1**8))

x = np.array([0.001, 0.369792000, 0.739584, 1.000512, 1.3167360,1.632096])



mu=4
mean,var,skew,kurt = st.poisson.stats(mu,moments='mvsk')
x = np.arange(st.poisson.ppf(0.01, mu),st.poisson.ppf(0.99, mu))

plt.plot(x, st.poisson.pmf(x, mu),'o')
plt.show()


int(str(time.time())[-1]) >= 7
count = 0
for i in range(1, 200000):
    if int(str(time.time())[-1]) >= 9 * (1/x[3]):
        if int(str(time.monotonic())[-1]) >= 9:
            count+=1
print(count/200000)

