import pygame, sys,os
from pygame.locals import * 

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Monkey Fever') 
screen = pygame.display.get_surface() 
monkey_head_file_name = os.path.join("data","chimp.bmp")
print monkey_head_file_name