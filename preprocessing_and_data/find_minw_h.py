#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:37:50 2020

find the smallest widh and high

@author: research
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.io import loadmat


data_path = glob("./mat/*")

min_h=1000

min_w=1000

for path1 in data_path:
    
    
    path2 =  os.path.join(path1+ '/*.mat')
    path2 = glob(path2)
    for img_path in path2:
        img = loadmat(img_path)
        img = img['temp1']
        
        h,w,d=img.shape
        temp=0
        
        if h<w: #if horizontal
            temp=h;
            h=w
            w=temp
        
        
        if h<min_h:
            min_h=h
            name1=img_path
            
        if w<min_w:
            min_w=w
            name_2=img_path
            

print ("min_w ")      
print (min_w)
print ("min_h")
print (min_h)
        
       
        
    
    


