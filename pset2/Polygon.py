from operator import itemgetter, attrgetter
import math
import copy
from Point import *
from Segment import *

class Polygon:

    def __init__(self, window, points):
        self.window = window
        self.points = points
        self.segments = []
        self.initial_vertices = []

        for t in points:
            self.initial_vertices.append(Point(t[0],t[1]))
        for i in xrange(0,len(self.initial_vertices)-1):
            self.segments.append(Segment(window, copy.deepcopy(self.initial_vertices[i]),copy.deepcopy(self.initial_vertices[i+1])))
        self.segments.append(Segment(window, copy.deepcopy(self.initial_vertices[-1]), copy.deepcopy(self.initial_vertices[0])))

    def vertices(self):
        vertices =[]
        for s in self.segments:
            vertices.append(s.p1)
        return vertices

    def position(self):
        return self.segments[0].p1.copy()

    def copy(self):
        return Point(self.x,self.y)
      
    def intersect(self, otherPolygon):
        for s in otherPolygon.segments:
            for s1 in self.segments:
                if s.intersect(s1):
                    return True
        return False

    def intersectSeg(self, segment):
        for s in self.segments:
            if s.intersect(segment):
                return True
        return False
    
    def pointInPoly(self,p):
        for s in self.segments:
            if s.crossProduct(p) == 0 or math.copysign(1.0, s.crossProduct(p)) == 1.0:
                return False
        return True

         
    def move(self, position):
        self.segments[0].move(position)
        for i in xrange(1, len(self.segments)):
            self.segments[i].move(self.segments[i-1].p2)

    def rotate(self, angle):
        self.segments[0].rotate(angle)
        for i in xrange(1,len(self.segments)):
            self.segments[i].move(self.segments[i-1].p2)
            self.segments[i].rotate(angle)

    def moveDelta(self, delta_x, delta_y):
        new_position = Point(self.position().x + delta_x, self.position().y + delta_y)
        self.move(new_position)
    
    def draw(self, color = "black"):
        for seg in self.segments:
            seg.draw(color)
    def __str__(self):
        s = "Obstacle: "
        for v in self.vertices():
            s += str(v) + " "
        s += " END"
        return s
    def copy(self):
        points = []
        for v in self.vertices():
            points.append(v.toTuple())
        return Polygon(self.window, points)

