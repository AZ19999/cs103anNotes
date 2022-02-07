'''
    Graph
'''

from PointList import *
from Point import *
import matplotlib.pyplot as plt

class Graph(PointList):

    def __init__(self,points):
        super().__init__(points)  # call the parent initializer

    def scatter(self):
        xs = [p.x for p in self.points]
        ys = [p.y for p in self.points]
        plt.scatter(xs,ys)
        plt.grid()
        plt.show()


    def line(self):
        xs = [p.x for p in self.points]
        ys = [p.y for p in self.points]
        plt.plot(xs,ys)
        plt.grid()
        plt.show()
        
if __name__ == '__main__':
    g = Graph([])
    for p in [Point(0,5),Point(1,4),Point(2,2),Point(3,9),Point(0,0)]:
        g.add_point(p)
    g.scatter()

    
    
