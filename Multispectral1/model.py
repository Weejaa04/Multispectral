#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 05:00:29 2020

@author: research
"""


#create the class model

from __future__ import absolute_import
from __future__ import print_function

#import numpy as np

import keras
from tensorflow.python.keras.models import Sequential
from keras.models import Model
from keras.layers import Input, Reshape,Dense, Conv2D, Flatten, MaxPooling2D,Concatenate, LSTM, BatchNormalization, Activation, AveragePooling2D, Add, Conv3D, MaxPooling3D, Conv1D, MaxPooling1D,AveragePooling1D, Dropout, AveragePooling3D
from keras.initializers import glorot_uniform
from keras.regularizers import l2
import tensorflow as tf

import os
import datetime



    

class CNNCNN():
    """
    this is the first model, simple model to predict the yield prediction
    """
    
    
    def __init__(self, nband, npatch):
        super(CNNCNN, self).__init__()
        self.band=nband
        self.patch=npatch
        self.init="he_normal"
        self.regularizer=l2(0.0001)
        self.filter=24
        
    
    def identity_block(self,X,stage,block):

        """
        This is the identity block
        """
        conv_name_base='res'+str(stage)+block+'_branch'
        bn_name_base='bn'+str(stage)+block+'_branch'
        
        #retrieve the filters
        #F1,F2,F3=filters
        
        X_shortcut=X
        
        #first component of main path
        X=Conv3D(self.filter, (3,3,1),kernel_initializer=self.init,kernel_regularizer=self.regularizer,padding='same')(X)
        X=BatchNormalization(axis=3)(X)
        X=Activation('relu')(X)
        
        #second component of main path
        X=Conv3D(self.filter, (3,3,1),kernel_initializer=self.init,kernel_regularizer=self.regularizer,padding='same')(X)

        
        #final step, add the shortcut
        X=Add()([X,X_shortcut])
        X=Activation('relu')(X)
        
        
        return X
    
    def ExtractFeatures(self,X):

        X= Conv3D (self.filter, kernel_size=(3,3,1),kernel_initializer=self.init,kernel_regularizer=self.regularizer,padding='same')(X)
         
        #stage 2
        X=self.identity_block(X,stage=2,block='a')
        
        #stage 3


        for i in range (2):#change from 2 to 20
            #stage 4

            #stage 5
            X=self.identity_block(X,stage=5,block='b'+str(i))
        
            #stage 6
        

        X=BatchNormalization(axis=3)(X)
        X=Activation('relu')(X)

        
        X=AveragePooling3D(pool_size=(5,5,2))(X)
        
        #output layer
        
        X = Dropout(0.5)(X)
        X=Flatten()(X)

        return X
        
        
        return X
        
    def build(self):
        inputA=Input(shape=(self.patch,self.patch,self.band,1))
        SSaA=self.ExtractFeatures(inputA)
        inputB=Input(shape=(self.patch,self.patch,self.band,1))
        SSaB=self.ExtractFeatures(inputB)
        inputC=Input(shape=(self.patch,self.patch,self.band,1))
        SSaC=self.ExtractFeatures(inputC)
        inputD=Input(shape=(self.patch,self.patch,self.band,1))
        SSaD=self.ExtractFeatures(inputD)


        Z=Concatenate()([SSaA, SSaB, SSaC, SSaD])

        
        
        X = Dense(64,activation='relu')(Z)
        X = Dropout(0.5)(X)
        output = Dense(1)(X)

        
        model=Model(inputs=[inputA, inputB, inputC, inputD], outputs=output)
        
        print (model.summary())
        return model