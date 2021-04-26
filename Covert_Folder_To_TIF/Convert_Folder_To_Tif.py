# Import System Modules
import arcpy
import os
from arcpy import env
import sys
import time


def main(in_workspace, out_folder):
    
    # Set the workspace environment setting
    arcpy.env.workspace = in_workspace
    
    # Get a list of the rasters in the directory
    rasters_list = arcpy.ListRasters()

    # Convert them all to rasters
    for raster in rasters_list:
        arcpy.RasterToOtherFormat_conversion(raster, out_folder, "TIFF")
        # Update the user that conversion was successful
        arcpy.AddMessage(str(raster) + " has been converted successfully ...")




################################
if __name__ == '__main__':

    # Get the input parameters
    in_workspace = arcpy.GetParameterAsText(0) # Directory housing all rasters
    out_folder = arcpy.GetParameterAsText(1) # Directory to place converted rasters

    # Run the program
    arcpy.AddMessage("Converting Rasters in " + in_workspace + str(time.asctime(time.localtime(time.time()))))
    main(in_workspace, out_folder)
