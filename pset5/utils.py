import math

class Stack():

    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        return False


class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        return self.queue.pop()

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        return False

class PriorityQueue:

    def  __init__(self):
        self.queue = []
        self.priority = []

    def push(self, item):
        self.queue.append(item)
        self.priority.append(item.priority)

    def pop(self):
        mini = self.findMin(self.priority)
        item = self.queue.pop(mini)
        self.priority.pop(mini)
        return item

    def findMin(self,l):
        current = []
        index = None
        for i in xrange(len(l)):
            if l[i] < current:
                current = l[i]
                index = i
        return index
          

    def isEmpty(self):
        return len(self.queue) == 0

class PriorityQueueWithFunction(PriorityQueue):

    def  __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        PriorityQueue.__init__(self)     

    def push(self, item):
        item.priority =  self.priorityFunction(item)
        PriorityQueue.push(self, item)


