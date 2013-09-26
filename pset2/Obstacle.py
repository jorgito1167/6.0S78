import copy
import math
from DrawingWindowStandalone import *

from operator import itemgetter, attrgetter

from Polygon import *

class Obstacle:
  
    def __init__(self, polygon, velocity=(0,0), boundary = False):
        self.initial_position = polygon.segments[0].p1
        self.position = self.initial_position
        self.velocity = velocity #tuple of (v_x, v_y)
        self.polygon = polygon
        self.CSpace = []

    def setPosition(self, time_step):
        self.position.x = self.initial_position.x + time_step* self.velocity[0]
        self.position.y = self.initial_position.y + time_step* self.velocity[1]

        self.polygon.move(self.position)

    def draw(self, color = "black"):
        self.polygon.draw(color)

    def drawCSpace(self, color = "black"):
        for p in self.CSpace:
            p.draw(color)
    
    def mapVertices(self):
        vertices = []
        segments = []
        polys = []
        for p in self.CSpace:

            vertices.extend(p.vertices())
            segments.extend(p.segments)
            polys.append(p)
        map_vertices = []
        for v in vertices:
            inPoly = False
            for p in polys:
                if p.pointInPoly(v):
                    inPoly = True
            inSeg = False
            for s in segments:
                if s.pointInSeg(v):
                    inSeg = True
            if (not inSeg) and (not inPoly):
                map_vertices.append(v)
        return map_vertices
            
        


    def findDelta(self,polygon):
        p1 = sorted(self.polygon.vertices(), key = attrgetter('x','y'), reverse = True)[0]
        p2 = sorted(polygon.vertices(), key = attrgetter('x','y'), reverse = True)[0]
        return (p1.x - p2.x , p1.y - p2.y)

    def trimCSpace(self):
        tCSpace =[]
        for p in self.CSpace:
            vertices = p.vertices()
            new_vertices = []
            for i in xrange(-1, len(vertices)-1):
                s = Segment(p.window, vertices[i-1].copy(), vertices[i+1].copy())
                if not s.pointInSeg(vertices[i]):
                    new_vertices.append(vertices[i].toTuple())
            tCSpace.append(Polygon(p.window,new_vertices))
        self.CSpace = tCSpace
                    
            

    def getCSpace(self, robot):
        self.CSpace = []
        for poly in robot.polygons:
            self.CSpace.append(self.getPolyCSpace(poly))
        for i in xrange(len(self.CSpace)):
            self.CSpace[i].moveDelta(-robot.offsets[i].x, -robot.offsets[i].y)
        self.trimCSpace()

    def getPolyCSpace(self, polygon):
        segments = [] 
        obs = self.polygon.copy()
        
        rob = polygon.copy()

        for i in obs.segments:
            segments.append((i.copy(), i.normalAngle("left"),"o"))

        for j in rob.segments:
            segments.append((j.copy(), j.normalAngle("right"),"r"))

        sorted_segments = sorted(segments, key= itemgetter(1))
            
        if sorted_segments[0][2] == "o":
            sorted_segments[0][0].reverse()

        for i in xrange(1, len(sorted_segments)):
            if sorted_segments[i][2] == "o":
                sorted_segments[i][0].reverse()
            sorted_segments[i][0].move(sorted_segments[i-1][0].p2)

        vertices =[]

        for s in sorted_segments:
            vertices.append(s[0].p1.toTuple())

        tempPoly = Polygon(self.polygon.window, vertices)
        delta = self.findDelta(tempPoly)
        tempPoly.moveDelta(delta[0],delta[1])
        return tempPoly


 
