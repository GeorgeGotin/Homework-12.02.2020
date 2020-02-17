import numpy as np
import matplotlib.pyplot as plt
import random

def fun(x):
	return 3*x**2 + 2*x + 1




def contrsqr(x,y):
	res = x.transpose()
	res = res @ x
	res = np.linalg.inv(res)
	res = res @ x.transpose()
	res = res @ y
	return res


h = np.arange(-10,10,0.1)
y = np.array(list(map(fun,h)))
for i in range(len(y)):
	y[i] = y[i] + random.uniform(-10,10)
x = np.array(list((list(map(lambda x:x**2,h)),h,[1 for i in np.arange(-10,10,0.1)])))
c=contrsqr(x.transpose(),y.transpose())

xs=np.arange(-10,10,0.1)
ys=np.array(list(map(lambda x:c[0]*x**2+c[1]*x+c[2],xs)))

fig = plt.figure()
a = fig.add_subplot()
a.grid(axis='both')
a.plot(list(xs),list(ys))
a.plot(h,y,'o')
plt.show()




