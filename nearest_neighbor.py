# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:32:37 2018

@author: Mikko Posio

"""

import geopandas as gpd
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


def nearest(row, geom_union, df1, df2, geom1_col='geometry', geom2_col='geometry', src_column=None):
    """Find the nearest point and return the corresponding value from specified column."""
    # Find the geometry that is closest
    nearest = df2[geom2_col] == nearest_points(row[geom1_col], geom_union)[1]
    # Get the corresponding value from df2 (matching is based on the geometry)
    value = df2[nearest][src_column].get_values()[0]
    return value

#Filepath
    
pks_fp = r'C:\Users\cscuser\Desktop\16.1\PKS_suuralue.kml'
address_fp= r'C:\Users\cscuser\Desktop\16.1\16.1.addresses.shp'

pks =gpd.read_file(pks_fp)
address = gpd.read_file(address_fp)

address = address.dropna(subset=['geometry'])

#Create a unary union of the points (Create multipoint)
unary = address.unary_union

# Calculate the centroids of the polygons

pks['centroid'] = pks.centroid

#Find out the 'id' value of the closest Address point in 'address' 

pks['nearest_id'] = pks.apply(nearest, geom_union=unary, df1=pks, df2=address, geom1_col='centroid', src_column='id')













