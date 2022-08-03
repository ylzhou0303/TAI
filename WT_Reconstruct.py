# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:52:04 2022

@author: YZ60069
"""

# This file compiles model output at all different time points

from contextlib import AsyncExitStack
#from socket import AF_X25
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/yz60069/TAI')
import scipy.io
#mat = scipy.io.loadmat('WaterTableData.mat')


#%% Specify the variable you want to plot
var_id = 2


if var_id == 1:
    var_str = 'Liquid Saturation'
elif var_id == 2:
    var_str = 'Total O2(aq) [M]'
elif var_id == 3:
    var_str = 'Total CH4(aq) [M]'
elif var_id == 4:
    var_str = 'Total DOM1 [M]'

#%% Read in data from PFLOTRAN
Full_Data = []
j = 1

for i in range(0,25):
    
    file_name = 'ferm_test__2-00' + str(i) + '.tec'
    if len(file_name)>20:
        file_name = file_name[0:13] + file_name[14:21]
    
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
    
    Full_Data.append(results[var_str])


Full_Data = np.array(Full_Data)

#%% Plot the depth profile of variable investigated

ydata = results['Z [m]'] - 1  #minus the depth of the soil profile
for i in range(0, 2):
    xdata = Full_Data[i,:]
    plt.plot(xdata, ydata)



#%%
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(Full_Data_ls[1:,1], 'b-')   #larger column number, closer to the soil surface
ax1.spines['left'].set_color('b')


ax2.plot(Full_Data_o2[0:,1], 'r-')
ax2.spines['right'].set_color('r')


#%% 
WTMean = []

from csv import reader
file_name = "WTMean.csv"

with open (file_name, 'r') as csv_file:
    csv_data = reader(csv_file)
    header = next(csv_file)
    
    for row in csv_data:
        WTMean.append(row)

WTMean = np.array(WTMean)

#%% compare the modeled water level with the observation
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(Full_Data[1:,1], 'r-o')
ax1.spines['left'].set_color('r')
ax1.set_ylim(0,1.1)
ydata = np.array(WTMean[200:248,1], dtype = float)
ax2.plot(range(0,48), ydata, 'b-o')
ax2.plot(range(0,50), [3.11]*50, 'b-')
ax2.spines['right'].set_color('b')
ax2.set_ylim(2.95, 3.5)



#%% Convert the liquid saturation to water table level
WT_mod = []
D = [0.5, 0.5]
Area = 1 * 1
Vol = np.array(D) * Area


for arr in Full_Data:
    WT_mod.append(sum(arr * Vol) / Area - sum(D) + 3.1149 )





#%%
plt.plot(range(1,49), np.array(WTMean[200:248,1], dtype = np.float32))
plt.plot(WT_mod, 'r.')