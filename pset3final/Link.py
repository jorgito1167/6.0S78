from Polygon import *
from Segment import *


class Link(Polygon):

    def __init__(self, window, points, r1, r2):
        Polygon.__init__(self, window, points)
        self.offsets = []
        self.connected_links = []
        self.offsets.append(Segment(window, Point(r1[0],r1[1]), self.segments[0].p1.copy()))
        self.offsets.append(Segment(window, Point(r1[0],r1[1]), Point(r2[0], r2[1]))) 

    def move(self, position):
        self.offsets[0].move(position)
        self.offsets[1].move(position)
        Polygon.move(self, self.offsets[0].p2)

    def rotate(self, angle):
        self.offsets[0].rotate(angle)
        self.offsets[1].rotate(angle)
        self.segments[0].move(self.offsets[0].p2)
        Polygon.rotate(self, angle)
        for link in self.connected_links:
            link.move(self.offsets[1].p2)
            link.rotate(angle)

    def connect(self, link):
        link.move(self.offsets[1].p2)
        self.connected_links.append(link)

    def updateJoint(self, position, angle):
        pass

    def draw(self, color="black"):
        self.window.drawPoint(self.offsets[0].p1.x,self.offsets[0].p1.y)
        self.window.drawPoint(self.offsets[1].p2.x,self.offsets[1].p2.y)
        Polygon.draw(self,color)

    def copy(self):
        return Link(self.window, self.points,self.offsets[0].p1.toTuple(),self.offsets[1].p2.toTuple())
