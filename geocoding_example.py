# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:01:25 2018
Geocoding example
@author: Mikko Posio
"""

import pandas as pd
import geopandas as gpd
from geopandas.tools import geocode
import geopy
from geopy.geocoders import Nominatim
from shapely.geometry import Point
import pycrs

# filepath to addresses

fp = r"C:\Users\cscuser\Desktop\16.1\addresses.txt"
data = pd.read_csv(fp, sep=';', encoding='utf8') #latin1 letter (character) encoding (utf8=scandinavian characters)

# 

# Geocode the addresses 
geo = geocode(data['addr'], provider='nominatim')

# --------------------------------------------------
# Add more control to geocoding
#---------------------------------------------------
geolocator = Nominatim()

# iterate over the rows

# Create new columns for Point and geocoded address
data = data.assign(geometry=None, address=None)

#iterate over the rows

for idx, row in data.iterrows():
   # print(idx,row)
    location = geolocator.geocode(row['addr'])
    # if location was found, then create a Poin out of it
    if location:
        point = Point(location.longitude, location.latitude)
        address = location.address
        #add the point and address to the DataFrame
        data.loc[idx, 'geometry'] = point 
        data.loc[idx, 'address'] = address
    else: 
        data.loc[idx, 'geometry'] = None
        data.loc[idx, 'address'] = None
    
    #save to Shapefile
CRS = pycrs.parser.from_epsg_code(4326).to_proj4()
geodf = gpd.GeoDataFrame(data, geometry='geometry', crs=CRS)
outfp = r"C:\Users\cscuser\Desktop\16.1.addresses.shp"
geodf.to_file(outfp)
geo2 = gpd.read_file(outfp)


