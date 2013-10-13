import copy
import math
from DrawingWindowStandalone import *

from operator import itemgetter, attrgetter
from Polygon import *
 

class NLinkRobot():

    def __init__(self, links, number_of_links = 3, identical_links = False):
        self.number_of_links = number_of_links
        self.identical_links = identical_links
        self.links = []
        if identical_links:
            self.position = links.offsets[0].p1.copy()
            self.links.append(links.copy())
            for i in range(1,number_of_links):
                self.links.append(links.copy())
                self.links[i-1].connect(self.links[i])
        else:
            self.position = links[0].offsets[0].p1
            self.links = links 
        self.initial_config = links


    def draw(self, color= "black"):
        for link in self.links:
            link.draw(color)

    def copy(self):
        if self.identical_links:
            return NLinkRobot(self.polygons, self.number_of_links, self.identical_links)
        else:
            return NLinkRobot(self.polygons)
            
    def setPosition(self, angles):
        self.reset() 
        for i in xrange(len(self.links)):
            self.links[i].rotate(angles[i]) 

    def moveBase(self, position):
        self.position = position
        self.links[0].move(position)
        for i in xrange(1,self.number_of_links):
            self.links[i].move(self.links[i-1].offsets[1].p2)

    def reset(self):
        self.links = []
        self.links.append(self.initial_config.copy())
        for i in range(1,self.number_of_links):
            self.links.append(self.initial_config.copy())
            self.links[i-1].connect(self.links[i])
        self.moveBase(self.position)

    def intersect(self, polygon):
        for part in self.links:
            if polygon.intersect(part):
                return True
        return False

    
