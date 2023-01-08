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
os.chdir('C:/Users/yz60069/TAI/TAI_fresh')
import scipy.io
#mat = scipy.io.loadmat('WaterTableData.mat')

#%% specify the pflotran output structure
nx = 1
ny = 1
nz = 5
nline = nx * ny * nz
ntimepoint = 336


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
elif var_id == 5:
    var_str = 'Total NH4+ [M]'
elif var_id == 6:
    var_str = 'microbes [mol/m^3]'

# Read in data from PFLOTRAN
Full_Data = np.empty( shape = (nline,ntimepoint), dtype = np.float32)
j = 0



for i in range(0,ntimepoint):
    
    file_name = 'TAI_wetlands-00' + str(i) + '.tec'
    if len(file_name)==21:
        file_name = file_name[0:13] + file_name[14:21]
    elif len(file_name)==22:
        file_name = file_name[0:13] + file_name[15:22]
    
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
    
    Full_Data[:,j] = results[var_str]
    j = j + 1





#%%
Coord = np.empty( shape = (nline,3) , dtype = np.float32 )
Coord[:,0] = results['VARIABLES=X [m]']
Coord[:,1] = results['Y [m]']
Coord[:,2] = results['Z [m]']



#%% Plot the depth profiles of the investigated variable for different timepoints
interval = nx * ny
depths = Coord[0:nline:interval,2] - 1  #minus the depth of the soil profile

for i in range(0,ntimepoint):
    conc = Full_Data[0:nline:interval,i] 
    plt.plot(conc, depths)

ax=plt.gca()
ax.set_xlabel(var_str)
ax.set_ylabel('Soil Depth (m)')
plt.rcParams.update({'font.size': 12})

#%% plot the time series of the variable

plt.plot(Full_Data[4,:])   #bigger row number means closer to the soil surface
ax=plt.gca()
ax.set_xlabel('Time (hr)')
ax.set_ylabel(var_str)
plt.rcParams.update({'font.size': 13})

 #%% plot O2 and liquid saturation profile
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(Full_Data_ls[:,4], 'b-')   #larger column number, closer to the soil surface
ax1.spines['left'].set_color('b')
ax1.set_ylabel('Liquid Saturation')

ax2.plot(Full_Data_o2[:,4], 'r-')
ax2.spines['right'].set_color('r')
ax2.set_ylabel('O2(aq) [M]')

#%% import the observation data of water table depth 
os.chdir('C:/MBL/Research/Typha data/water table')
WTMean = []


from csv import reader
file_name = "WTMeanCB.csv"

with open (file_name, 'r') as csv_file:
    csv_data = reader(csv_file)
    header = next(csv_file)
    
    for row in csv_data:
        WTMean.append(row)

WTMean = np.array(WTMean)

#%%  Plot the observed water table with the modeled liquid saturation
fig, ax1 = plt.subplots()

ax1.plot(Full_Data[4,:], 'r-', label = 'Liquid Saturation (PFLOTRAN)')  
ax1.set_ylim(0,1.1)
ax1.set_ylabel('Liquid Saturation', color = 'r')

ax2 = ax1.twinx()
ydata = np.array(WTMean[1515:1850, 1], dtype = float)
ax2.plot(range(0,335), ydata, 'b-', label = 'Water Table')
ax2.plot([0, 335], [0.95, 0.95], 'k-', label = 'Soil Surface')
ax2.spines['right'].set_color('b')
ax2.spines['left'].set_color('r')
ax2.set_ylabel('Water Table(m)', color = 'b')
#ax2.set_ylim(2.95, 3.5)

ax1.set_xlabel('Time (hr)')
plt.rcParams.update({'font.size': 13})
fig.legend(loc = 'lower left', bbox_to_anchor=(0,0.05), bbox_transform=ax.transAxes, fontsize = 10)

#%% Convert the liquid saturation to water table level
WT_mod = []
WaterHeight = []
D = [0.2]*5
Area = 1 * 1
soil_depth = 1
Vol = np.array(D) * Area


for i in range():
    WaterHeight.append(sum(arr * Vol) /Area)
    WT_mod.append(sum(arr * Vol) / Area + (0.95 - soil_depth) )





#%% compare the modeled water level with the observation
plt.plot(range(1,25), np.array(WTMean[200:248:2,1], dtype = np.float32))
plt.plot(WT_mod, 'r.')



#%% Compare modeled O2 and observed O2
#%% import O2 data
os.chdir('C:/MBL/Research/Typha data/Redox')
OxyConc = []


from csv import reader
file_name = "Oxygen_Conc_CB.csv"

with open (file_name, 'r') as csv_file:
    csv_data = reader(csv_file)
    header = next(csv_file)
    
    for row in csv_data:
        OxyConc.append(row)

OxyConc = np.array(OxyConc)

#%% Plot the modeled O2 against observed O2
plt.plot(Full_Data[1,:]*32*1000, 'b--', label = 'Modeled O2')

ydata = np.array(OxyConc[3773:7805:12,24], dtype = float)
plt.plot(ydata, 'b-', label = 'Estimated O2 (redox)')
plt.legend(loc = 0)

ax = plt.gca()
ax.set_xlabel('Time (hr)')
ax.set_ylabel('O2(aq) (mg/L)')
ax.set_ylim(-0.1, 4.2)