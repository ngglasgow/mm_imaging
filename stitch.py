import imagej
import numpy as np
from skimage import io
import os

# set paths
machine = os.uname()[0]
if machine == 'Darwin':
    home_dir = '/Volumes/Urban'

elif machine == 'Linux':
    home_dir = '/run/user/1000/gvfs/smb-share:server=sds1.neurobio.pitt.edu,share=urban'

else:
    home_dir = os.path.join('Z:', os.sep)

project_dir = os.path.join(home_dir, 'Glasgow', 'ng_testing')
figure_dir = os.path.join(project_dir, 'figures')
table_dir = os.path.join(project_dir, 'tables')
data_dir = os.path.join(project_dir, '190821')
filedir_list = os.listdir(data_dir)

imagej_version = 'sc.fiji:fiji:2.0.0-pre-8'

ij = imagej.init(ij_dir_or_version_or_endpoint='/home/ngg1/Fiji.app', headless=False)

ij.ui().showUI()

from jnius import autoclass
IJ = autoclass('ij.IJ')
# below is the JS output from fiji when running a fusion directly, need to put into python imagej format and go from there

IJ.run("Grid/Collection stitching",
       "type=[Filename defined position] \
       order=[Defined by filename         ] \
       grid_size_x=2 \
       grid_size_y=6 \
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
       image_output=[Fuse and display]");
imp = IJ.getImage()
imp2 = imp.duplicate()
imp.close()