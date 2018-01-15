# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:50:34 2018

@author: cscuser
"""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
from fiona.crs import from_epsg
import pycrs


# Creating a new GeoDataFrame
geo = gpd.GeoDataFrame()

#Create a 'geometry' column
geo['geometry'] = None

#Create a few more columns into the GeoDataFrame
geo = geo.assign(name=None, area=None, centroid=None)

# Coordinates of senate square
coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(shell=coordinates)

# insert the Polygon into GeoDataFrame
geo.loc[0, 'geometry'] = poly

# Define the coordinate reference system
geo.crs = pycrs.parser.from_epsg_code(4326).to_proj4()
