import numpy as np

def maxmul(a):
	h = a[0].shape[0]
	for i in a:
		if i.shape[0] != i.shape[1] or i.ndim != 2 or i.shape[0] != h:
			return None
	res = np.eye(a[0].shape[0])
	for i in range(len(a)):
		res = res@a[i]
	return res

a = np.eye(3)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
c=np.array([[1,0,0],[0,1,0],[0,0,1]])
print(a,b,c)
print(maxmul(list((a,b,c))))
