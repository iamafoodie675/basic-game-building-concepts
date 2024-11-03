import pygame 
pygame.init()
window =pygame.display.set_mode((400,400))
window.fill((255,255,255))
PINK=(253, 193, 252)
pygame.draw.circle(window,PINK,(300,300),50)
pygame.draw.circle(window,PINK,(100,100),50, 3)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
            
pygame.quit()
