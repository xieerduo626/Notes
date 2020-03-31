import numpy as np
from intervals import Interval
from matplotlib import rcParams
import matplotlib.pyplot as plt
import math as m
from PIL import Image
from scipy.optimize import curve_fit
import matplotlib.patches as mpatches


a = np.loadtxt('Values#2.csv', delimiter=",", skiprows=1)

x=a[:,0]
y=a[:,1]


b = sum(x * y) / sum(y)
c = np.sqrt(sum(y * (x - b)**2) / sum(y))

def Gauss(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2 * c**2))

popt,pcov = curve_fit(Gauss, x, y, p0=[max(y), b, c])

a,b,c=popt


fig, ax = plt.subplots()

rcParams['font.family']='sans-serif'
rcParams['font.sans-serif']=['Helvetica']

ax.set_xlim(0, 500)
ax.set_ylim(0, 230)
p1=ax.plot(x, y,color='black', linewidth=1.0, label='data')
p2=ax.plot(x, Gauss(x, *popt), 'r-', linewidth=0.7,label='fit')
plt.legend(
ax.set_xlabel("Distance(pixels)")
ax.set_ylabel("Grey Value(a.u.)")

plt.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)

plt.savefig("Q8figure1.png",bbox_inches='tight',transparent=True,dpi=500)

plt.show()

'''title="The fit parameters: a=%s,b=%s,c=%s"%(a,b,c)
ax.set_title(title)'''
