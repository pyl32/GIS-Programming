# XYTableToPoint.py
# Description: Creates a point feature class from input table
# Resource: https://pro.arcgis.com/en/pro-app/tool-reference/data-management/xy-table-to-point.htm

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "G:/586/project2"

# Set the local variables
in_table = "G:/586/project2/DCA_Cultural_Centers_and_Theaters.csv"
out_feature_class = "DCA_Cultural_Centers_and_Theaters.shp"
x_coords = "X_Long"
y_coords = "Y_Lati"
z_coords = "Z_Elevation_ft"

# Make the XY event layer...Source: https://spatialreference.org/ref/epsg/4326/, ? mean sea level (height) unknown for this dataset
arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords, z_coords,
                                arcpy.SpatialReference(4326))
# Print the total rows
print(arcpy.GetCount_management(out_feature_class))
