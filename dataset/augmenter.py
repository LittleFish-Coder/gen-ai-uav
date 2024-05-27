import os
import cv2
import albumentations as A


def augmentation_AB(root="training_dataset", folder_A="trainA", folder_B="trainB"):

    folder_A = os.path.join(root, folder_A)
    folder_B = os.path.join(root, folder_B)

    files_A = sorted([f for f in os.listdir(folder_A) if f.endswith(".jpg") or f.endswith(".png")])
    files_B = sorted([f for f in os.listdir(folder_B) if f.endswith(".jpg") or f.endswith(".png")])

    # Define Augmentation
    transform = A.Compose(
        A.OneOf(
            [A.HorizontalFlip(p=0.5), A.VerticalFlip(p=0.5)],
            p=1.0,
        ),
        additional_targets={"image0": "image"},
    )

    for i, (file_A, file_B) in enumerate(zip(files_A, files_B)):

        # filename for each image
        filename_A, ext_A = file_A.split(".")
        filename_B, ext_B = file_B.split(".")

        img_A = cv2.imread(os.path.join(folder_A, file_A))
        img_B = cv2.imread(os.path.join(folder_B, file_B))

        # same augmentation for both images
        augmented = transform(image=img_A, image0=img_B)
        img_A_augmented = augmented["image"]
        img_B_augmented = augmented["image0"]

        # Save augmented images
        cv2.imwrite(os.path.join(folder_A, f"{filename_A}_aug.{ext_A}"), img_A_augmented)
        cv2.imwrite(os.path.join(folder_B, f"{filename_B}_aug.{ext_B}"), img_B_augmented)


if __name__ == "__main__":
    print(os.getcwd())
    augmentation_AB("training_dataset")
    # augmentation_AB("dataset/testA", "dataset/testB")
