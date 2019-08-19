'''
Created on Aug 9, 2019

@author: Ethan
'''
import threading
import time

import pygame

from animal import Animal, FemaleAnimal, MaleAnimal
from world_map import WorldMap
from pathfinding import Path
from render import render
from object import Object

running = True

def test(creature, world):
    path = Path(world.getObjectPosition(creature), (100, 100), world)
    path.calculate()
    path.run(creature)

if __name__ == "__main__":
    pygame.init()
    
    clock = pygame.time.Clock()
    
    earth = WorldMap(size=(1000, 1000))
    
    a = Animal(world=earth, object=Object(size=(10, 10), location=(50, 50)))
    
    t = threading.Thread(target=test, args=(a,earth,))
    t.start()
    
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            print(event)
        
        #Render the screen
        render(earth.screen, earth.objects)
        clock.tick(60)
        
    pygame.quit()
    quit()