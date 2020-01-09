import os

image_dir = '191014VJ_C448L_4_1_gfp_1/'
file_list = os.listdir(image_dir)
os.chdir(image_dir)
for file in file_list:
    if '.tif' in file:
        file_split = file.split('_')
        xpos = file_split[-2][-3:]
        ypos = file_split[-1][:3]

        new_name = 'x' + xpos + '_y' + ypos + '.tif'

        os.rename(file, new_name)

import re

for file in file_list:
    if '.tif' in file:
        xypos = re.search('Pos(\d{3})_(\d{3})', file)
        xpos = xypos.group(1)
        ypos = xypos.group(2)
        new_name = 'x' + xpos + '_y' + ypos + '.tif'

# this script below walks through all subdirectories and will look for only tifs
# still need something to confirm or be a little more careful
# need to test that the script runs in a given dir as opposed to where the script lives


def main():
    path = os.getcwd()
    count = 1

    for root, dirs, files in os.walk(path):
        for file in files:
            if '.tif' in file:
                print(os.path.join(root, file))

