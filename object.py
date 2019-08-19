'''
Created on Aug 13, 2019

@author: Ethan
'''
import pygame

class Object:
    def __init__(self, size=(1, 1), location=(0, 0), color=(0, 0, 0)):
        self.size = size
        self.location = location
        self.color = color
        self.rect = pygame.Rect(self.location, self.size)