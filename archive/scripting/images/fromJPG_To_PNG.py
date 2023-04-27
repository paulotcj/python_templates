import sys
import os
from PIL import Image

jpeg_folder = sys.argv[1]
png_folder = sys.argv[2]
# jpeg_folder = "./converting/fromJPG"
# png_folder = "./converting/toPNG"

print(f"jpeg_foler : {jpeg_folder} ,png_folder: {png_folder} ")

if not os.path.exists(jpeg_folder):
    print(f"The path does not exist: {jpeg_folder}")
    exit()

if not os.path.exists(png_folder):
    print(f"The path does not exist: {png_folder}")
    os.makedirs(png_folder)



for file in os.listdir(jpeg_folder):
    full_file_path = f"{jpeg_folder}/{file}"
    print(f"processing file: {full_file_path}")
    img = Image.open(full_file_path)
    file = file.replace(".jpg","").replace(".JPG","").replace(".jpeg","").replace(".JPEG","")
    
    new_png_file = f"{png_folder}/{file}.png"
    img.save(new_png_file,"png")
