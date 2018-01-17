# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:42:36 2018

@author: Mikko Posio
"""
import rasterio
from rasterio.plot import show
from rasterstats import zonal_stats
import osmnx as ox
import geopandas as gpd
from fiona.crs import from_epsg

#Filepath
dem_fp = r'C:\Users\cscuser\Desktop\17.1\Raster_data\Helsinki_DEM_2x2m_Mosaic.tif'
dem = rasterio.open(dem_fp)


#Specify the names of the areas
kallio_q = 'Kallio, Helsinki, Finland'
pihla_q = 'Pihlajamäki, Malmi, Helsinki, Finland'

#Fletch the polygons from OSM

kallio = ox.gdf_from_place(kallio_q)
pihla = ox.gdf_from_place(pihla_q)

#Reproject to the same CRS as raster
kallio = kallio.to_crs(epsg=3067) 
pihla = pihla.to_crs(epsg=3067)
#Plot
ax=show((dem, 1))
kallio.plot(ax=ax, facecolor='None', edgecolor='red', linewidth=2)
pihla.plot(ax=ax, facecolor='None', edgecolor='blue', linewidth=2)

#Fetch the elevation values
heigths = dem.read(1)
affine = dem.affine

# Conduct the zonal statistics
zs_kallio = zonal_stats(kallio, heigths, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
zs_pihla = zonal_stats(pihla, heigths, affine=affine, stats=['min', 'max', 'mean', 'median', 'majority'])
