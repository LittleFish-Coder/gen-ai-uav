# make the directory
mkdir -p ./checkpoints/ROAD_RIVER_pix2pix

# set the model file path
NET_G_FILE=./checkpoints/ROAD_RIVER_pix2pix/latest_net_G.pth
NET_D_FILE=./checkpoints/ROAD_RIVER_pix2pix/latest_net_D.pth
net_G_url="https://ncku365-my.sharepoint.com/:f:/g/personal/nm6121030_ncku_edu_tw/Ep4F1YoBC2lHhmPUpATWqmYBUDYzw_GXS0dRB-Esr1zAMg?e=ZfLSao&download=1"
net_D_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EaVmCVx45qFAqdH4BtS-FxkBn4R_qzmJRM1m33M7f3AZcw?e=gnnOM4&download=1"

# download the pretrained weight
echo "Downloading the pretrained weight for the ROAD_RIVER_pix2pix model..."
wget -N $net_G_url -O $NET_G_FILE
wget -N $net_D_url -O $NET_D_FILE