# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:20:05 2018

@author: cscuser
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString

#filepath

txt_fp = r"C:\Users\cscuser\Desktop\Data\travelTimes_2015_Helsinki.txt"
#excel_fp = r"C:\Users\cscuser\Desktop\Data\travelTimes_2015_Helsinki.xlsx"
#stream = open(txt_fp, 'r')
#stream.readline()
#stream.close() #control + 1 change lines to #dfgd

#read the data

data = pd.read_csv(txt_fp, sep=';')
#data = pd.read_excel(excel_fp, sheet_name="travelTimes_2015_Helsinki")
data['origin_point'] = data.apply(lambda row: Point(row['from_x'], row['from_y']), axis=1)
data['dest_point'] = data.apply(lambda row: Point(row['to_x'], row['to_y']), axis=1)

# create a GeoDataFrame
geo = gpd.GeoDataFrame(data, geometry='dest_point', crs={'init':'epsg4326'})
#create LineString between points
geo['line'] = geo.apply(lambda row: LineString([row['origin_point'], row['dest_point']]), axis=1)
geo = geo.set_geometry('line')
geo[0:10].plot()
