
"""
@author: mohammadahangar
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.io import loadmat
from scipy.io import savemat




def image_ext(img, img_path):
    count = 0
    patch_size = 40
    shape = np.shape(img)
    Row = int(round((shape[0]/patch_size)))
    Column = int(round((shape[1]/patch_size)) )
    for row in range(Row):
        for column in range(Column):
            patch = img[row*patch_size:(row+1)*patch_size,\
                              column*patch_size:(column+1)*patch_size,:]
            

            new_path = img_path.replace('/crop/', '/patch/')
            new_path = new_path.replace('.mat', '_%d.mat'%(count))
#            print(new_path)
            #np.save(new_path,patch)
            savemat(new_path, {'temp1':patch})
            
            count +=1
    
    
data_path = glob("./crop/*")
# path =  os.path.join(data_path[0]+ '/*.mat')

for path1 in data_path:
    
    path = path1.replace('/crop/', '/patch/')
    print(path)
    if not os.path.isdir('./patch'):
        os.mkdir('./patch')
    if not os.path.isdir(path):
        os.mkdir(path) 
    
    path2 =  os.path.join(path1+ '/*.mat')
    path2 = glob(path2)
    for img_path in path2:
        img = loadmat(img_path)
        img = img['crop']
        
        image_ext(img, img_path)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# def image_ext(X, location, path_to_save, day = '1'):
#     patch_size = 32
#     start_x = int(location[0,0])
#     stop_x = int(location[0,1])
#     count = 0
#     for i in range (len(location)-1):
#         start_y = int(location[i+1, 0])
#         stop_y = int(location[i+1, 1])
#         crop = X[ start_y:stop_y, start_x:stop_x,:]
#         shape = np.shape(crop)
#         Row = int(round((shape[0]/patch_size)))
#         # print(Row)
#         Column = int(round((shape[1]/patch_size)) )
#         # print(Column)
                         
#         for row in range(Row-1):
#             for column in range(Column-1):
#                 patch = crop[row*patch_size:(row+1)*patch_size,\
#                              column*patch_size:(column+1)*patch_size,:3]

#                 np.save(path_to_save+day+'_patch_%d.npy'%(count),patch)
#                 count +=1
#                 print(np.shape(patch))