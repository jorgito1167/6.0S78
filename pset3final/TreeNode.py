
class TreeNode():
    
    window = None

    def __init__(self, state, parent):
        self.parent = parent
        self.children = []
        self.state = state

    def addChild(self, child):
        self.children.append(child)

    def draw(self):
        s = self.state
        self.window.drawOval((s[0]-0.5,s[1]+0.5),(s[0]+0.5,s[1]-0.5))
        for c in self.children:
            self.window.drawLineSeg(s[0],s[1],c.state[0],c.state[1]) 

    def __str__(self):
        s = ""
        if self.parent != None:
            s+= "Parent: "  + str(self.parent.state)

        s+= " State: " + str(self.state) + "\n"

        for c in self.children:
            s+= "Child: " + str(c.state) + "\n"
        
        return s


