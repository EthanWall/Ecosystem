'''
Created on Aug 8, 2019

@author: Ethan
'''
import WorldMap

class Animal:
    def __init__(self, age=0, hunger=0, thirst=0, world=WorldMap.WorldMap()):
        self.age = age
        self.hunger = hunger
        self.thirst = thirst
        self.world = world
        
        self.world.addAnimal(animal=self)
        print(self.world.animals)
        
class MaleAnimal(Animal):
    def findNearestFemale(self):
        pass
    
class FemaleAnimal(Animal):
    def findNearestMale(self):
        pass
    
if __name__ == "__main__":
    earth = WorldMap.WorldMap()
    
    MaleAnimal(world=earth)
    FemaleAnimal(world=earth)
    Animal(world=earth)