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
        self.tilt=0
        self.tick_count=0
        self.vel=0
        self.height=self.y
        self.img_count=0
        self.img=self.imgs[0]

    def jump(self):
        self.vel=-10.5
        self.tick_count=0
        self.height=self.y

    def move(self):
        self.tick_count+=1
        d=self.vel*self.tick_count+1.5*self.tick_count**2
        if d>=16:
            d=16
        if d<0:
            d-=2
        
        self.y=self.y+d
        if d<0 or self.y <self.height+50:
            if self.tilt < self.max_rotation:
                self.tilt=self.max_rotation
        else:
            if self.tilt> -90:
                self.tilt-=self.rot_vel   
    
    def drow(self,win):
        self.img_count+=1

        if self.img_count < self.animation_time:
            self.img = self.imgs[0]
        elif self.img_count < self.animation_time*2:
            self.img = self.imgs[1]
        elif self.img_count < self.animation_time*3:
            self.img = self.imgs[2]
        elif self.img_count < self.animation_time*4:
            self.img = self.imgs[1]
        elif self.img_count < self.animation_time*4+1:
            self.img = self.imgs[0]
            self.img_count=0

        if self.tilt<=-80:
            self.img=self.imgs[1]
            self.img_count=self.animation_time*2

        #will rotate the image about the center
        rotated_image = pygame.transform.rotate(self.img,self.tilt)
        new_rect=rotated_image.get_rect(center=self.get_rect(topLeft=(self.x,self.y)).center)
        win.blit(rotated_image,new_rect.topleft)

    def get_mask(selft):
        return pygame.mask.from_surface(self.img)