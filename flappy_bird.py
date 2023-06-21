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


