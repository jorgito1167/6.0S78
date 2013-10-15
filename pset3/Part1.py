from DrawingWindowStandalone import *
import copy
import math
from geometry import *
from CollisionBox import *
from TreeNode import *
from RRT import *

if __name__ == "__main__":
    window = DrawingWindow(700, 700, 0,100, 0, 100, 'test')
    TreeNode.window = window
    RRT.window = window

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
    vertices1 = ([0,0], [0,15], [30,7])
    poly1 = Polygon(window, vertices1)
    poly1.move(Point(10, 20))
    obstacles.append(poly1)

    vertices2 = ((0,0), (0,10),(30,10), (30,0))
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
    rrt = RRT((3,3,0),(85,85,0),collision_box, dimensions,euclideanDistance, 10, 100) 
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



    window.tk.mainloop()



