# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:03:33 2018

@author: Mikko Posio
""" 
import geopandas as gpd
import matplotlib.pyplot as plt

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

address_fp= r'C:\Users\cscuser\Desktop\16.1\16.1.addresses.shp'
poly_fp = r'C:\Users\cscuser\Desktop\16.1\PKS_suuralue.kml'

#  Read files

address = gpd.read_file(address_fp)
poly = gpd.read_file(poly_fp, driver= 'KML')


#Select region
southern = poly.loc[poly['Name'] == 'Eteläinen']
#reset the index

southern = southern.reset_index(drop=True)

#Create a mask of the points what are withing the area

pip_mask = address.within(southern.loc[0, 'geometry'])
# select the rows that were inside the polygon
pip_data = address.loc[pip_mask]

#Visualize the selection
fig, ax = plt.subplots()
poly.plot(ax=ax, facecolor='grey')
southern.plot(ax=ax, facecolor='red')
address.plot(ax=ax, facecolor='blue', markersize=6)
pip_data.plot(ax=ax, color='gold', markersize=6)

#Select points that were not under 'Eteläinen' area
#address_outpoly= address.loc[~address['id'].isin(pip_data['id'])] #~ make opposite what else do
address_outpoly= address.loc[~pip_mask]
