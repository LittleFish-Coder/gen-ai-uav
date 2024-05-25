# make the directory
mkdir -p ./checkpoints/ROAD_pix2pix

# set the model file path
ROAD_NET_G_FILE=./checkpoints/ROAD_pix2pix/latest_net_G.pth
ROAD_NET_D_FILE=./checkpoints/ROAD_pix2pix/latest_net_D.pth
road_net_G_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EZ7UIyR9lU5DtSidvsWFMVQBZatxHpbpOluDjeQ1eEQLKQ?e=Wz9hE7&download=1"
road_net_D_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/ERXXo4WtOZpNkPCg7jCx94gBNpgYTR1p_JeisEh0nwfB5A?e=ACXVuV&download=1"

# download the pretrained weight
echo "Downloading the pretrained weight for the ROAD_pix2pix model..."
wget -N $road_net_G_url -O $ROAD_NET_G_FILE
wget -N $road_net_D_url -O $ROAD_NET_D_FILE

# make the directory
mkdir -p ./checkpoints/RIVER_pix2pix

# set the model file path
RIVER_NET_G_FILE=./checkpoints/RIVER_pix2pix/latest_net_G.pth
RIVER_NET_D_FILE=./checkpoints/RIVER_pix2pix/latest_net_D.pth
river_net_G_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EVRE2SjLSJlOpOMNZYQroHgByoXga5slwJwNcG-d-g1jhQ?e=kkRtEy&download=1"
river_net_D_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EfQE1HbtrihLoiKePSt80pABxsODjk57sYe0qZmjC3Sjjg?e=Pjg1Sb&download=1"

# download the pretrained weight
echo "Downloading the pretrained weight for the RIVER_pix2pix model..."
wget -N $river_net_G_url -O $RIVER_NET_G_FILE
wget -N $river_net_D_url -O $RIVER_NET_D_FILE