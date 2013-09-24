import copy
import math
from DrawingWindowStandalone import *

from operator import itemgetter, attrgetter

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
    def reverse(self):
        p1 = self.p1
        p2 = self.p2
        self.p1 = p2
        self.p2 = p1

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

    def normalAngle(self, side):
        if side == "right":
            x = (self.p2.y - self.p1.y)
            y = -(self.p2.x - self.p1.x)
        else:
            x = -(self.p2.y - self.p1.y)
            y = (self.p2.x - self.p1.x)
        print x, y
        if y<0:
          sign = -1
        else:
          sign = 1

        return sign*math.degrees(math.acos(x/math.sqrt(math.pow(x,2) + math.pow(y,2))))

    def __str__(self):
        return "P1: " + str(self.p1) + " P2: " + str(self.p2)


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

        self.position = self.segments[0].p1      

    def vertices(self):
        vertices =[]
        for s in self.segments:
            vertices.append(s.p1)
        return vertices

    def position(self):
        return self.segments[0].p1
      
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

    def moveDelta(self, delta_x, delta_y):
        new_position = Point(self.position.x + delta_x, self.position.y + delta_y)
        self.move(new_position)
    
    def draw(self):
        for seg in self.segments:
            seg.draw()
    def __str__(self):
        s = ""
        for v in self.vertices():
            s += str(v) + " "
        return s
    def copy(self):
        points = []
        for v in self.vertices():
            points.append(v.toTuple())
        return Polygon(self.window, points)

class Robot:

    def __init__(self, polygons):
        self.initial_position = polygons[0].segments[0].p1
        self.position = self.initial_position
        self.polygons = polygons
        self.extendedX = self.extendPolygon(1,0) # different initial point
        self.extendedY = self.extendPolygon(0,1)

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

    def findMinMax():
        #0 for x axis, 1 for y axis
        if axis == "x":
            sortAxis = sorted(self.vertices(), key = lambda vertex: vertex.x)
        else:
            sortAxis = sorted(self.vertices(), key = lambda vertex: vertex.y)

        return (sortAxis[0], sortAxis[-1])


    def extendPolygon(self, delta_x, delta_y):

        if delta_x == 1:
            s = sorted(self.polygons[0].vertices(), key = attrgetter('x'), reverse = True)
            s1 = sorted(s, key=attrgetter('y'))
            s2 = sorted(self.polygons[0].vertices(), key = attrgetter('y', 'x'))


        else:
            s = sorted(self.polygons[0].vertices(), key = attrgetter('y'), reverse = True)
            s1 = sorted(s, key=attrgetter('x'))
            s2 = sorted(self.polygons[0].vertices(), key = attrgetter('x','y'))

        (min_v, max_v) = (s1[0], s2[-1])
        #print min_v
        #print max_v
        
        min_v_index = self.polygons[0].vertices().index(min_v)  
        max_v_index = self.polygons[0].vertices().index(max_v)  

        if delta_x ==1:
            if min_v_index <= max_v_index:
                max_v_index += 2
            else:
                max_v_index += 1
        
        if delta_y ==1:
                min_v_index += 1
                max_v_index += 1
            
        
        new_vertices = list(copy.deepcopy(self.polygons[0].points))
        #print "Before: " + str(new_vertices)
        new_min_v = [min_v.x + delta_x, min_v.y + delta_y]
        new_max_v = [max_v.x + delta_x, max_v.y + delta_y]
        #print "min index: " + str(min_v_index)
        #print "max index: " + str(max_v_index)
        new_vertices.insert(min_v_index, new_min_v)
        new_vertices.insert(max_v_index, new_max_v)
        mini = min(new_vertices.index(new_max_v) , new_vertices.index(new_min_v))
        maxi = max(new_vertices.index(new_max_v) , new_vertices.index(new_min_v))
        #print new_vertices
        for i in xrange(mini + 1, maxi):
            #print i
            new_vertices[i][0] += delta_x
            new_vertices[i][1] += delta_y

        #print new_vertices

        return Polygon(self.polygons[0].window, new_vertices)



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
        print "Before: "
        print self.polygon
        print polygon
        p1 = sorted(self.polygon.vertices(), key = attrgetter('x','y'), reverse = True)[0]
        p2 = sorted(polygon.vertices(), key = attrgetter('x','y'), reverse = True)[0]
        return (p1.x - p2.x , p1.y - p2.y)


    def getCSpace(self, robot):
        segments = [] 
        obs = self.polygon.copy()
        rob = robot.polygons[0].copy()

        for i in obs.segments:
            segments.append((copy.copy(i), i.normalAngle("left"),"o"))

        for j in rob.segments:
            segments.append((copy.copy(j), j.normalAngle("right"),"r"))

        sorted_segments = sorted(segments, key= itemgetter(1))
        
        #for s in sorted_segments:
        #    print s[0]
        for i in xrange(1, len(sorted_segments)):
            if sorted_segments[i][2] == "o":
                sorted_segments[i][0].reverse()
            sorted_segments[i][0].move(sorted_segments[i-1][0].p2)
        #print "After: "
        #for s in sorted_segments:
        #    print s[0]
        vertices =[]

        for s in sorted_segments:
            vertices.append(s[0].p1.toTuple())
        
        tempPoly = Polygon(self.polygon.window, vertices)
        delta = self.findDelta(tempPoly)
        print delta
        tempPoly.moveDelta(delta[0],delta[1])
        print "After: "
        print tempPoly
        self.CSpace = tempPoly

        

        

        



