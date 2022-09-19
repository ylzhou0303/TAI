# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:22:33 2022

@author: YZ60069
"""

import matplotlib
import matplotlib.pyplot as plt




plt.plot(Full_Data_tide[4,:], 'b-', label = 'tide only')   #larger column number, closer to the soil surface
plt.plot(Full_Data_O2exchange[4,:], 'r.', label = 'tide +O2 exchange')
#plt.plot(Full_Data_biggerflow[4,:],'k.', label = 'bigger O2 flow')
plt.xlabel('Time (hr)')
plt.ylabel('Total O2(aq)')
plt.legend(loc = 'upper center')


#%%
plt.plot(Full_Data_1h[4,:], 'b-', label = 'data interval 1h')
plt.plot(range(0, 337, 12), Full_Data_12h[4,:], 'ro', label = 'data interval 12h')
plt.xlabel('Time (hr)')
plt.ylabel('Liquid Sat')
plt.legend(loc = 'lower center')


#%%
import matplotlib
import matplotlib.pyplot as plt

#plt.plot(data1[0,:], 'k-', label = 'tide only')
plt.plot(data2[0,:], 'b-', label = '+ O2 exchange')
plt.plot(data3[0,:], 'r-', label = '+ plant O2 input')
plt.plot(data0[0,:], 'g-', label = 'nothing')
plt.xlabel('Time (hr)')
plt.ylabel('O2(aq) (mol/L)')
plt.legend(loc = 0)


ax = plt.gca()
#ax.set_ylim(-0.00001, 0.00032)