# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:06:55 2018

@author: cscuser
"""

import geopandas as gpd
#file path
fp = r"C:\Users\cscuser\Desktop\Europe_borders\Europe_borders.shp"
data = gpd.read_file(fp)

#reproject the data into epsg 3035 prject
data_proj = data.to_crs(epsg=3035)

#reproject2
data_proj2 = data.to_crs(pycrs.parser.from_esri_code(37205).to_proj4))

