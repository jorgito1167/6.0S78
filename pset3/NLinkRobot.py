import copy
import math
from DrawingWindowStandalone import *

from operator import itemgetter, attrgetter
from Polygon import *
 

class NLinkRobot():

    def __init__(self, links, number_of_links = 3, identical_links = False):
        self.number_of_links = number_of_links
        self.identical_links = identical_links
        if identical_links:
            self.links = [links.copy() for x in range(number_of_links)]
        else:
            self.links = links 


    def draw(self, color= "black"):
        for polygon in self.link:
            polygon.draw(color)

    def copy(self):
        if self.identical_links:
            return NLinkRobot(self.polygons, self.number_of_links, self.identical_links)
        else:
            return NLinkRobot(self.polygons)
            
    def setPosition(self, angles):
        for i in xrange(len(self.polygons)):
            self.polygons[i].move(position + self.offsets[i])
    
    def intersect(self, polygon):
        for part in self.links:
            if polygon.intersect(part):
                return True
        return False

    
