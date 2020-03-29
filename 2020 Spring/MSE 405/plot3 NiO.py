import numpy as np
from intervals import Interval
from matplotlib import rcParams
import matplotlib.pyplot as plt
import math as m
from PIL import Image
from scipy.optimize import curve_fit
import matplotlib.patches as mpatches
from scipy.signal import find_peaks



a = np.loadtxt('NiO.csv', delimiter=',', skiprows=1)
x=a[:,0]
y=a[:,1]


fig, ax = plt.subplots()

rcParams['font.family']='sans-serif'
rcParams["legend.fancybox"] = False
rcParams['font.sans-serif']=['Helvetica']

peaks, _ = find_peaks(y, height= 25, distance= 40)

ax.set_xlim(10, 100)
ax.set_ylim(0, 250)
ax.plot(x, y,color='black', linewidth=1.0, label='data')
#ax.plot(x[peaks], y[peaks], "x")
ax.set_xlabel(r"$2\theta$(degrees)",size=14)
ax.set_ylabel("Intensity(a.u.)",size=14)

plt.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)

plt.savefig("Q4NiO.png",bbox_inches='tight',transparent=True,dpi=500)
plt.show()
print(x[peaks],y[peaks])

