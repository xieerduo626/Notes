import numpy as np
from intervals import Interval
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import math as m


a = np.loadtxt('distrubution.csv', delimiter=",", skiprows=1)
size0=a[:,1]

sort=np.sort(size0)
n=np.size(sort)


plt.rcParams["font.family"] = "sans-serif"

x=range(1,n+1)
y=sort
fig, ax = plt.subplots()

hfont = {'fontname':'Helvetica'}
ax.scatter(x,y,s=0.5)
ax.set_xlim(0, 900)
ax.set_ylim(1, 100000)
ax.set_title('Size Distrubution of Corn Stem Cells',fontsize=18, **hfont)
ax.set_xlabel('Cell Number',fontsize=14,**hfont)
ax.set_ylabel(r'Cell Size($\mu m^2$)',fontsize=14,**hfont)

ax.minorticks_on()
plt.yscale('log')
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)

#linear fit
logsize=np.log(sort)
xsmall=x[0:600]
sizesmall=logsize[0:600]

bsmall, msmall = polyfit(xsmall, sizesmall, 1)

ax.plot(x,np.exp(bsmall+msmall*x),color='red', linewidth=0.5, label="Small Type")
logsize=np.log(sort)
xbig=x[600:n]
sizebig=logsize[600:n]
bbig, mbig = polyfit(xbig, sizebig, 1)
ax.plot(x,np.exp(bbig+mbig*x),color='orange', linewidth=0.5, label="Big Type")

ax.legend(loc=2)

plt.show()
