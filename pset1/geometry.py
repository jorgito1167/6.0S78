import copy
import math
from DrawingWindowStandalone import *

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveDelta(self,delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def move(self, x, y):
        self.x = x
        self.y = y

    def toTuple(self):
        return (self.x,self.y)

    def equal(self, otherPoint):
        if (self.x == otherPoint.x) and (self.y == otherPoint.y):
            return True
        return False

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)


class Segment:
    
    def __init__(self, window, p1, p2):
        self.window = window
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        self.window.drawLineSeg(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def moveDelta(self, delta_x, delta_y):
        self.p1.move(delta_x, delta_y)
        self.p2.move(delta_x, delta_y)

    def move(self, p):
        delta_x = p.x - self.p1.x
        delta_y = p.y - self.p1.y
        self.p1.move(p.x,p.y)
        self.p2.moveDelta(delta_x, delta_y)

    def intersect(self, segment):
        sign = [0,0,0,0]
        sign[0]  = math.copysign(1.0, self.crossProduct(segment.p1))
        sign[1]  = math.copysign(1.0, self.crossProduct(segment.p2))
        sign[2]  = math.copysign(1.0, segment.crossProduct(self.p1))
        sign[3]  = math.copysign(1.0, segment.crossProduct(self.p2))

        if (sign[0] == sign[1]) or (sign[2] == sign[3]):
            return False

        return True

    def crossProduct(self,p):
        u1 = p.x - self.p1.x
        u2 = p.y - self.p1.y
        v1 = self.p2.x - self.p1.x
        v2 = self.p2.y - self.p1.y

        return (u1*v2 - u2*v1)


class Polygon:

    def __init__(self, window, points):
        self.segments = []
        self.vertices = []
        for t in points:
            self.vertices.append(Point(t[0],t[1]))
        for i in xrange(0,len(self.vertices)-1):
            self.segments.append(Segment(window, copy.deepcopy(self.vertices[i]),copy.deepcopy(self.vertices[i+1])))
        self.segments.append(Segment(window, copy.deepcopy(self.vertices[-1]), copy.deepcopy(self.vertices[0])))

    def intersect(self, otherPolygon):
        for s in otherPolygon.segments:
            for s1 in self.segments:
                if s.intersect(s1):
                    return True
        return False
         
    def move(self, position):
        self.segments[0].move(position)
        for i in xrange(1, len(self.segments)):
            self.segments[i].move(self.segments[i-1].p2)
    
    def draw(self):
        for seg in self.segments:
            seg.draw()

class Robot:

    def __init__(self, polygons):
        self.initial_position = polygons[0].segments[0].p1
        self.position = self.initial_position
        self.polygons = polygons

    def draw(self):
        for polygon in self.polygons:
            polygon.draw()

    def setPosition(self, position):
        #fix to move all polygons to desired position
        for polygon in self.polygons:
            polygon.move(position)

    def intersect(self, polygon):
        for part in self.polygons:
            if polygon.intersect(part):
                return True
        return False

        

class Obstacle:
  
    def __init__(self, polygon, velocity=(0,0), boundary = False):
        self.initial_position = polygon.segments[0].p1
        self.position = self.initial_position
        self.velocity = velocity #tuple of (v_x, v_y)
        self.polygon = polygon

    def setPosition(self, time_step):
        self.position.x = self.initial_position.x + time_step* self.velocity[0]
        self.position.y = self.initial_position.y + time_step* self.velocity[1]

        self.polygon.move(self.position)

    def draw(self):
        self.polygon.draw()


