# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:36:22 2018

@author: Mikko Posio
"""

import rasterio
from rasterio.plot import show
import numpy as np
# File Path

fp = r"C:\Users\cscuser\Desktop\17.1\p188r018_7t20020529_z34__LV-FIN.tif"

#Open the file for reading
raster = rasterio.open(fp)

#Check the crs
CRS = raster.crs

#Check affine transform
affine = raster.transform

#dimensions
width = raster.width
height = raster.height

# Check band count
band_cnt = raster.count

#Check bounds
bounds = raster.bounds

#Driver
dataformat = raster.driver

# Meta data from the raster

meta = raster.meta

#visualize data
show(raster)

#================================
#Get data from channels and calculate statistics
#===================================================

red = raster.read(3)  # show(nir[0:5,0:5])
nir = raster.read(4) 

#Check datatype
dtype = red.dtype

# Empty pixel https://mapbox.github.io/rasterio/topics/masks.html

# Calculate the stats for all channels

stats = []

# Read all bands at one go
bands = raster.read()

for band in bands:
    stats.append( {'min':band.min(), 
                   'max' : band.max(),
                   'median': np.median(band), #median on np(numpyssa), muut band
                   'mean': band.mean()
                   } 
                )
stats
    # Visualize near infrared
show(nir, cmap='terrain')

# Visualize the histogram

from rasterio.plot import show_hist
show_hist(raster, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title='Histogram')



