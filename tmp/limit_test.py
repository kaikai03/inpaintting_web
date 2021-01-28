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


for i in range(1, 50):
    start = time.time()
    print(i, fab(i), time.time()-start)



stamp = int(time.mktime(time.strptime('2020-01-01','%Y-%m-%d')))
stamp2 = int(time.mktime(time.strptime('2036-04-01','%Y-%m-%d')))
stamp2 - stamp

np.exp(stamp2/stamp)

diff = np.log(np.exp(stamp2*0.1**8) / np.exp(stamp*0.1**8))

x = np.array([0.001, 0.316224, 0.63158, 0.9469, 1.2623,1.57852])

plt.plot(np.linspace(1,len(x),len(x)),x)
plt.show()



# mu=4
# mean,var,skew,kurt = st.poisson.stats(mu,moments='mvsk')
# x = np.arange(st.poisson.ppf(0.01, mu),st.poisson.ppf(0.99, mu))
#
# plt.plot(x, st.poisson.pmf(x, mu),'o')
# plt.show()


int(str(time.time())[-1]) >= 7
count = 0
for i in range(1, 400000):
    if int(str(time.time())[-1]) >= 9 * (1/((np.e**(diff*2)/(np.e**(diff*2)++3.567))+0.3267)):
        if int(str(time.monotonic())[-1]) >= 9:
            count+=1
print(count/400000)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
import sklearn.gaussian_process.kernels as kl

a1=np.random.normal(1, 1.5, 50).reshape(50,1)
# a2=np.random.normal(10.6, 8.6, 50).reshape(50,1)

# b=a1-np.random.random(5).reshape(5,1)
b=np.random.laplace(2,1.1,50).reshape(50,1)
# plt.scatter(a1,b,marker = 'o', color = 'r', label='3', s = 15)
# plt.show()



gaussian=GaussianProcessRegressor(kernel=kl.RBF(5.0,length_scale_bounds='fixed'))
fiting=gaussian.fit(a1,b)

gaussian.get_params(True)

# c=np.linspace(a1.min()-0.1,a1.max()+0.1,50)
c=np.linspace(a1.min(),a1.max(),20)
d=gaussian.predict(c.reshape(20,1),True)
plt.scatter(a1,b,marker = 'o', color = 'r', label='3', s = 15)
plt.plot(c,d[0])
plt.plot(c,d[0]+(d[1]*200).reshape(20,1))
plt.plot(c,d[0]-(d[1]*200).reshape(20,1))
plt.show()

