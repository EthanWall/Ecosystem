'''
Created on Aug 9, 2019

@author: Ethan
'''
import time

class Path:
    def __init__(self, start, end, world):
        self.start = start
        self.end = end
        self.world = world
        self.calculated = False
        
    def calculate(self):
        #Calculate distance from target
        startX = round(self.start[0])
        startY = round(self.start[1])
        endX = round(self.end[0])
        endY = round(self.end[1])
        distance = abs((startX + startY) - (endX + endY))
        
        #Make a list to store all path nodes
        self.nodes = []
        
        currentX = startX
        currentY = startY
        
        while distance > 0:
            if currentX != endX:
                if endX > startX:
                    #Go forwards
                    currentX += 1
                else:
                    #Go backwards
                    currentX -= 1
                distance -= 1
            if currentY != endY:
                if endY > startY:
                    #Go forwards
                    currentY += 1
                else:
                    #Go backwards
                    currentY -= 1
                distance -= 1
            
            newNode = (currentX, currentY)
            self.nodes.append(newNode)
            print(self.nodes)
            
        self.calculated = True
        
    def run(self, obj):
        if self.calculated:
            while len(self.nodes) > 0:
                time.sleep(0.1)
                self.world.setObjectPosition(obj, self.nodes[0])
                del self.nodes[0]
        else:
            print("Path has not been calculated yet")