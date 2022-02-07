'''
    Point - an (x,y) point in the 2d plain
'''

class Point():

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def __repr__(self):
        return "Point("+str(self.x)+","+str(self.y)+")"

    def add(self,p):
        return Point(self.x+p.x,self.y+p.y)

    def sub(self,p):
        return Point(self.x-p.x,self.y-p.y)

    def dot(self,p):
        return self.x*p.x + self.y*p.y
