'''
Created on Aug 8, 2019

@author: Ethan
'''
class WorldMap:
    def __init__(self, animals={}):
        self.animals = animals
        
    def addAnimal(self, animal, loc=(0, 0)):
        self.animals[animal] = loc
    
    def findNearbyObject(self, origin, objectType):
        pass