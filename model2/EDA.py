import pandas as pd 
import numpy as np 
# import matplotlib.pyplot as plt 
# import seaborn as sns 
# from moviepy.editor import VideoFileClip
# from os import listdir
# from os.path import isfile,join
# import json
# import glob
# from utils.TIUday import Indexing
# indexing = Indexing("/mlcv/Databases/HCM_AIC22/")
# features,index = indexing.get_all_features
# with open("index.npy","wb") as f:
#     np.save(f,index)
# with open('features.npy','wb') as f:
#     np.save(f,features)
# features = np.load('features.npy')
index = np.load('index.npy')
print(index)
# print(features.shape)