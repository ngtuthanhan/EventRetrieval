import pandas as pd 
import numpy as np 
import os
from os import listdir
from os.path import isfile,join
import json
import glob
import scann
import torch
from transformers import CLIPModel, CLIPProcessor
from tqdm import tqdm
class Searcher:
    
    def __init__(self, index, features, num_neighbors = 200, distance_measure = 'dot_product'):
        self.index = index
        self.searcher = scann.scann_ops_pybind.builder(
                                features,
                                num_neighbors,
                                distance_measure).score_brute_force(1).build()
        
    def __call__(self,text_embedding):
        neighbors,distances = self.searcher.search(text_embedding, final_num_neighbors = 200)
        # print(self.index[neighbors])
        return self.index[neighbors]

        
class CLIPFeatureExtractor:
    def __init__(self):
        model_name = "openai/clip-vit-base-patch16"
        self.model = CLIPModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)

    def __call__(self, text):
        inputs = self.processor(text=text, return_tensors="pt")
        inputs = inputs.to(self.device)
        text_features = self.model.get_text_features(**inputs)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        text_features = text_features.tolist()
        return text_features

class Indexing:
    
    def __init__(self,root_data):
        self.root_data = root_data
        self.all_batch_data = glob.glob(root_data + '*')
    @property
    def all_keyframes_path(self):
        all_folder_keyframes = np.array([])
        for batch in self.all_batch_data:
            all_folder_batch_keyframes = glob.glob(join(self.root_data,batch,"Keyframes",'*'))
            all_folder_keyframes = np.concatenate((all_folder_keyframes,np.array(all_folder_batch_keyframes)),axis = 0)
        all_folder_keyframes.sort()
        return all_folder_keyframes 
    @property
    def get_all_features(self):
        features = np.empty([0,512],dtype = float)
        index = []
        for folder_keyframes in tqdm(self.all_keyframes_path):
            # Add features vector
            # print(folder_keyframes.replace("Keyframes","CLIP_features"))
            feature_video = np.load(folder_keyframes.replace("Keyframes","CLIP_features") + ".npy")
            features = np.concatenate((features,feature_video),axis = 0)
            # Add path key_frames
            # path_keyframes = glob.glob(folder_keyframes + '/*.jpg')
            # path_keyframes.sort()
            # for path in path_keyframes:
            #     temp = path.split("/")
            #     video_name , ID = temp[-2] + '.mp4',temp[-1].replace('.jpg','')
            #     index.append(list((video_name,ID)))
        return features,np.array(index)
    
        