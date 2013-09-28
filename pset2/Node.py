from Segment import *
class Node():

    def __init__(self,window, position, angle):
        self.state = (position,angle)
        self.children = []
        self.window = window

    def addChild(self, node):
        self.children.append(node)

    def drawChildren(self):
        for c in self.children:
            s = Segment(self.window, self.state.copy(), c.state.copy())
            s.draw("green")

    def draw(self, color = "black"):
        self.window.drawPoint(self.state.x, self.state.y,color)
      
