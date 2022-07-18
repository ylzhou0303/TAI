# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:26:31 2022

@author: YZ60069
"""

fig, ax = plt.subplots()
x = [0, 1, 2]
y1 = x
ax.plot(x, y1, label = 'line1')

y2 = [4, 5, 6]
ax.plot(x, y2, label = 'line2')