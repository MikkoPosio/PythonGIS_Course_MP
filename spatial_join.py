# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:07:43 2018

@author: cscuser
"""

import geopandas as gpd

# File Path

pop_fp = r'C:\Users\cscuser\Desktop\16.1\join tables\Vaestotietoruudukko_2015.shp'
address_fp = r'C:\Users\cscuser\Desktop\16.1\16.1.addresses.shp'

#read the files

pop = gpd.read_file(pop_fp)
address = gpd.read_file(address_fp)

# Exlude the NaNs

pop = pop.dropna(subset=['geometry'])
address = address.dropna(subset=['geometry'])

# Reproject the data

address = address.to_crs(pop.crs)

#Spatial join
join = gpd.sjoin(address, pop, op='within')
join2 = gpd.sjoin(pop, address, op='contains')

# 
