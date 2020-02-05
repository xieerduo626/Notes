import numpy as np
from intervals import Interval
import matplotlib.pyplot as plt
import math as m

a = np.loadtxt('distribution.csv', delimiter=",", skiprows=1)
size0=a[:,1]
size=np.log(size0)

maxValue = np.amax(size)
minValue = np.amin(size)
d=(maxValue-minValue)/80
sort=np.array([0,0])


for i in range(0,80):
    count = 0
    for b in size:
            if b>= (minValue + i*d) and b < (minValue+(i+1)*d):
                count +=1
            else:
                count +=0
    cellsize=minValue+(i+0.5)*d
    sort=np.vstack([sort,[count,cellsize]])


x=sort[:,0]
y=np.exp(sort[:,1])
fig, ax = plt.subplots()

ax.scatter(x,y)
ax.set_xlim(0, 43)
plt.yscale('log')
plt.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.legend()
plt.show()

