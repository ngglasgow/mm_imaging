import os

cwd = os.getcwd()

file_list = os.listdir(cwd)

for file in file_list:
    if '.tif' in file:
        file_split = file.split('_')
        xpos = file_split[-2][-3:]
        ypos = file_split[-1][:3]

        new_name = 'x' + xpos + '_y' + ypos + '.tif'

import re

for file in file_list:
    if '.tif' in file:
        xypos = re.search('Pos(\d{3})_(\d{3})', file)
        xpos = xypos.group(1)
        ypos = xypos.group(2)
        new_name = 'x' + xpos + '_y' + ypos + '.tif'
