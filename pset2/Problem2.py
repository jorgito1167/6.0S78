from DrawingWindowStandalone import *
import copy
import math
from geometry import *
from utils import *
from Map import *
from VisibilityGraph import *

if __name__ == "__main__":
    (window,bounds) = makeRoom(0,100,0,100)
    head_points = ([0,0], [3,7], [5,0])
    head = Polygon(window, head_points)
    head.move(Point(12,17))

    s = Segment(window, Point(20,10), Point(20,40))
    torso_points = ((0,0), (0,7),(7,7), (7,0))
    torso = Polygon(window,torso_points)
    torso.move(Point(10,10))

    robot = Robot([torso, head])
    #robot.draw()

    robot.setPosition(Point(30,30))
    #robot.draw()
    #robot.extendedX.move(Point(5,15))
    #robot.extendedX.draw()
    #robot.extendedY.move(Point(15,5))
    #robot.extendedY.draw()


    vertices1 = ([0,0], [0,20], [40,10])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(50,20))
    obs1 = Obstacle(poly1)
    #obs1.draw('blue')
    obs1.getCSpace(robot)
    obs1.drawCSpace('red')

    vertices2 = ((0,0), (0,15),(40,15), (40,0))
    poly2 = Polygon(window, vertices2)
    poly2.move(Point(20, 60))
    obs2 = Obstacle(poly2)
    #obs2.draw('blue')
    obs2.getCSpace(robot)
    obs2.drawCSpace('red')

    visi = VisibilityGraph(window,Point(5,20), Point(90,90), [obs1,obs2], robot)
    print len(visi.nodes)
    visi.nodes[10].drawChildren()
    '''
    #obs1.draw('blue')
    #obs1.getCSpace(robot)
    obs1.drawCSpace('red')
    #obs2.draw('blue')
    #obs2.getCSpace(robot)
    obs2.drawCSpace('red')
    '''
    window.tk.mainloop()
