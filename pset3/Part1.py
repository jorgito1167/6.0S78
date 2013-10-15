from DrawingWindowStandalone import *
import copy
import math
from geometry import *
from CollisionBox import *
from TreeNode import *
from RRT import *

def polyRobot(window):

    head_points = ([0,0], [0,3], [2,1])
    head = Polygon(window, head_points)
    head.move(Point(17,8))

    torso_points = ((0,0), (0,1),(7,1), (7,0))
    torso = Polygon(window,torso_points)
    torso.move(Point(10,10))

    robot = Robot([torso, head])
    robot.setConfig((3,3,60))
    robot.draw()

    robot.setConfig((85,85,20))
    robot.draw()
    
    obstacles = []
    vertices1 = ([0,0], [0,20], [52,7])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(5, 20))
    obstacles.append(poly1)

    vertices2 = ((0,0), (0,10),(60,10), (60,0))
    poly2 = Polygon(window, vertices2)
    poly2.move(Point(10, 75))
    obstacles.append(poly2)

    poly3 = poly2.copy()
    poly3.move(Point(30, 46))
    obstacles.append(poly3)

    poly4 = poly3.copy()
    poly4.move(Point(60, 15))
    obstacles.append(poly4)

    vertices5 = ((0,0), (10,10),(20,10), (30,0), (20,-10), (10, -10))
    poly5 = Polygon(window, vertices5)
    poly5.move(Point(70, 70))
    obstacles.append(poly5)

    for p in obstacles:
        p.draw()
    dimensions = ((5,95,0.5),(5,95,0.5),(0,0,1))
    collision_box = CollisionBox(obstacles, robot)
    rrt = RRT((3,3,0),(85,85,0),collision_box, dimensions,euclideanDistance, 5, 10000)
    node = rrt.run()
    rrt.draw()
    if node!=None:
        parent = node.parent
        while parent!=None:
            s = node.state
            p = parent.state
            window.drawOval((s[0]-1,s[1]+1),(s[0]+1,s[1]-1),'blue')
            window.drawLineSeg(s[0],s[1],p[0],p[1],'blue') 
            node = parent
            parent = node.parent

def nLinkRobot(window):
    obstacles = []
    vertices = ((5,5), (5, 9), (25,9), (25,5))
    link1 = Link(window,vertices,(8,7), (23,7))
    robot = NLinkRobot(link1, 4,True)
    robot.moveBase(Point(50,10))

    robot.setConfig((30,30,30,30))
    robot.draw()

    robot.setConfig((160,-30,-40,-40))
    robot.draw()

    vertices6 = ((0,0), (10,10),(20,10), (30,0), (20,-10), (10, -10))
    poly6 = Polygon(window, vertices6)
    poly6.move(Point(30, 40))
    obstacles.append(poly6)


    for p in obstacles:
        p.draw()

    dimensions = ((-120,160,1),(-120,120,1), (-120,120,1), (-120,120,1))
    collision_box = CollisionBox(obstacles, robot)
    rrt = RRT((30,30,30,30),(160, -30, -40, -40),collision_box, dimensions,euclideanDistance, 5, 10000) 
    node = rrt.run()
    if node!=None:
        parent = node.parent
        count = 15
        color = 4
        node.draw()
        colors = ('yellow','green','red','blue','black')

        while parent!=None:
            if count ==0:
                count = 10
                color -=1
                robot.setConfig(parent.state)
                robot.draw(colors[color])
            else:
                count -=1
            if color ==0:
                color = 4 
            node = parent
            parent = node.parent


if __name__ == "__main__":
    window = DrawingWindow(700, 700, 0,100, 0, 100, 'test')
    TreeNode.window = window
    RRT.window = window
    nLinkRobot(window)
    window.tk.mainloop()



