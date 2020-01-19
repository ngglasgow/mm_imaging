import imagej
import numpy as np
import os
import re


def server():
    '''function to define path to server base directory'''

    machine = os.uname()[0]
    if machine == 'Darwin':
        server_dir = '/Volumes/Urban'

    elif machine == 'Linux':
        server_dir = '/run/user/1000/gvfs/smb-share:server=sds1.neurobio.pitt.edu,share=urban'

    else:
        server_dir = os.path.join('Z:', os.sep)

    return server_dir


home_path = os.path.expanduser('~')

project_path = os.path.join(home_path, 'urban', 'mm_imaging')
figure_path = os.path.join(project_path, 'figures')
table_path = os.path.join(project_path, 'tables')
data_path = os.path.join(project_path, '191014VJ_C448L')
test_data_path = os.path.join(project_path, '191014VJ_C448L_4_1_gfp_1')

# choose imagej/fiji to use, uncomment imagej_version to use the cached version
# imagej_version = 'sc.fiji:fiji:2.0.0-pre-8'
local_fiji = os.path.join(home_path, 'Fiji.app')

ij = imagej.init(local_fiji, headless=False)

ij.ui().showUI()

from jnius import autoclass
IJ = autoclass('ij.IJ')
# below is the JS output from fiji when running a fusion directly, need to put into python imagej format and go from there

#TODO
# need to figure out how to input variables into the text here easily
# at minimum need x, y, and directory
# maybe just make a plus script
IJ.run("Grid/Collection stitching",
       "type=[Filename defined position] \
       order=[Defined by filename         ] \
       grid_size_x={} \
       grid_size_y={} \
       tile_overlap=20 \
       first_file_index_x=0 \
       first_file_index_y=0 \
       directory=/home/ngg1/urban/191014VJ_C448L/191014VJ_C448L_4_1_gfp_1 \
       file_names=x{xxx}_y{yyy}.tif \
       output_textfile_name=TileConfiguration.txt \
       fusion_method=[Linear Blending] \
       regression_threshold=0.30 \
       max/avg_displacement_threshold=2.50 \
       absolute_displacement_threshold=3.50 \
       compute_overlap computation_parameters=[Save memory (but be slower)] \
       image_output=[Fuse and display]".format(x, y))
imp = IJ.getImage()
imp2 = imp.duplicate()
imp.close()

    for root, dirs, files in os.walk(path):
        for file in files:
            if '.tif' in file:
                if 'Pos' in file:
                    name_split = file.split('_')
                    xpos = name_split[-2][-3:]
                    ypos = name_split[-1][:3]

                    new_name = 'x' + xpos + '_y' + ypos + '.tif'

                    src = os.path.join(root, file)
                    dst = os.path.join(root, new_name)

                    os.rename(src, dst)

def get_rows_columns(data_dir):
    xs = []
    ys = []
    file_list = os.listdir(data_dir)
    file_list.sort()
    for file in file_list:
        if '.tif' in file:
            xypos = re.search('x(\d{3})_y(\d{3})', file)
            xpos = int(xypos.group(1))
            ypos = int(xypos.group(2))
            xs.append(xpos)
            ys.append(ypos)
    xmax = np.array(xs).max()
    ymax = np.array(ys).max()
    return xmax, ymax


x, y = get_rows_columns(test_data_path)

