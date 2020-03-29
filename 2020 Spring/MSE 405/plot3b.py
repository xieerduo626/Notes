import numpy as np
from intervals import Interval
from matplotlib import rcParams
import matplotlib.pyplot as plt
import math as m
from PIL import Image
from scipy.optimize import curve_fit
import matplotlib.patches as mpatches
from scipy.signal import find_peaks


a = np.loadtxt('Q3b.csv', delimiter=",", skiprows=1)

x=a[:,0]
y=a[:,1]

peaks, _ = find_peaks(y, distance=100)


fig, ax = plt.subplots()

rcParams['font.family']='sans-serif'
rcParams["legend.fancybox"] = False
rcParams['font.sans-serif']=['Helvetica']

#ax.set_xlim(0, 0.7)
ax.set_ylim(0, 260)
ax.plot(x, y,color='black', linewidth=1.0, label='data')
ax.plot(x[peaks], y[peaks], "x")
ax.set_xlabel("Distance(pixels)",size=14)
ax.set_ylabel("Intensity(a.u.)",size=14)

plt.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)

plt.savefig("Q3.png",bbox_inches='tight',transparent=True,dpi=500)
plt.show()
position=x[peaks]
print(position)
