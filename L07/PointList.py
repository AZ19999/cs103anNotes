'''
    PointList -- a list of 2d points
'''

from Point import *

class PointList():

    def __init__(self,points):
        self.points = points

    def add_point(self,point):
        self.points.append(point)

    def __str__(self):
        s = "["
        for i in range(len(self.points)-1):
            s += self.points[i]+","
        s += self.points[-1]+"]"
        return s
    
    def remove_point(self,i):
        del self.points[i]
