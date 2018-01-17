# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:52:40 2018

@author: Mikko Posio
"""


import rasterio
from rasterio.mask import mask
from shapely.geometry import box
import pycrs
import geopandas as gpd
from rasterio.plot import show
from fiona.crs import from_epsg

import rasterio


#Filepath
fp = r'C:\Users\cscuser\Desktop\17.1\p188r018_7t20020529_z34__LV-FIN.tif'
outfp = r'C:\Users\cscuser\Desktop\17.1\Helsinki_clipped_p188r018_7t20020529_z34__LV-FIN.tif'

#read file
data = rasterio.open(fp)

# Create a bounding box

minx, miny, = 24.6, 60.0
maxx, maxy = 25.22, 60.35
bbox = box(minx, miny, maxx, maxy)

#Parse the EPSG code automatically from the raster CRS
epsg_code = int(data.crs.data['init'][5:])

#Create a DataFrame of the bounding box
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

#Reproject the data to the same one as the raster
#geo = geo.to_crs(pycrs.parser.from_epsg_code(epsg_code).to_proj4())
geo = geo.to_crs(crs=data.crs.data)
#Exract the coordinates in a format that rasterio wants them
def getFeatures(gdf):
    """ Parses the coordinates from a GeoDatFrame in a format that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

# Parse the coordinates
coords = getFeatures(geo)

#Clip the raster based on the Polygon
out_img, out_transform = mask(raster=data, shapes=coords, crop=True)

#save the raster to disk
#------------------------

proj4_txt = pycrs.parser.from_epsg_code(epsg_code).to_proj4()

#Update the metadata of our new clipper raster

out_meta = data.meta.copy()
out_meta.update( {'driver': 'Gtiff',
                     'height': out_img.shape[1],
                     'width' : out_img.shape[2],
                     'transform' : out_transform,
                     'crs': proj4_txt
                     } )

    #save the clipped raster to disk
with rasterio.open(outfp, 'w', **out_meta) as dest:
    dest.write(out_img)

#open 
clipped = rasterio.open(outfp)
show((clipped, 5), cmap='terrain')


    


