import numpy as np
from intervals import Interval
from matplotlib import rcParams
import matplotlib.pyplot as plt
import math as m
from PIL import Image
from scipy.optimize import curve_fit
import matplotlib.patches as mpatches
from scipy.signal import find_peaks



a = np.loadtxt('powderpattern_Ni.csv', delimiter=',', skiprows=1)
x1=a[:,0]
y10=a[:,1]
y1 = 100 * y10/np.max(y10)
b = np.loadtxt('ICSD reference data/NiGe_ICSD_Pbnm.csv', delimiter=',', skiprows=1)
x2=b[:,0]
y20=b[:,1]
y2 = 100 * y20/np.max(y20)
c= np.loadtxt('powderpattern_Ge.csv', delimiter=',', skiprows=1)
x3=c[:,0]
y30=c[:,1]
y3 = 100 * y30/np.max(y30)



fig, ax = plt.subplots()

rcParams['font.family']='sans-serif'
rcParams["legend.fancybox"] = False
rcParams['font.sans-serif']=['Helvetica']

#peaks, _ = find_peaks(y, height= 10)
ax.set_xlim(20, 100)
ax.set_ylim(0, 110)
ax.plot(x1, y1, linewidth=1.0, label='Ni')
#ax.plot(x2, y2, linewidth=1.0, label='Expected NiGe')
ax.plot(x3, y3, linewidth=1.0, label='Ge')
#ax.plot(x[peaks], y[peaks], "x")
ax.set_xlabel(r"$2\theta$(degrees)",size=14)
ax.set_ylabel("Intensity(a.u.)",size=14)

plt.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.legend()
plt.savefig("Mix.png",bbox_inches='tight',transparent=True,dpi=500)
plt.show()
