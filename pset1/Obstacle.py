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
        self.CSpace = None

    def setPosition(self, time_step):
        self.position.x = self.initial_position.x + time_step* self.velocity[0]
        self.position.y = self.initial_position.y + time_step* self.velocity[1]

        self.polygon.move(self.position)

    def draw(self):
        self.polygon.draw()

    def findDelta(self,polygon):
        p1 = sorted(self.polygon.vertices(), key = attrgetter('x','y'), reverse = True)[0]
        p2 = sorted(polygon.vertices(), key = attrgetter('x','y'), reverse = True)[0]
        return (p1.x - p2.x , p1.y - p2.y)


    def getCSpace(self, robot):
        segments = [] 
        obs = self.polygon.copy()
        
        rob = robot.polygons[0].copy()

        for i in obs.segments:
            segments.append((i.copy(), i.normalAngle("left"),"o"))

        for j in rob.segments:
            segments.append((j.copy(), j.normalAngle("right"),"r"))

        sorted_segments = sorted(segments, key= itemgetter(1))
            
        if sorted_segments[0][2] == "o":
            sorted_segments[0][0].reverse()

        for i in xrange(1, len(sorted_segments)):
            if sorted_segments[i][2] == "o":
                print sorted_segments[i][0]
                sorted_segments[i][0].reverse()
            sorted_segments[i][0].move(sorted_segments[i-1][0].p2)

        vertices =[]

        for s in sorted_segments:
            vertices.append(s[0].p1.toTuple())

        tempPoly = Polygon(self.polygon.window, vertices)
        delta = self.findDelta(tempPoly)
        tempPoly.moveDelta(delta[0],delta[1])
        self.CSpace = tempPoly

 
