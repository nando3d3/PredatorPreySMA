from src import *
from src.model import PredatorPreyModel
from src.config import SCREEN
pygame.init()

pygame.display.set_caption("Predator-Prey")

clock = pygame.time.Clock()

creatures = PredatorPreyModel(5, 10, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    SCREEN.fill(BLACK)
    
    creatures.step()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()