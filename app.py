import pygame
import neat
import time
import os
import random

win_width=800
win_height=600

bird_imgs=[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),
          pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),
          pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))
          ]

pipe_img=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
base_img=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
bg_img=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

class Bird:
    imgs=bird_imgs
    max_rotation=25
    rot_vel=20
    animation_time=5

    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        self.titl=0
        self.tick_count=0
        self.vel=0
        self.height=self.y
        self.img_count=0