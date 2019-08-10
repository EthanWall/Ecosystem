'''
Created on Aug 9, 2019

@author: Ethan
'''
import threading
import time

import animal
import world_map
import pathfinding

def live(creature):
    while True:
        pass
    
def test(creature, world):
    path = pathfinding.Path(world.getObjectPosition(creature), (100, 100), world)
    path.calculate()
    path.run(creature)

def main():
    earth = world_map.WorldMap(size=(200, 200))
    
    a = animal.Animal(world=earth)
    
    t = threading.Thread(target=test, args=(a,earth,))
    t.start()
    
    while True:
        time.sleep(0.1)
        earth.render()

if __name__ == "__main__":
    main()