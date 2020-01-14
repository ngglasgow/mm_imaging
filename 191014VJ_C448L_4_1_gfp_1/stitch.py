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
imp2 = imp.duplicate();
imp.close();