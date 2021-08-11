# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# A.py
# Created on: 2020-08-21 16:36:39.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: LOS 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension("3D")
env.workspace = "C:/LOS"
arcpy.env.overwriteOutput = True


# Local variables:
GroundOK_wrl = "GroundOK.wrl"
GroundOK_shp = "GroundOK.shp"
GroundOK_tif = "GroundOK.tif"
GroundOK25_tif = "GroundOK25.tif"
CeilingsMax_wrl = "CeilingsMax.wrl"
CeilingsMax_shp = "CeilingsMax.shp"
CeilingsMax_tif = "CeilingsMax.tif"
CeilingsMin_wrl = "CeilingsMin.wrl"
CeilingsMin_shp = "CeilingsMin.shp"
CeilingsMin_tif = "CeilingsMin.tif"
CeilingsOK_tif = "CeilingsOK.tif"
Slope_tif = "Slope.tif"
Height_tif = "Height.tif"
OPosture_tif = "OPosture.tif"
OPosition_tif = "OPosition.tif"
OP_shp = "OP.shp"
Target_shp = "Target.shp"
GUs_shp = "GUs.shp"
TP_shp = "TP.shp"
Buffer_shp = "Buffer.shp"
OPs_shp = "OPs.shp"
LS_shp = "LS.shp"
LSLight_shp = "LSLight.shp"
LSSelect_shp = "LSSelect.shp"
ObserverStatistics_dbf = "ObserverStatistics.dbf"
OPFrequency_tif = "OPFrequency.tif"
OPKernelDensity_tif = "OPKernelDensity.tif"
TargetStatistics_dbf = "TargetStatistics.dbf"
TPFrequency_tif = "TPFrequency.tif"
TPKernelDensity_tif = "TPKernelDensity.tif"
Standing_tif = "Standing.tif"
Stooping_tif = "Stooping.tif"
VisibilityRange_tif = "VisibilityRange.tif"
VisibilityStooping_tif = "VisibilityStooping.tif"
VisibilityStanding_tif = "VisibilityStanding.tif"


# Process: Import 3D Files
arcpy.Import3DFiles_3d(GroundOK_wrl, GroundOK_shp, "ONE_ROOT_ONE_FEATURE", "PROJCS['ETRS_1989_ETRS-TM30',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-3.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0,001;0,001;0,001;IsHighPrecision", "Z_IS_UP", "*", "", "")

# Process: Multipatch to Raster
arcpy.MultipatchToRaster_conversion(GroundOK_shp, GroundOK_tif, "0,05")

# Process: Multipatch to Raster (2)
arcpy.MultipatchToRaster_conversion(GroundOK_shp, GroundOK25_tif, "0,25")

# Process: Import 3D Files (2)
arcpy.Import3DFiles_3d(CeilingsMax_wrl, CeilingsMax_shp, "ONE_ROOT_ONE_FEATURE", "PROJCS['ETRS_1989_ETRS-TM30',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-3.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0,001;0,001;0,001;IsHighPrecision", "Z_IS_UP", "*", "", "")

# Process: Multipatch to Raster (3)
arcpy.MultipatchToRaster_conversion(CeilingsMax_shp, CeilingsMax_tif, "0,05")

# Process: Import 3D Files (3)
arcpy.Import3DFiles_3d(CeilingsMin_wrl, CeilingsMin_shp, "ONE_ROOT_ONE_FEATURE", "PROJCS['ETRS_1989_ETRS-TM30',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-3.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0,001;0,001;0,001;IsHighPrecision", "Z_IS_UP", "*", "", "")

# Process: Multipatch to Raster (4)
arcpy.MultipatchToRaster_conversion(CeilingsMin_shp, CeilingsMin_tif, "0,05")

# Process: Mosaic To New Raster
arcpy.MosaicToNewRaster_management("CeilingsMax.tif;CeilingsMin.tif", "C:\\LOS", \
                                   "CeilingsOK.tif", "PROJCS['ETRS_1989_ETRS-TM30',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-3.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]",\
                                   "32_BIT_FLOAT", "0,05", "1", "MINIMUM","REJECT")

# Process: Slope
arcpy.gp.Slope_sa(GroundOK_tif, Slope_tif, "DEGREE", "1")

# Process: Raster Calculator
Height = (Raster(CeilingsOK_tif) - Raster(GroundOK_tif))
Height.save(Height_tif)

# Process: Raster Calculator (2)
A_tif = SetNull(Height_tif, Height_tif, "VALUE < 0,71")

# Process: Raster Calculator (3)
B_tif = SetNull(Slope_tif, A_tif, "VALUE >= 30")

# Process: Raster Calculator (4)
D_tif = Con(B_tif, "1,66", B_tif, "VALUE >= 1,66")

# Process: Raster Calculator (5)
E_tif = Con(D_tif, "0,71", D_tif, "VALUE < 1,66")
E_tif.save(OPosture_tif)

# Process: Raster Calculator (6)
F_tif = (GroundOK25_tif+E_tif)
F_tif.save(OPosition_tif)

# Process: Raster to Point 
arcpy.RasterToPoint_conversion(F_tif, OP_shp, "VALUE")

# Process: Buffer analysis
arcpy.Buffer_analysis(GUs_shp, Buffer_shp, "2,99 Meters", "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Clip analysis
arcpy.Clip_analysis(OP_shp, Buffer_shp, OPs_shp)

# Process: Construct Sight Lines
arcpy.ConstructSightLines_3d(OPs_shp, TP_shp, LS_shp, "grid_code", "Shape.Z", "<None>", "1", "NOT_OUTPUT_THE_DIRECTION")

# Process: Intervisibility
arcpy.Intervisibility_3d(LS_shp, CeilingsMax_shp, "VISIBLE")

# Process: Add Geometry
arcpy.AddGeometryAttributes_management(LS_shp, "LENGTH_3D", "METERS", "", "PROJCS['ETRS_1989_ETRS-TM30',GEOGCS['GCS_ETRS_1989',DATUM['D_ETRS_1989',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-3.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]")

# Process: Select
arcpy.Select_analysis(LS_shp, LSLight_shp, "\"LENGTH_3D\" <= 2.99")

# Process: Select (2)
arcpy.Select_analysis(LSLight_shp, LSSelect_shp, "\"VISIBLE\" = 1")

# Process: Summary Statistics
arcpy.Statistics_analysis(LSSelect_shp, ObserverStatistics_dbf, "OID_OBSERV COUNT", "OID_OBSERV")

# Process: Join Field
arcpy.JoinField_management(OPs_shp, "FID", ObserverStatistics_dbf, "OID_OBSERV", "COUNT_OID_")

# Process: Add Field
arcpy.AddField_management(OPs_shp, "Frequency", "DOUBLE", 100, 10, 10, "", "NON_NULLABLE", "NON_REQUIRED")

## input file
file = OPs_shp

field_to_max = 'COUNT_OID_' ### field with values
field_to_update = 'Frequency' ### Field to be updated

values = []
# Process: Max
with arcpy.da.SearchCursor(file, field_to_max) as cursor, arcpy.da.UpdateCursor(file, [field_to_max, field_to_update]) as upd_cursor:
    for row in cursor:
        values.append(row[0])
    max_num = max(values) ### get max value
    for row in upd_cursor:
        value = (float(row[0]) / float(max_num)) * 100

        row[1] = float(value) ### calculate value
        upd_cursor.updateRow(row) ### set value

# Process: Point to Raster
arcpy.PointToRaster_conversion(OPs_shp, "Frequency", OPFrequency_tif, "MAXIMUM", "NONE", "0,25")

# Process: Summary Statistics (2)
arcpy.Statistics_analysis(LSSelect_shp, TargetStatistics_dbf, "OID_TARGET COUNT", "OID_TARGET")

# Process: Join Field (2)
arcpy.JoinField_management(TP_shp, "FID", TargetStatistics_dbf, "OID_TARGET", "COUNT_OID_")

# Process: Add Field (2)
arcpy.AddField_management(TP_shp, "Frequency", "DOUBLE", 100, 10, 10, "", "NON_NULLABLE", "NON_REQUIRED")

## input file (2)
file2 = TP_shp

field_to_max2 = 'COUNT_OID_' ### field with values
field_to_update2 = 'Frequency' ### Field to be updated

values2 = []
with arcpy.da.SearchCursor(file2, [field_to_max2]) as cursor, arcpy.da.UpdateCursor(file2, [field_to_max2, field_to_update2]) as upd_cursor:
    for row in cursor:
        values2.append(row[0])
    max_num2 = max(values2) ### 
    for row in upd_cursor:
        value2 = (float(row[0]) / float(max_num2)) * 100

        row[1] = float(value2) ### calculate value
        upd_cursor.updateRow(row) ### set value

# Process: Point to Raster (2)
arcpy.PointToRaster_conversion(TP_shp, "Frequency", TPFrequency_tif, "MAXIMUM", "NONE", "0,25")

# Process: Raster Calculator (7)
G_tif = SetNull(OPosture_tif, 0, "VALUE < 1,66")
G_tif.save(Standing_tif)

# Process: Raster Calculator (8)
H_tif = SetNull(OPosture_tif, 0, "VALUE >= 1,66")
H_tif.save(Stooping_tif)

# Process: Reclassify
outReclass1 = Reclassify(OPFrequency_tif, "Value", RemapRange([[0.01,33.33,1],[33.33,66.66,2],[66.66,100,3]]),"NODATA")
outReclass1.save(VisibilityRange_tif)

# Process: Raster Calculator (9)
I_tif = (G_tif+VisibilityRange_tif)
I_tif.save(VisibilityStanding_tif)

# Process: Raster Calculator (10)
J_tif = (H_tif+VisibilityRange_tif)
J_tif.save(VisibilityStooping_tif)

## input file
file = VisibilityStooping_tif

field_to_take = 'Count' ### field with values
field_to_update = 'Occupancy' ### Field to be updated

# Process: Add Field (4)
arcpy.AddField_management(VisibilityStooping_tif, "Occupancy", "DOUBLE", 100, 10, 10, "", "NON_NULLABLE", "NON_REQUIRED")

values = []
# Process: CalculateMax
with arcpy.da.SearchCursor(file, field_to_take) as cursor, arcpy.da.UpdateCursor(file, [field_to_take, field_to_update]) as upd_cursor:
    for row in cursor:
        values.append(row[0])
    for row in upd_cursor:
        value = (float(row[0]) * 0.0625) / 0.9

        row[1] = float(value) ### calculate value
        upd_cursor.updateRow(row) ### set value