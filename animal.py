'''
Created on Aug 8, 2019

@author: Ethan
'''
import random

import world_map

class Animal:
    def __init__(self, age=0, hunger=0, thirst=0, fieldOfView=10, world=world_map.WorldMap()):
        self.age = age
        self.hunger = hunger
        self.thirst = thirst
        self.world = world
        self.fieldOfView = fieldOfView
        
        self.world.addObject(self, (random.randrange(0, self.world.size[0]), random.randrange(0, self.world.size[1])))
        
    def navigateTo(self, destination):
        pass
        
class MaleAnimal(Animal):
    def findNearestFemale(self):
        return self.world.findNearbyObject(self, FemaleAnimal, self.fieldOfView)
    
class FemaleAnimal(Animal):
    def findNearestMale(self):
        return self.world.findNearbyObject(self, MaleAnimal, self.fieldOfView)
    
if __name__ == "__main__":
    earth = world_map.WorldMap(size=(200, 200))
    
    a = MaleAnimal(world=earth)
    b = FemaleAnimal(world=earth)
    
    earth.render()