'''
    Polygon -- a list of points defining a region in the 2d plane
'''

from Point import *
from PointList import *
import math

class Polygon(PointList):  # a Polygon is a Pointlist with more features!

    def __init__(self,points):
        super().__init__(points)


    def name(self):
        n = len(self.points)
        if n==0:
            return "empty"
        elif n==1:
            return "point"
        elif n==2:
            return "line"
        elif n==3:
            return "triangle"
        elif n==4:
            return "quadrilateral"
        elif n==5:
            return "pentagon"
        elif n==6:
            return "hexagon"
        elif n==7:
            return "septagon"
        elif n==8:
            return "octagon"
        elif n==9:
            return "nonagon"
        elif n==10:
            return "decagon"
        else:
            return str(n)+"-gon"

    def _distance(self,p1,p2):
        d = math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
        return d

    def perimeter(self):
        total = 0
        n = len(self.points)
        for i in range(n):
            p = self.points[i]
            q = self.points[(i+1)%n]
            total += self._distance(p,q)
        return total

    def area(self):
        total = 0
        for i in range(len(self.points)):
            n = len(self.points)
            p = self.points[i]
            q = self.points[(i+1) % n]
            # calculate the signed area of the triangle with vertices (0,0),p,q
            triangle_area = (p.x*q.y - p.y*q.x)/2
            total += triangle_area
        return total

    def is_convex(self):
        n = len(self.points)
        for i in range(n):
            p = self.points[(i+1)%n]
            q = self.points[i]
            pq = p.sub(q)
            for j in range(n):
                s = self.points[(i+j)%n]
                sq = s.sub(q)  
                if pq.dot(sq)<0:
                    return False
        return True

    def __str__(self):
        pname = self.name()
        s = pname+"(" + ",".join([p.__str__() for p in self.points]) + ")"
        return s
        
    def print_description(self):
        
        print('here is the polygon:',self)
        print('the polygon is a',self.name())
        print('it has an area of',self.area())
        print('and a perimeter of',self.perimeter())
        print('is it convex?',self.is_convex())

    
if __name__ == '__main__':
    s = Polygon([])
    s.add_point(Point(0,0))
    s.add_point(Point(1,0))
    s.add_point(Point(1,1))
    s.add_point(Point(0,1))
    s.add_point(Point(0.5,0.5))
    s.print_description()
    print("\n ******* \n")
    s = Polygon([Point(0,0),Point(6,0),Point(6,6),Point(0,6),Point(4,3)])
    s.print_description()

    
    
