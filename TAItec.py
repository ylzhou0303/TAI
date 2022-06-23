#with open("./COMPASS_PNNL/Compass_CRC_TR_302_WaterLevel600B.dat", 'r') as inputFile:
from contextlib import AsyncExitStack
#from socket import AF_X25
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

os.chdir('C:/Users/yz60069/TAI')

for k in range(1,6):
    file_name = "ferm-00" + str(k) + ".tec"
    with open(file_name,'r') as inputFile:
        read_lines = inputFile.readlines()
        read_lines = read_lines.replace(' -','  ')
        parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
        parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
        result_list = [] #define a list 
        dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
        for i in range(0,len(parameter_list)): #loop for reading in data line by line
            dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
            result_list.append(dic) #append value list from each line in the data file
        for i in range(3, len(read_lines)): #start from the 4th line
            data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
            for j in range(0,len(result_list)): #loop for reading in data at each line
                for key,value in result_list[j].items(): #key is the variable name, value is the data
                    value.append(data_list[j])            
        var_y = []
        var_x = []
        
        for i in range(0,len(result_list)):
           for key,value in result_list[i].items():
             if "Z [m]" in key: #read in depth to array
                var_y = 10 - (np.array(value, dtype=np.float32))
                print(var_y)
             if "Liquid Saturation" in key:
                 var_x = np.array (value, dtype=np.float32)
                 print(var_x)
    

    plt.plot(var_x, var_y)

ax = plt.gca()
ax.set_xlim(0.6, 1)
ax.set_ylim(8, 1)
ax.set_xlabel('Water Saturation')
ax.set_ylabel('Depth (m)')
"""
    plt.figure(1)
    plt.subplot(111)
#plt.xscale('log')
ax=plt.gca()
#ax.set_ylim(30,-10)
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0.0001, 0.0005)
ax.set_xlabel('0')
#plt.xscale('log')
#ax.ticker.LogLocator(base=10.0, subs=(1.0,), numdecs=4, numticks=None)

plt.subplot(192)
with open("TAI_GENX-001.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "TITLE" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('6')
ax.set_yticklabels([])

plt.subplot(193)
with open("TAI_GENX-002.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
plt.xscale('log')
#plt.ticklabel_format(style='plain')
ax.set_ylim(1,0)
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('12')
ax.set_yticklabels([])

plt.subplot(194)
with open("TAI_GENX-003.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('18')
ax.set_yticklabels([])

plt.subplot(195)
with open("TAI_GENX-004.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('24')
ax.set_yticklabels([])

plt.subplot(196)
with open("TAI_GENX-005.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('30')
ax.set_yticklabels([])

plt.subplot(197)
with open("TAI_GENX-006.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('36')
ax.set_yticklabels([])


plt.subplot(198)
with open("TAI_GENX-007.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
#ax.set_xlim(0, 0.0005)
ax.set_xlabel('42')
ax.set_yticklabels([])

plt.subplot(199)
with open("TAI_GENX-008.tec",'r') as inputFile:
    read_lines = inputFile.readlines()
    parameter_str = read_lines[1] #read in the 2nd line, getting variable names as strings
    parameter_list = parameter_str.replace('"','').replace('\n','').split(',')
    result_list = [] #define a list 
    dic = {} #define a dic conrresponding to result_list, each dic will have a list in result_list
    for i in range(0,len(parameter_list)): #loop for reading in data line by line
        dic = {parameter_list[i]:[]} #define a default format for each dic as variable_name:value_list
        result_list.append(dic) #append value list from each line in the data file
    for i in range(3, len(read_lines)): #start from the 4th line
        data_list = read_lines[i].split('  ') #begin reading data, split with two splaces '  '
        for j in range(0,len(result_list)): #loop for reading in data at each line
            for key,value in result_list[j].items(): #key is the variable name, value is the data
                value.append(data_list[j])            
    var_value1 = []
    var_value2 = []
    var_value3 = []
    for i in range(0,len(result_list)):
       for key,value in result_list[i].items():
         if "Total Tracer7" in key: #search for variable name and read in variable to array
            var_value1 = np.array(value, dtype=np.float32)
            print(var_value1)
         elif "Z [m]" in key: #read in depth to array
            var_value2 = 42.09014 - (np.array(value, dtype=np.float32))
            print(var_value2)
         elif "Total DOM1" in key:
             var_value3 = np.array (value, dtype=np.float32)
             print(var_value3)
plt.plot(var_value1, var_value2)
ax=plt.gca()
ax.set_ylim(1,0)
plt.xscale('log')
#ax.set_xlim(0, 1.2*(10**-4))
##ax.set_xlim(0, 0.0005)
ax.set_xlabel('48')
ax.set_yticklabels([])


plt.show()    
"""