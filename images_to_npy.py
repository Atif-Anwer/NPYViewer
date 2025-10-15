#!/usr/bin/env python3

"""Convert all images in a specified folder to NumPy .npy files.
Each image is saved as a separate .npy file with the same base name."""

import argparse
import os

import numpy as np
from PIL import Image


def convert_images_to_npy(folder_path, convert_to_grayscale=False, resize=False):
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
                if convert_to_grayscale and img.mode != 'L':
                    img = img.convert('L')
                if resize:
                    img = img.resize((512, 512))

                img_array = np.array(img)

            base_name = os.path.splitext(img_name)[0]
            npy_path = os.path.join(folder_path, f"{base_name}.npy")

            np.save(npy_path, img_array)
            print(f"Saved: {npy_path}")
        except Exception as e:
            print(f"Failed to process {img_name}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert all images in a folder to .npy files.")
    parser.add_argument(
        "folder_path",
        type=str,
        help="Path to the folder containing images."
    )
    parser.add_argument(
        "--grayscale",
        "-g",
        action="store_true",
        help="Convert images to grayscale before saving as .npy."
    )
    parser.add_argument(
        "--resize",
        "-r",
        action="store_true",
        help="Resize images to 512x512 before saving as .npy."
    )
    args = parser.parse_args()
    convert_images_to_npy(args.folder_path, args.grayscale, args.resize)

if __name__ == "__main__":
    main()
