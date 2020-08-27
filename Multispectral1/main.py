#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 06:56:49 2020

@author: Wijayanti Nurul Khotimah
"""

from __future__ import print_function
from __future__ import division 


#for the argument 
import argparse
import numpy as np

import tensorflow as tf 
from tensorflow.python.keras.optimizers import RMSprop, SGD, Adam


#commecting the classes
from MSI import MSI
from experiment import Experiment 
from model import*



hyperparams=	{
  "folder": "../Datasets/Multispectral/", #the directory of dataset
  "model": "BasicWija2",
  "epoch": 50,
  "runs":1,
  "training_sample":0.7,
  "batch_size":128,
  "norm_type":"scale"

}

#some initializations 

filename='new_data.csv'
date1='15_08'
date2='09_09'
date3='10_10'
date4='25_10'


#The process of deep learning 

ITER=hyperparams['runs']

for index_range in range (ITER):
    print ("Iterartion:{}".format(index_range+1))
    
    ex=Experiment(filename, **hyperparams)
    x_train, x_test, y_train, y_test=ex.set_train_test()
    Y_train=y_train.values
    Y_test=y_test.values
    #the type of x_train: pandas.core.frame.DataFrame
    #the type of y_train: pandas.core.series.Series
    
    #read the multispectral image and stack them togother 
    
    # get the size of training and testing 
    
    training_size=x_train.shape[0]
    testing_size=x_test.shape[0]
    
    Xtrain=np.empty((training_size,4,40,40,6))
    Xtest=np.empty((testing_size,4,40,40,6))
    i=0
    
    for index, row in x_train.iterrows():
        Treatment= row['Treatment']
        Plot=row['Plot']
        drivemonth1=hyperparams['folder']+'patch/'+'mat_MSK_'+date1+'_'+Treatment+'_image/'
        file='Plot_ID_'+str(Plot)+'.mat'
        MSI1=MSI(drivemonth1+file,**hyperparams)
        MSI1.MSI_open()
        img1=MSI1.img
        Xtrain[i,0,:,:,:]=img1[:,:,0:6]
        drivemonth2=hyperparams['folder']+'patch/'+'mat_MSK_'+date2+'_'+Treatment+'_image/'
        MSI2=MSI(drivemonth2+file,**hyperparams)
        MSI2.MSI_open()
        img2=MSI2.img
        Xtrain[i,1,:,:,:]=img2[:,:,0:6]    
        drivemonth3=hyperparams['folder']+'patch/'+'mat_MSK_'+date3+'_'+Treatment+'_image/'
        MSI3=MSI(drivemonth3+file,**hyperparams)
        MSI3.MSI_open()
        img3=MSI3.img
        Xtrain[i,2,:,:,:]=img3[:,:,0:6]  
        drivemonth4=hyperparams['folder']+'patch/'+'mat_MSK_'+date4+'_'+Treatment+'_image/'
        MSI4=MSI(drivemonth3+file,**hyperparams)
        MSI4.MSI_open()
        img4=MSI4.img
        Xtrain[i,3,:,:,:]=img4[:,:,0:6]
        i=i+1
    
    #read data for testing 
    i=0
    for index, row in x_test.iterrows():
        Treatment= row['Treatment']
        Plot=row['Plot']
        drivemonth1=hyperparams['folder']+'patch/'+'mat_MSK_'+date1+'_'+Treatment+'_image/'
        file='Plot_ID_'+str(Plot)+'.mat'
        MSI1=MSI(drivemonth1+file,**hyperparams)
        MSI1.MSI_open()
        img1=MSI1.img
        Xtest[i,0,:,:,:]=img1[:,:,0:6]
        drivemonth2=hyperparams['folder']+'patch/'+'mat_MSK_'+date2+'_'+Treatment+'_image/'
        MSI2=MSI(drivemonth2+file,**hyperparams)
        MSI2.MSI_open()
        img2=MSI2.img
        Xtest[i,1,:,:,:]=img2[:,:,0:6]    
        drivemonth3=hyperparams['folder']+'patch/'+'mat_MSK_'+date3+'_'+Treatment+'_image/'
        MSI3=MSI(drivemonth3+file,**hyperparams)
        MSI3.MSI_open()
        img3=MSI3.img
        Xtest[i,2,:,:,:]=img3[:,:,0:6]  
        drivemonth4=hyperparams['folder']+'patch/'+'mat_MSK_'+date4+'_'+Treatment+'_image/'
        MSI4=MSI(drivemonth3+file,**hyperparams)
        MSI4.MSI_open()
        img4=MSI4.img
        Xtest[i,3,:,:,:]=img4[:,:,0:6]
        i=i+1
    
    
    XTrainA=Xtrain[:,0,:,:]
    XTrain_A=XTrainA.reshape(XTrainA.shape[0],XTrainA.shape[1],XTrainA.shape[2],XTrainA.shape[3],1)
    XTrainB=Xtrain[:,1,:,:]
    XTrain_B=XTrainB.reshape(XTrainB.shape[0],XTrainB.shape[1],XTrainB.shape[2],XTrainB.shape[3],1)
    XTrainC=Xtrain[:,2,:,:]
    XTrain_C=XTrainC.reshape(XTrainC.shape[0],XTrainC.shape[1],XTrainC.shape[2],XTrainC.shape[3],1)
    XTrainD=Xtrain[:,3,:,:]
    XTrain_D=XTrainD.reshape(XTrainD.shape[0],XTrainD.shape[1],XTrainD.shape[2],XTrainD.shape[3],1)
    
    XTestA=Xtest[:,0,:,:]
    XTestB=Xtest[:,1,:,:]
    XTestC=Xtest[:,2,:,:]
    XTestD=Xtest[:,3,:,:]
    XTest_A=XTestA.reshape(XTestA.shape[0],XTestA.shape[1],XTestA.shape[2],XTestA.shape[3],1)
    XTest_B=XTestB.reshape(XTestB.shape[0],XTestB.shape[1],XTestB.shape[2],XTestB.shape[3],1)
    XTest_C=XTestC.reshape(XTestA.shape[0],XTestC.shape[1],XTestC.shape[2],XTestC.shape[3],1)
    XTest_D=XTestD.reshape(XTestD.shape[0],XTestD.shape[1],XTestD.shape[2],XTestD.shape[3],1)
    
    
    
       
    if hyperparams['model']=='BasicWija2':
        #test
        model=CNNCNN(6,40) #the number of 6 and 64 is just trial, we can change later
        model1=model.build()
        
        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model1.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])

        
        #do the learning
        model1.fit([XTrain_A,XTrain_B,XTrain_C,XTrain_D], Y_train, epochs=ex.epoch, batch_size=ex.batch_size, shuffle=True)
        y_pred=model1.predict([XTest_A,XTest_B,XTest_C,XTest_D])
        

"""


"""


