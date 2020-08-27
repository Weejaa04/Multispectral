#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:02:48 2020

This finction is to crop the image from center based on the shape

@author: research
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.io import loadmat
from scipy.io import savemat


data_path = glob("./mat/*")

min_h=90

min_w=62

for path1 in data_path:
    path = path1.replace('/mat/', '/crop/')
    print(path)
    if not os.path.isdir('./crop'):
        os.mkdir('./crop')
    if not os.path.isdir(path):
        os.mkdir(path)     
    
    path2 =  os.path.join(path1+ '/*.mat')
    path2 = glob(path2)
    for img_path in path2:
        img = loadmat(img_path)
        img = img['temp1']
        
        h,w,d=img.shape
        temp=0
        center_x=int(w/2)
        center_y=int(h/2)
        
        if h<w: #if horizontal
            corn_x=center_x-min_h
            corn_y=center_y-min_w
            #crop the image
            crop = img[corn_y:corn_y+(min_w*2),corn_x:corn_x+(min_h*2),:]
            
        else:
            corn_x=center_x-min_w
            corn_y=center_y-min_h
            crop = img[corn_y:corn_y+(min_h*2),corn_x:corn_x+(min_w*2),:]
            
        new_path = img_path.replace('/mat/', '/crop/')
        savemat(new_path, {'crop':crop})
        
            

