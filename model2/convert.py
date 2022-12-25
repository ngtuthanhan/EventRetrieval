import glob 
import numpy as np
import pandas as pd
path_csv = "/mlcv/WorkingSpace/Personals/nhanntt/AIC22/System/Dockerfile_mongo/keyframe_p"
all_path_csv = glob.glob(path_csv + "/*")
all_path_csv.sort()
i = 1
index = np.load("/mlcv/WorkingSpace/Personals/thuongpt/AIC2022/TIUday/index.npy")
for path in all_path_csv:
    k = int(path[-8:-4])
    if k <= 99:
        data = pd.read_csv(path)
        data = np.array(data)
        for j in data:
                index[i][1] = j[1]
                i += 1
        i += 1
for path in all_path_csv:
    k = int(path[-8:-4])
    if 200 > k > 99:
        data = pd.read_csv(path)
        data = np.array(data)
        for j in data:
                index[i][1] = j[1]
                i += 1
        i += 1
with open('index1.npy','wb') as f:
    np.save(f,np.array(index))