from Obstacle import *
from Robot import *

class Map():
    
    def __init__(self, obstacles, robot, min_angle=0, max_angle=90):
        self.obstacles = obstacles
        self.robot = robot.copy()
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.getAllCSpaces()

    def getAllCSpaces(self):
        self.CSpaces = []
        for angle in xrange(self.min_angle, self.max_angle+1):
            self.CSpaces.append(self.getCSpace(angle))
            

    def getCSpace(self, angle=0):
        CSpace = []
        robot = self.robot.copy()
        robot.rotate(angle)
        for o in self.obstacles:
            c = o.copy()
            c.getCSpace(robot)
            CSpace.append(c)
        return CSpace

    def pointInCSpace(self,i, point):
        for o in self.CSpaces[i]:
            for p in o.CSpace:
                if p.pointInPoly(point):
                    return False
        return True
    
    def vertices(self,i):
        vertices = []
        for o in self.CSpaces[i]:
            vertices.extend(o.mapVertices())
        return vertices

    def isSegLegal(self, segment, i):
        for o in self.CSpaces[i]:
            for p in o.CSpace:
                if p.intersectSeg(segment) or p.pointInPoly(segment.midpoint()):
                    return False
        return True
        
