# make the directory
mkdir -p ./checkpoints/ROAD_pix2pix

# set the model file path
ROAD_MODEL_FILE=./checkpoints/ROAD_pix2pix/latest_net_G.pth
road_pth_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EZ7UIyR9lU5DtSidvsWFMVQBZatxHpbpOluDjeQ1eEQLKQ?e=eSJEvP&download=1"

# download the pretrained weight
echo "Downloading the pretrained weight for the ROAD_pix2pix model..."
wget -N $road_pth_url -O $ROAD_MODEL_FILE

# make the directory
mkdir -p ./checkpoints/RIVER_pix2pix

# set the model file path
RIVER_MODEL_FILE=./checkpoints/RIVER_pix2pix/latest_net_G.pth
river_pth_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EVRE2SjLSJlOpOMNZYQroHgByoXga5slwJwNcG-d-g1jhQ?e=JNu92T&download=1"

# download the pretrained weight
echo "Downloading the pretrained weight for the RIVER_pix2pix model..."
wget -N $river_pth_url -O $RIVER_MODEL_FILE