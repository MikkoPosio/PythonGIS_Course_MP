# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:08:39 2018

@author: cscuser
"""

from shapely.geometry import Point
from shapely.geometry import Polygon 
def createPointGeom(x_coord=None, y_coord=None):
    """ Returns Shapely Point object from Coordinates"""
    if type(x_coord) == float and type(y_coord) == float:
        return Point(x_coord, y_coord)
    else:
        print("Coordinate should be floats")
        
def creatPolyGeom(points=None):
    if type(points)!= list:
        print ("The input should inside a list")
    elif len(points) > 0:
        
        coords = []
        for point in point:
            if not type(point) == Point:
                coords.append(point)
            else:
                coords.append((point.x, point.y)
                        
        print(coords)
        return Polygon(coords)
            
            