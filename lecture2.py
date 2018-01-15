# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:45:24 2018

Lesson 2 CSC

@author: cscuser
"""

import geopandas as gpd
import pandas as pd

# Filepaths

fp = r"C:\Users\cscuser\Desktop\Data\DAMSELFISH_distributions.shp"
outfp = r"C:\Users\cscuser\Desktop\Data\Selection_DAMSELFISH_distributions.shp"
#read the data
data = gpd.read_file(fp)
# Select attributes and certain rows from the data
selection = data.loc[data['YEAR']==2012, ['YEAR', 'geometry', 'BINOMIAL']] 
selection_all = data.loc[data['YEAR']==2012] 
#write data to file
selection.to_file(outfp)

#create a neew column call area of the Polygons
data['area_decimal_degrees'] = data.area
data['centroid'] = data.centroid

#centroids

centroids = data[['centroid', 'BINOMIAL', 'YEAR']]

centroids = centroids.rename(columns={'centroid': 'geometry'})

#converts the pandas to GeaDataFrame
centroids = gpd.GeoDataFrame(centroids, geometry='geometry', crs=data.crs)

# 
