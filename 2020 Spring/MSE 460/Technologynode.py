import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
rcParams['font.family']='sans-serif'
rcParams["legend.fancybox"] = False
rcParams['font.sans-serif']=['Helvetica']
rcParams["errorbar.capsize"]= 3

x=np.arange(5)
y=np.array([3.9,3.7,2.85,2.15,1.5])
err=np.array([0,0.2,0.15,0.2,0.5])


fig, ax = plt.subplots()
ax.errorbar(0, 3.9, 0,fmt='o',ms=8,label=r'SiO$_2$')
ax.errorbar(1, 3.7, 0.2,fmt='s',ms=8,label='Fluorosilicate glass(FSG)')
ax.errorbar(2, 2.85, 0.15,fmt='p',ms=8,label='SiOH')
ax.errorbar(3, 2.15, 0.2,fmt='*',ms=8,label='p-SiOH')
ax.errorbar(4, 1.5, 0.5,fmt='h',ms=8,label='Sillica xerogels, air gap')
ax.plot(x,y,linewidth=1)

ax.set_ylim(0.5, 4.5)
plt.xticks(np.arange(5),('before 180nm', '180nm,130nm', '90nm,65nm', '45nm,32nm,22nm', '14nm & after'))
plt.yticks(np.arange(1, 5, step=1))
ax.set_ylabel("Dielectric Constant",fontsize=15)
ax.set_xlabel("Technology Nodes",fontsize=15)
ax.grid(linestyle='-.', linewidth=0.5)
plt.tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.legend(borderaxespad=0,edgecolor='black')

plt.savefig("Q5.png",bbox_inches='tight',transparent=True,dpi=500)

plt.show()
