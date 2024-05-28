from transformers import Swin2SRForImageSuperResolution
from transformers import Swin2SRImageProcessor
import os
from PIL import Image
import numpy as np
import torch
import shutil

model = Swin2SRForImageSuperResolution.from_pretrained("caidas/swin2SR-classical-sr-x2-64")
processor = Swin2SRImageProcessor()

# road_dir = "./pytorch-CycleGAN-and-pix2pix/results/ROAD_pix2pix/test_latest/submission"
# river_dir = "./pytorch-CycleGAN-and-pix2pix/results/RIVER_pix2pix/test_latest/submission"
dir = "../pytorch-CycleGAN-and-pix2pix/results/ROAD_RIVER_combined/submission"
output_dir = "upscaled_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# all
for img_name in os.listdir(dir):

    if "PUB" in img_name:
        print(f"Skipping {img_name}")
        continue

    img_path = os.path.join(dir, img_name)
    img = Image.open(img_path)
    if img_name in os.listdir(output_dir):
        print(f"Skipping {img_name}")
        continue
    pixel_values = processor(img, return_tensors="pt").pixel_values
    with torch.no_grad():
        outputs = model(pixel_values)
    output = outputs.reconstruction.data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.moveaxis(output, source=0, destination=-1)
    output = (output * 255.0).round().astype(np.uint8)  # float32 to uint8
    # resize to 428x240
    output = np.array(Image.fromarray(output).resize((428, 240), Image.BICUBIC))
    # save the image
    output_img = Image.fromarray(output)
    output_img.save(os.path.join(output_dir, img_name))

    print(f"Upscaling {img_name} done!")
print("Upscaling done!")


# # road
# for img_name in os.listdir(road_dir):
#     img_path = os.path.join(road_dir, img_name)
#     if img_name in os.listdir(output_dir):
#         print(f"Skipping {img_name}")
#         continue
#     img = Image.open(img_path)
#     pixel_values = processor(img, return_tensors="pt").pixel_values
#     with torch.no_grad():
#         outputs = model(pixel_values)
#     output = outputs.reconstruction.data.squeeze().float().cpu().clamp_(0, 1).numpy()
#     output = np.moveaxis(output, source=0, destination=-1)
#     output = (output * 255.0).round().astype(np.uint8)  # float32 to uint8
#     # resize to 420x240
#     output = np.array(Image.fromarray(output).resize((420, 240), Image.BICUBIC))
#     # save the image
#     output_img = Image.fromarray(output)
#     output_img.save(os.path.join(output_dir, img_name))
# print("Upscaling road done!")

# # river
# for img_name in os.listdir(river_dir):
#     img_path = os.path.join(river_dir, img_name)
#     img = Image.open(img_path)
#     if img_name in os.listdir(output_dir):
#         print(f"Skipping {img_name}")
#         continue
#     pixel_values = processor(img, return_tensors="pt").pixel_values
#     with torch.no_grad():
#         outputs = model(pixel_values)
#     output = outputs.reconstruction.data.squeeze().float().cpu().clamp_(0, 1).numpy()
#     output = np.moveaxis(output, source=0, destination=-1)
#     output = (output * 255.0).round().astype(np.uint8)  # float32 to uint8
#     # resize to 420x240
#     output = np.array(Image.fromarray(output).resize((420, 240), Image.BICUBIC))
#     # save the image
#     output_img = Image.fromarray(output)
#     output_img.save(os.path.join(output_dir, img_name))
# print("Upscaling river done!")

# zip the output

shutil.make_archive(output_dir, "zip", output_dir)
