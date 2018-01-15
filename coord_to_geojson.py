# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:20:05 2018

@author: cscuser
"""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

#filepath

txt_fp = r"C:\Users\cscuser\Desktop\Data\travelTimes_2015_Helsinki.txt"

#stream = open(txt_fp, 'r')
#stream.readline()
#stream.close() #control + 1 change lines to #dfgd

#read the data

data = pd.read_csv(txt_fp, sep=';')
