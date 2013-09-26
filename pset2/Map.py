from Obstacle import *
from Robot import *

class Map():
    
    def __init__(self, obstacles, robot):
        self.obstacles = obstacles
        self.robot = robot
        self.getCSpace()

    def getCSpace(self, angle=0):
        self.CSpace = []
        #robot.rotate(angle)
        for o in self.obstacles:
            o.getCSpace(self.robot)
            self.CSpace.extend(o.CSpace)
    
    def vertices(self):
        vertices = []
        for o in self.obstacles:
            vertices.extend(o.mapVertices())
        return vertices

    def isSegLegal(self, segment):
        for p in self.CSpace:
            if p.intersectSeg(segment) or p.pointInPoly(segment.midpoint()):
                return False
        return True
        
