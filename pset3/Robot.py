import copy
import math
from DrawingWindowStandalone import *

from operator import itemgetter, attrgetter
from Polygon import *
 

class Robot:

    def __init__(self, polygons):
        self.polygons = polygons
        self.offsets = []
        for p in polygons:
            self.offsets.append(p.position() - polygons[0].position())
            

    def draw(self, color= "black"):
        for polygon in self.polygons:
            polygon.draw(color)

    def position(self):
        return self.polygons[0].position()

    def copy(self):
        return Robot(self.polygons)

    def setConfig(self,config):
        self.setPosition(Point(config[0],config[1]))
        self.rotate(config[2])

    def setPosition(self, position):
        for i in xrange(len(self.polygons)):
            self.polygons[i].move(position + self.offsets[i])
    
    def rotate(self,angle):
        for i in xrange(len(self.offsets)):
            point = self.offsets[i]
            x = point.x 
            y = point.y 
            a  = math.radians(angle)
            new_x = math.cos(a)*x - math.sin(a)*y
            new_y = math.sin(a)*x + math.cos(a)*y
            self.offsets[i].x = new_x 
            self.offsets[i].y = new_y 
        for p in self.polygons:
            p.rotate(angle)
        self.setPosition(self.position())
            

    def intersect(self, polygon):
        for part in self.polygons:
            if polygon.intersect(part):
                return True
        return False


