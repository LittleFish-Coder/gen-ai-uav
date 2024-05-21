# download training dataset
train_dataset_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EdW17v3WeLFOiFunN-ubMgABHWBd21TjKK9S0SwAFY9Apg?e=pMEbP5&download=1"
train_dataset="34_Competition 1_Training dataset.zip"
# if the dataset is already downloaded, then skip downloading
if [ -f "$train_dataset" ]; then
    echo "$train_dataset already exists. Skipping download."
else
    echo "Downloading $train_dataset..."
    wget -N $train_dataset_url -O "$train_dataset"
fi


# download public testing dataset
public_testing_dataset_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/Efhu6__QLKpBppVWOOR1MQUBqgu_W50eBNaqI8JQnsxoaw?e=qazWJg&download=1"
public_testing_dataset="34_Competition 1_public testing dataset.zip"
# if the dataset is already downloaded, then skip downloading
if [ -f "$public_testing_dataset" ]; then
    echo "$public_testing_dataset already exists. Skipping download."
else
    echo "Downloading $public_testing_dataset..."
    wget -N $public_testing_dataset_url -O "$public_testing_dataset"
fi

# download private testing dataset
private_testing_dataset_url="https://ncku365-my.sharepoint.com/:u:/g/personal/nm6121030_ncku_edu_tw/EVwEjKzvNI1Hi4LhCVqVUB4Bf5En2hNs_MgGJJqkgtAwtw?e=RHsQzz&download=1"
private_testing_dataset="34_Competition 1_Private Test Dataset.zip"
# if the dataset is already downloaded, then skip downloading
if [ -f "$private_testing_dataset" ]; then
    echo "$private_testing_dataset already exists. Skipping download."
else
    echo "Downloading $private_testing_dataset..."
    wget -N $private_testing_dataset_url -O "$private_testing_dataset"
fi

echo "All datasets are downloaded."