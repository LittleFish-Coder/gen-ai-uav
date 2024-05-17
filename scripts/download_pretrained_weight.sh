# make the directory
mkdir -p ./checkpoints/ROAD_RIVER_pix2pix

# set the model file path
MODEL_FILE=./checkpoints/ROAD_RIVER_pix2pix/latest_net_G.pth
pth_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EStoJ1cEWjtBsJqOH1v3JW8BxwEzca7_vPpWEkHfsP19Yw?e=u0ggoJ&download=1"

# download the pretrained weight
wget -N $pth_url -O $MODEL_FILE