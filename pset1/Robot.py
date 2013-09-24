import copy
import math
from DrawingWindowStandalone import *

from operator import itemgetter, attrgetter
from Polygon import *
 

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


