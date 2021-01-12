import json
import cv2
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import numpy as np


path2images = './of500_images_resized/'

X_name =  np.load('./X_name.npy')
c = 0
for i in tqdm(X_name):
    img = cv2.imread(path2images + i,1)
    if c == 0:
        reshape_image = np.reshape(img,(1,img.shape[0],img.shape[1],img.shape[2]))
        X = reshape_image
    else:
        reshape_image = np.reshape(img,(1,img.shape[0],img.shape[1],img.shape[2]))
        X = np.concatenate((X,reshape_image),axis = 0)
    c+=1

np.save('./X.npy',X)