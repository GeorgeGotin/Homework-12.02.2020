import numpy as np
import matplotlib.pyplot as plt

def fun(x):
	return x**2

def creat(f,a,b):
	x = np.arange(a-0.001,b,0.001)
	y = list(map(f,x))
	fig = plt.figure()
	a = fig.add_subplot()
	a.grid(axis='both')
	a.set_title('My first graffic')
	a.plot(x,y,'+--')
	plt.show()

creat(fun,-3,3)


