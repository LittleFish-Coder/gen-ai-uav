import os
from PIL import Image


def align_images(source_folder, target_folder="train"):
    train_folder = os.path.join(source_folder, target_folder)
    if not os.path.exists(train_folder):
        os.makedirs(train_folder)

    train_A_files = get_file_paths(os.path.join(source_folder, "trainA"))
    train_B_files = get_file_paths(os.path.join(source_folder, "trainB"))

    print(f"saving aligned images to {train_folder}")
    # Align images
    for i in range(len(train_A_files)):
        filename = os.path.basename(train_A_files[i]).split(".")[0]

        img_A = Image.open(train_A_files[i])
        img_B = Image.open(train_B_files[i])
        assert img_A.size == img_B.size

        aligned_image = Image.new("RGB", (img_A.size[0] * 2, img_A.size[1]))
        aligned_image.paste(img_A, (0, 0))
        aligned_image.paste(img_B, (img_A.size[0], 0))
        # default save as {filename}.jpg
        aligned_image.save(os.path.join(train_folder, f"{filename}.jpg"))
        # else save as {index}.jpg
        # aligned_image.save(os.path.join(train_folder, f"{i:04d}.jpg"))
    print("Done!")


def get_file_paths(folder):
    image_file_paths = []
    for root, dirs, filenames in os.walk(folder):
        filenames = sorted(filenames)
        for filename in filenames:
            input_path = os.path.abspath(root)
            file_path = os.path.join(input_path, filename)
            if filename.endswith(".png") or filename.endswith(".jpg"):
                image_file_paths.append(file_path)

        break  # prevent descending into subfolders
    return image_file_paths


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source_folder",
        default="training_dataset",
        help="help='Which folder to process (it should have subfolders testA, testB, trainA and trainB'",
    )
    args = parser.parse_args()

    source_folder = args.source_folder

    align_images(source_folder)
