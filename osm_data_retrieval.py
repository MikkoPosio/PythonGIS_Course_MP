# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:59:47 2018

@author: Mikko Posio
"""



import osmnx as ox
import matplotlib.pyplot as plt
#specify the place what you are Looking for
place_name = 'Kamppi, Helsinki, Finland'

#Fetch the street

graph = ox.graph_from_place(place_name)

#Plot
fig, ax = ox.plot_graph(graph)

#graph_map = ox.plot_graph_folium(graph)
#outfp = r"C:\Users\cscuser\Desktop\16.1\folium"
#graph_map.save(outfp)

buildings = ox.buildings_from_place(place_name)
buildings.plot()

# Fetch region foot print

footprint = ox.gdf_from_place(place_name)

# Convert the graph to nodes and edges GeoDataFrame

nodes, edges = ox.graph_to_gdfs(graph)

# Define the figure, ax
fig, ax = plt.subplots()
footprint.plot(ax=ax, facecolor='black')
buildings.plot(ax=ax, facecolor='khaki', alpha=0.7)
edges.plot (ax=ax, linewidth=1, edgecolor='#CD5C5C')
