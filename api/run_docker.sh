docker run -it --gpus 'all' --shm-size=64g --name aic_tiuday_nhanntt_api \
-v /mlcv:/mlcv -v /mlcv/WorkingSpace/Personals/nhanntt/AIC22/System/api:/api -p 15400:15400 aic_tiuday_nhanntt_api