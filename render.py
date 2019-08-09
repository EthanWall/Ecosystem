'''
Created on Aug 9, 2019

@author: Ethan
'''
import sys
import os

def clear():
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        command = "clear"
    elif sys.platform == "win32":
        command = "cls"
    else:
        return
    os.system(command)

def render(size, objects={}):
    clear()
    
    objects = {v: k for k, v in objects.items()} #Flip the objects dictionary
    for x in range(size[0]):
        line = ""
        for y in range(size[1]):
            for _ in objects:
                if (x, y) in objects:
                    line += "/"
                else:
                    line += "*"
        print(line)