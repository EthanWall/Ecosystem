'''
Created on Aug 8, 2019

@author: Ethan
'''
import random

from object import Object

class Animal():
    def __init__(self, world, age=0, hunger=0, thirst=0, fieldOfView=10, object=Object()):
        self.age = age
        self.hunger = hunger
        self.thirst = thirst
        self.world = world
        self.fieldOfView = fieldOfView
        self.object = object
        
        self.world.addObject(self, (random.randrange(0, self.world.size[0]), random.randrange(0, self.world.size[1])))
        
    def navigateTo(self, destination):
        pass
        
class MaleAnimal(Animal):
    def findNearestFemale(self):
        return self.world.findNearbyObject(self, FemaleAnimal, self.fieldOfView)
    
class FemaleAnimal(Animal):
    def findNearestMale(self):
        return self.world.findNearbyObject(self, MaleAnimal, self.fieldOfView)