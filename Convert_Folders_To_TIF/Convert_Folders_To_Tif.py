# Import System Modules
import arcpy
import os
from arcpy import env
import sys
import time


def main(in_workspace, out_folder):
    # Check extensions and set workspaces
    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
        arcpy.env.overwriteOutput = True
        workspace = in_workspace
        env.workspace = env.scratchWorkspace = workspace
        arcpy.AddMessage("current ws: " + workspace)
    

    # Get a list of all folders in the input workspace
    folder_list = os.listdir(in_workspace)
    arcpy.AddMessage("Found these folders: " + str(folder_list))
  

    for folder in folder_list:
        current_ws = workspace + "\\" + folder
        arcpy.AddMessage("Currently converting: " + current_ws)
        arcpy.env.workspace = current_ws  
        
        # Get a list of the rasters in the directory
        rasters_list = arcpy.ListRasters()
        arcpy.AddMessage("Found these rasters: " + str(rasters_list))

        # Convert them all to rasters
        for raster in rasters_list:
            try:
                arcpy.RasterToOtherFormat_conversion(raster, out_folder, "TIFF")
                # Update the user that conversion was successful
                arcpy.AddMessage(str(raster) + " has been converted successfully ...")
            except:
                # Update the user that conversion was a failure
                arcpy.GetMessages()




################################
if __name__ == '__main__':

    # Get the input parameters
    in_workspace = arcpy.GetParameterAsText(0) # Directory housing all raster bearing directories
    out_folder = arcpy.GetParameterAsText(1) # Directory to place converted rasters

    # Run the program
    arcpy.AddMessage("Converting Rasters in " + in_workspace + str(time.asctime(time.localtime(time.time()))))
    main(in_workspace, out_folder)
