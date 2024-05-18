# Generative-AI Navigation Information Competition for UAV

AI CUP 2024 Spring

- Team ID: TEAM_5333
- Member:
    - Chen-Yang Yu, NCKU (Leader)
    - Yuan-Chun Jiang, NTU (Consultant)

## Setup
```bash
git clone https://github.com/LittleFish-Coder/gen-ai-uav
```
```bash
cd gen-ai-uav
```
before you run the code, you need to do 2 things:
1. Download the dataset from the [AI cup website](https://tbrain.trendmicro.com.tw/Competitions/Details/34), and put the dataset in the `gen-ai-uav/dataset` folder.
2. clone the pix2pix repository from [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

```bash
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
```

## Prepare The Dataset
run `preprocess_dataset.ipynb`

## Train The Model
run `train_model.ipynb`

## Test The Model
run `test_model.ipynb`

## Submission History
| Time | Filename | Score | Description |
| --- | --- | --- | --- |
| 4/24 |submission.zip|Format Error| Inference with AI cup pretrained-weight|
|5/04 |submission1.zip|178.4705| 1. Inference with pre-trained-weight <br>2. Preprocess: invert the white and black color|
|5/04 |submission2.zip|182.4264| test the model with trained-weight-epoch-40|
|5/04 |submission3.zip|181.2201| test the model with trained-weight-epoch-170|
|5/05 |submission400.zip|172.6293| test the model with trained-weight-epoch-400|
|5/05 |submission200.zip|142.2167| retrain the model with 200 epoch since I misuse the training set|
|5/06 |submission_road_river.zip|134.3143| train 2 domain-specific models for road and river train with 200 epochs|
|5/17 |submission_retrain200.zip|142.1900| 1. use the re-trained weights for all dataset (200 epochs) <br>2. test the image in single_test_mode|
|5/17 |submission_road_river_80epochs.zip|144.3565|train 2 domain-specific models for 80 epochs and test in single mode|
|5/17 |submission_all_load_size_256.zip|141.6813|test the image in single_test_mode and load_size as 256|
|5/18|submission_road_river_400epochs.zip|124.748221|train 2 domain-specific models for 400 epochs and test in single mode|