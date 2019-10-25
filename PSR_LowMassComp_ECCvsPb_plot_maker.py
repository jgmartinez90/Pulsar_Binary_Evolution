#!/user/bin/python

import os.path
import glob

import subprocess
from matplotlib import pyplot as plt
import numpy as np
from math import pow, sqrt, log10
#from math import floor, pow, log10, exp, sqrt
import datetime as dt

from mpl_toolkits.mplot3d import Axes3D
from subprocess import Popen, PIPE, STDOUT, call

from collections import Counter
import matplotlib.cm as cm
from scipy import signal
from scipy import misc

from pylab import *


def Phinney_relation(Eccen,Pb):
#	sqrt(Eccen^2) = 1.5e-4 * (Pb/100)
    Phinney_relation = (1.5e-4 * np.array(Pb)/100.)
    return Phinney_relation
    
Eccen = []
Eccen_error = []
Pb = []
Pb_error =[]
HighEccen=[]
HighEccen_error =[]
Pb_highEccen=[]
Pb_highEccen_error = []

NEW_Eccen = []
NEW_Eccen_error = []
NEW_Pb = []
NEW_Pb_error = []

f = open('PSR_Period_Pb_ECC_MinMassWithErrors_finalList.txt', 'r')
for line in f:
	if line.startswith("#"):
		print "TOP LINE"
	elif line.split()[9] == "*":
		print "\n\n No Eccentricity \n\n"
	elif float(line.split()[12]) > 0.4:
		print "Mass is greater than 0.4 solar masses."
	else:
		if float(line.split()[9]) > 0.01 :
			print "High Eccentricity"
			print line.split()[9]
			HighEccen.append(float(line.split()[9]))
			HighEccen_error.append(float(line.split()[10]))
			print "Orbital Period"
			print line.split()[6]
			Pb_highEccen.append(float(line.split()[6]))
			Pb_highEccen_error.append(float(line.split()[7]))
		else:
			print "Low Eccentricity"
			print line.split()[9]
			Eccen.append(float(line.split()[9]))
			Eccen_error.append(float(line.split()[10]))
			print "Orbital Period"
			print line.split()[6]
			Pb.append(float(line.split()[6]))
			Pb_error.append(float(line.split()[7]))


f = open('NEW_PSR.txt', 'r')
for line in f:
	print "NEW Systems \n\n"
	print "Eccentricity"
	print line.split()[9]
	NEW_Eccen.append(float(line.split()[9]))
	NEW_Eccen_error.append(float(line.split()[10]))
	print "Orbital Period"
	print line.split()[6]
	NEW_Pb.append(float(line.split()[6]))
	NEW_Pb_error.append(float(line.split()[7]))


print "High Eccen"
print HighEccen
print "PB of High Eccen"
print Pb_highEccen
#print Eccen

plt.figure(figsize=(15, 8))


ax = plt.figure(1)
ax = plt.subplot(111)



plt.scatter(Pb, Eccen,  marker='o', facecolor='k', edgecolors='k', s=50, label='Circular Binaries')
plt.scatter(Pb_highEccen, HighEccen, marker='*', facecolor='b', edgecolor='b', s=50, label='Eccentric Binaries')
plt.scatter(NEW_Pb, NEW_Eccen, marker='^', facecolor='r', edgecolor='r', s=50, label='New Binaries')
plt.plot(np.linspace(1, 150, 10), Phinney_relation(np.linspace(0.00001, 0.1, 10),np.linspace(1, 150,10)), 'k--', linewidth =0.5, label='Phinney 1992')

#plt.errorbar(Pb, Eccen, yerr=Pb_error, xerr=Eccen_error, fmt='o', label='Circular Binaries')
#plt.errorbar(Pb_highEccen, HighEccen, yerr=Pb_highEccen_error, xerr=HighEccen_error, fmt='*', label='Eccentric Binaries')
#plt.errorbar(NEW_Pb, NEW_Eccen, yerr=NEW_Pb_error, xerr=NEW_Eccen_error, fmt='o', label='New Binaries')

plt.xlim(1, 130) #130
plt.ylim(pow(10,-7), 1.0)

ax.set_yscale('log')
ax.set_xscale('log')
plt.yticks([pow(10,-7), pow(10,-6), pow(10,-5), pow(10,-4), pow(10,-3), 0.01, 0.1], fontsize = 10)
#plt.xticks(['1','10', '100'], fontsize = 10 )
ax.set_xticks([1,10,100])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax.tick_params(axis='both', labelsize=15, pad=6)
ax.spines['top'].set_linewidth(1.6)
ax.spines['bottom'].set_linewidth(1.6)
ax.spines['left'].set_linewidth(1.6)
ax.spines['right'].set_linewidth(1.6)
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10

handles, labels = ax.get_legend_handles_labels()

legend = ax.legend( loc =2, ncol=1, prop={'size': 17}, fancybox=False, shadow=False, borderpad=1, scatterpoints = 1)

legend.legendHandles[0]._sizes = [50]


plt.xlabel(r'Orbital Period (days)', fontsize=20)
plt.ylabel(r"Eccentricity" , fontsize=20)
plt.tight_layout()
plt.savefig('/homes/joey/Scripts/PSR_LowMassCompanion_ECCvsPb_plots/Eccen_vs_OrbitalPeriod.pdf', dpi=100)
plt.show()

