import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
from matplotlib import rcParams
import math as m

#Font
plt.rcParams["font.family"] = "sans-serif"
hfont = {'fontname':'Helvetica'}

#legend
rcParams["legend.fancybox"] = False

#data
x = np.linspace(0,1.2,121)
nd = np.exp((0.27-x)*38.64)
n0 = 1
na = np.exp((x-0.51)*38.64)
ynd = nd/(nd+n0+na)
yn0 = 1/(nd+n0+na)
yna = na/(nd+n0+na)



#plot
fig, ax = plt.subplots()
ax.plot(x,ynd, linewidth=1.5, label="+ state")
ax.plot(x,yn0, linewidth=1.5, label="neutral state")
ax.plot(x,yna,linewidth=1.5, label="- state")
ax.set_xlim(-0.2, 1.4)
ax.set_ylim(-0.05,1.05)
plt.xticks([0, 0.27, 0.51, 1.2],["Ev", "Ed", "Ea", "Ec"]) 
plt.plot([0.27,0.27], [-0.1,0.5],'--',linewidth=0.5,color='black')
plt.plot([0.51,0.51], [-0.1,0.5],'--',linewidth=0.5,color='black')
plt.plot([-0.2,0.51], [0.5,0.5],'--',linewidth=0.5,color='black')

#ax.set_title('Size Distrubution of Corn Stem Cells',fontsize=18)
ax.set_xlabel(r'E$_f$(eV)',fontsize=14)
ax.set_ylabel('Density',fontsize=14)


#design
#ax.minorticks_on()
ax.legend(borderaxespad=0,edgecolor='black',loc=1)
ax.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.show()
