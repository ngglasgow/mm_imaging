import re

for file in file_list:
    if '.tif' in file:
        xypos = re.search('Pos(\d{3})_(\d{3})', file)
        xpos = xypos.group(1)
        ypos = xypos.group(2)
        new_name = 'x' + xpos + '_y' + ypos + '.tif'