#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 07:17:58 2020

@author: research
"""


from scipy import io, misc
import numpy as np
import os 
import spectral
from sklearn import  preprocessing



def open_files (filename):
    _,ext=os.path.splitext(filename)
    ext=ext.lower()
    if ext=='.mat':
        return io.loadmat(filename)
    else:
        return ValueError("Only can read mat file")
    
class MSI ():
    """
    Generic class for multispectral image
    """
    
    def __init__(self,name,**hyperparams):
        super(MSI,self).__init__()
        
        self.name=name
        self.norm_type=hyperparams['norm_type']
        
        #img=self.MSI_open()
        
        
    def MSI_open(self):
        self.img=open_files(self.name)['temp1']
    
        #return img #img must contain only the value matrix     
    
    def Normalize (self, norm_type):
        """
        the normalization process
        """
        
        if norm_type is None:
            norm_type='normal'
            
        if norm_type =='scale':
            #standarization
            data=self.img.reshape(np.prod(self.img.shape[:2]),np.prod(self.img.shape[2:]))
            data=preprocessing.scale(data)
            self.img=data.reshape(self.img.shape[0],self.img.shape[1],self.img.shape[2])
            return self.img
        
        elif norm_type=='normal':
            self.img=(self.img-np.min(self.img))/(np.max(self.img)-np.min(self.img))
            return self.img
        
        else:
        
            return ValueError ("the normalization you choose is not available")
        