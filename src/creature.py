from mesa import Agent
import random
from .config import *
import pygame
import math

class Creature(Agent):
    def __init__(self, uid, model, color, size, food = ()):
        super().__init__(uid, model)
        self.size = size
        self.color = color
        self.food = food
        x, y = None, None
        self.uid = uid
        
        # desenha agente
        self.surf = pygame.Surface((2*self.size, 2*self.size), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.surf, self.color, (self.size, self.size), self.size)
        self.rect = self.surf.get_rect()
        
        self.vmax = 2.0
        
        # posicao inicial
        self.x = x if x else random.randint(1, SCREEN_WIDTH-1)
        self.y = y if y else random.randint(1, SCREEN_HEIGHT-1)
        
        # velocidade inicial
        self.dx = 0
        self.dy = 0
        
        # valor inicial
        self.is_alive = True
        self.target = None
        self.age = 0
        self.energy = 0
        
        # movimentar agente
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
        global SCREEN
        SCREEN.blit(self.surf, self.rect)
    
    def step(self):
        
        global SCREEN
        #screen = SCREEN
        self.age += 1
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
        SCREEN.blit(self.surf, self.rect)
        
        self.updateDelta()
        
        # att posicao baseado em delta x e y
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        self.x = max(self.x, 0)
        self.x = min(self.x, SCREEN_WIDTH)
        self.y = max(self.y, 0)
        self.y = min(self.y, SCREEN_HEIGHT)

        self.updateTarget(self.food)
        
    def updateDelta(self):
        #fx = random.randint(-3, 3)
        #fy = random.randint(-3, 3)
        fx, fy = 0, 0

        
        if self.target:
            fx += 0.1 * (self.target.x - self.x)
            fy += 0.1 * (self.target.y - self.y)
        
        
        # atualiza direcao usando a forca aplicada
        self.dx = self.dx + 0.05 * fx
        self.dy = self.dy + 0.05 * fy
        
        # limita a velocidade do agente
        vel = math.sqrt(self.dx ** 2 + self.dy ** 2)
        if vel > self.vmax:
            self.dx = (self.dx / vel) * self.vmax
            self.dy = (self.dy / vel) * self.vmax
            
        # se move na direcao do target
        if self.target:
            fx += 0.1*(self.target.x - self.x)
            fy += 0.1*(self.target.y - self.y)

    def updateTarget(self, food):
        # target morreu
        if self.target and not self.target.is_alive:
            self.target = None

        # come o target se estiver proximo
        if self.target:
            dist = (self.x - self.target.x)**2 + (self.y - self.target.y)**2
            if dist < 400:
                self.target.is_alive = False
                self.energy = self.energy + 1

        # procura target        
        if not self.target: 
            min_dist = 9999999
            min_agent = None
            for a in food:
                if a is not self and a.is_alive:
                    dist_food = (self.x - a.x) ** 2 +  (self.y - a.y) ** 2
                    if dist_food < min_dist:
                        min_dist = dist_food
                        min_agent = a
            
            if min_dist < 100000:
                self.target = min_agent