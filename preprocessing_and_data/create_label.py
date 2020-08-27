#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 05:58:56 2020
#this file is used to create label 

@author: research
"""

import pandas as pd
import csv


filename='test.csv'
filedrive=""

data=pd.read_csv(filename)
treatment=data.Treatment
plot=data.Plot
y=data.Yield
patch=data.Patch

size=treatment.size

count=0
new_treatment=[]
new_plot=[]
new_yield=[]
file = open('new_data.csv', 'w', newline ='') 
with file: 
    # identifying header   
    header = ['Treatment', 'Plot', 'Yield'] 
    writer = csv.DictWriter(file, fieldnames = header) 
      
    # writing data row-wise into the csv file 
    writer.writeheader() 


    for i in range(size):
        treatment_i=treatment[i]
        plot_i=plot[i]
        patch_i=patch[i]
        y_i=(y[i]*1000)/patch_i
        
        for j in range(patch_i):
            new_treatment.append(treatment_i)
            name=str(plot_i)+'_'+str(j)
            new_plot.append(name)
            new_yield.append(y_i)   
            
            writer.writerow({'Treatment' : treatment_i,'Plot': name,'Yield': y_i}) 
        
            count=count+1
    
#add new_treatment, new_plot, and new_yield into one dictionary




data = [{'Treatment':t, 'Plot': p, 'Yield': y} for t,p,y in zip(new_treatment,new_plot,new_yield)] 
    


