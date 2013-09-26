from Segment import *
class Node():

    def __init__(self,window, state):
        self.state = state
        self.children = []
        self.window = window

    def addChild(self, node):
        self.children.append(node)

    def children(self):
        return self.connectedNodes

    def drawChildren(self):
        for c in self.children:
            s = Segment(self.window, self.state.copy(), c.state.copy())
            s.draw("green")
      
