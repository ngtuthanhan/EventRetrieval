import os
import json
import numpy as np
import pandas as pd
jsonfile = []
for batch in os.listdir('/mlcv/Databases/HCM_AIC22'):
    for vid in os.listdir('/mlcv/Databases/HCM_AIC22/' + batch + '/Keyframes'):
        df = pd.read_csv(f'keyframe_p/{vid}.csv', names=['KeyFrame', 'TrueFrame'], header=None)
        TrueFrameList = []
        Video_list = os.listdir('/mlcv/Databases/HCM_AIC22/' + batch + '/Keyframes/' + vid)
        for i, keyframe in enumerate(Video_list):
            if keyframe == '.ipynb_checkpoints':
                continue
            TrueFrame = df[df["KeyFrame"].isin([keyframe])]["TrueFrame"].tolist()[0]
            TrueFrameList.append(TrueFrame)
        
        temp = np.argsort(TrueFrameList)
        PosFrameList = np.arange(len(TrueFrameList))[np.argsort(temp)]


        for i, keyframe in enumerate(Video_list):
            if keyframe == '.ipynb_checkpoints':
                continue
            TrueFrame = df[df["KeyFrame"].isin([keyframe])]["TrueFrame"].tolist()[0]
            TrueFrameList.append(TrueFrame)
            jsonfile.append({
                "Batch": batch,
                "VideoID": vid,
                "KeyFrame": keyframe,
                "TrueFrame": TrueFrame,
                "PositionFrame": int(PosFrameList[i]),
                "IDFrame": vid + '_' + str(TrueFrame)
                })

with open("KeyFrameBatch3V4.json", "w") as outfile:
    json.dump(jsonfile, outfile)
