# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:03:11 2026

@author: ASUS
"""
# REPLACE ALL BOARDER ELEMENTS WITH ZERO
import numpy as np
l=[[10,20,30,40,50,60],
   [70,80,90,100,110,120],
   [130,140,150,160,170,180],
   [190,200,210,220,230,240]]
a=np.array(l)
a[0]=0      #first row
a[:,0]=0    #first column
a[:,-1]=0   #last column
a[-1]=0     #last row




# DISPLAY THE INDEX OF THE HIGHEST ELEMENT IN AN ARRAY
import numpy as np
arr = np.array([
    [3,5,2],
    [9,1,4],
    [7,8,6]
])
print(np.argmax(arr,axis=1))




