'''
Created on Aug 8, 2019

@author: Ethan
'''
import render

class WorldMap:
    def __init__(self, size=(100, 100), objects={}):
        self.objects = objects
        self.size = size
        
    def addObject(self, obj, location=(0, 0)):
        self.objects[obj] = location
        
    def render(self):
        render.render(self.size, self.objects)
    
    def setObjectPosition(self, obj, location, relative=False):
        if relative:
            self.objects[obj][0] += location[0] #X
            self.objects[obj][1] += location[1] #Y
        else:
            self.objects[obj] = location
    
    def getObjectPosition(self, obj):
        if obj in self.objects:
            return self.objects[obj]
        return None
    
    def findNearbyObject(self, origin, objectType, radius=10):
        closestObject = None
        for i in self.objects:
            if i != origin:
                distance = (self.objects[i][0] + self.objects[i][1]) - (self.objects[origin][0] + self.objects[origin][1])
                if type(i) == objectType and distance <= radius:
                    if closestObject == None:
                        closestObject = (i, distance)
                    else:
                        if distance < closestObject[1]:
                            closestObject = (i, distance)
        return closestObject[0]