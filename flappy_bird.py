import pygame
import neat
import time
import os
import random

WIN_HEIGHT = 800
WIN_WIDTH = 600

BIRD_IMAGES = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png")))],
	      	  [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png")))],
			  [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))]
			  
PIPE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "pipe.png")))]
BASE_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))]
BACKGROUND_IMAGE = [pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))]

class Bird:
	IMAGES = BIRD_IMAGES
	MAX_ROTATION = 25
	ROTATION_VELOCITY = 20
	ANIMATION_TIME = 5
	
	def __init(self, x, y):
		self.x = x
		self.y = y
		self.tilt = 0
		self.tick_count = 0
		self.velocity = 0
		self.height = self.y
		self.image_count = 0
		self.image = self.IMAGES[0]
		
	def jump(self):
		self.velocity = -10.5
