#!/usr/bin/env python3

"""Convert all images in a specified folder to NumPy .npy files.
Each image is saved as a separate .npy file with the same base name."""

import os
import sys

import numpy as np
from PIL import Image


def convert_images_to_npy(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

    if not image_files:
        print("No image files found in the provided folder.")
        return

    for img_name in image_files:
        img_path = os.path.join(folder_path, img_name)
        try:
            with Image.open(img_path) as img:
                img_array = np.array(img)

            base_name = os.path.splitext(img_name)[0]
            npy_path = os.path.join(folder_path, f"{base_name}.npy")

            np.save(npy_path, img_array)
            print(f"Saved: {npy_path}")
        except Exception as e:
            print(f"Failed to process {img_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_images_to_npy.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        convert_images_to_npy(folder_path)
