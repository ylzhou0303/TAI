# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:39:47 2022

@author: YZ60069
"""


from contextlib import AsyncExitStack
#from socket import AF_X25
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/yz60069/TAI/TAI_fresh')

#%%
var_id = 2  #choose which variable to plot


if var_id == 1:
    var_str = 'Liquid Saturation'
elif var_id == 2:
    var_str = 'Total O2(aq) [M]'
elif var_id == 3:
    var_str = 'Total CH4(aq) [M]'
elif var_id == 4:
    var_str = 'Total DOM1 [M]'

#%%
for i in range(0,7):
    
    file_name = 'TAI_fresh_YL-00' + str(i) + '.tec'
    with open(file_name,'r') as inputFile:
        read_lines = inputFile.readlines()
       
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    data_list = [] #define a list 
    results = {} #define a dic called results where the numbers are paired with the variable names
    
    for i in range(3, len(read_lines)):
        data_str = read_lines[i].replace(' -','  ').replace('    ','  ').split('  ')
        data_list.append(np.array(data_str, dtype = np.float32))
        
      
    data_list = np.array(data_list)   #convert the list into numpy array
    
    for i in range(0, len(parameter_list)):
        results[parameter_list[i]] = data_list[:,i]
    
    xdata = results[var_str]
    #xdata = results['SOIL1 [mol/m^3]']
    #xdata = results['Total NH4+ [M]']
    ydata = results['Z [m]'] - 20   #minus the depth of the soil profile
    plt.plot(xdata, ydata)


