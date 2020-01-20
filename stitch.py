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
        server_dir = '/run/user/1000/gvfs/smb-share:server=130.49.237.41,share=urban'

    else:
        server_dir = os.path.join('Z:', os.sep)

    return server_dir


home_path = os.path.expanduser('~')

project_path = os.path.join(home_path, 'urban', 'mm_imaging')
figure_path = os.path.join(project_path, 'figures')
table_path = os.path.join(project_path, 'tables')
data_root = os.path.join(project_path, '191014VJ_C448L')
test_data_path = os.path.join(project_path, '191014VJ_C448L_4_1_gfp_1')

server_dir = server()
server_project = os.path.join(server_dir, 'Glasgow', 'injections')
# below is the JS output from fiji when running a fusion directly, need to put into python imagej format and go from there

#TODO
# need to figure out how to input variables into the text here easily
# at minimum need x, y, and directory
# maybe just make a plus script


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
    xmax = np.array(xs).max() + 1
    ymax = np.array(ys).max() + 1
    return xmax, ymax


def make_fusion(root, dir):
    data_dir = os.path.join(root, dir)
    x, y = get_rows_columns(data_dir)
    save_path = os.path.join(root, 'fused', dir + '.tif')

    IJ.run("Grid/Collection stitching",
        "type=[Filename defined position] \
        order=[Defined by filename         ] \
        grid_size_x=%d \
        grid_size_y=%d \
        tile_overlap=10 \
        first_file_index_x=0 \
        first_file_index_y=0 \
        directory=%s \
        file_names=x{xxx}_y{yyy}.tif \
        output_textfile_name=TileConfiguration.txt \
        fusion_method=[Linear Blending] \
        regression_threshold=0.30 \
        max/avg_displacement_threshold=2.50 \
        absolute_displacement_threshold=3.50 \
        compute_overlap subpixel_accuracy computation_parameters=[Save memory (but be slower)] \
        image_output=[Fuse and display]" % (x, y, data_dir))
    imp = IJ.getImage()
    IJ.saveAs(imp, "Tiff", save_path)
    imp.close()

# choose imagej/fiji to use, uncomment imagej_version to use the cached version
# imagej_version = 'sc.fiji:fiji:2.0.0-pre-8'
local_fiji = os.path.join(home_path, 'Fiji.app')

ij = imagej.init(local_fiji, headless=False)

ij.ui().showUI()

from jnius import autoclass

IJ = autoclass('ij.IJ')

#TODO
# -make into module instead
# -make this a separate script
# -clean up code
# -write new running script to call base functions
# -add code to join overlays
# - look into how to change parameters of stitching
# - look into how to open up temp dirs to make it faster off of the server

# local
with os.scandir(data_root) as it:
    for entry in it:
        if entry.is_dir() and entry.name.startswith('19'):
            make_fusion(data_root, entry.name)

# server
with os.scandir(server_project) as it:
    for entry in it:
        if entry.is_dir() and entry.name.startswith('19'):
            make_fusion(server_project, entry.name)


