docker run -it --gpus 'all' --shm-size=64g --name aic_tiuday_nhanntt_system \
-v /mlcv:/mlcv -v $(pwd):/app -p 9000:3000 \
aic_tiuday_nhanntt_system