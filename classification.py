# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:46:14 2018

@author: Mikko Posio
"""

import geopandas as gpd
import pysal as ps

# Filepath
fp = r'C:\Users\cscuser\Desktop\16.1\TravelTimes_to_5975375_RailwayStation.shp'
data = gpd.read_file(fp)

# Plot the data
data.plot(column='pt_r_t')

#remove No data with -1 value
#Select rows where 'pt_r_t' >=0
data = data.loc[data['pt_r_t']>=0]

#plot the data
data.plot(column='pt_r_t', scheme='quantiles', k=9, cmap='RdYlBu', linewidth=0)
# Classify the data values in GeoDataFrame

n_classes = 9

#Initialize classifier
classifier = ps.Natural_Breaks.make(k=n_classes)

# Do the classification
classification = data[['pt_r_t']].apply(classifier)

#rename the column to keep track on the classification method
classification.columns = ['pt_r_t_nb9']
# join the data back to the original DF

data = data.join(classification)

#Plot
data.plot(column='pt_r_t_nb9', linewidth=0, cmap='RdYlBu')
