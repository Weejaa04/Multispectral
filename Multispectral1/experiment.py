#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 06:35:19 2020
This class is used to do some setting about experiment
@author: research
"""

import pandas as pd
from sklearn.model_selection import  train_test_split


class Experiment():
    
    def __init__(self, filename, **parameters):
        super (Experiment,self).__init__()
        
        self.training_sample=parameters['training_sample']
        self.filename=filename
        self.drive=parameters['folder']
        self.epoch=parameters['epoch']
        self.batch_size=parameters['batch_size']
        
    def set_train_test(self):
        
        data=pd.read_csv(self.drive+self.filename)
        #split the data into labels amd feature
        y=data.Yield
        x=data.drop('Yield', axis=1)
        
        x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2)
        print (x_train.head())
        return x_train, x_test, y_train, y_test


