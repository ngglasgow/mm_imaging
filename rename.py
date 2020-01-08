import os

cwd = os.getcwd()
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
