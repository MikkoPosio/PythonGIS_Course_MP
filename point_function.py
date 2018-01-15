# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from shapely.geometry import Point 
def createPointGeom(x_coord=None, y_coord=None):
    """ Returns Shapely Point object from Coordinates"""
    if type(x_coord) == float and type(y_coord) == float:
        return Point(x_coord, y_coord)
    else:
        print("Coordinate should be floats")
        
    

my_point = createPointGeom(x_coord=2.0,y_coord=3.5) #here must be float, not work if int
print(my_point)