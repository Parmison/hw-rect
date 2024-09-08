import pygame
pygame.init()

screen = pygame.display.set_mode((1250,690))

class Rect:
    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
    def grow(self):
        self.w += 5
        self.h += 5
        self.draw()
R1 = Rect(600,345,400,200,"white")
screen.fill("black")
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            R1.draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            R1.grow()
            pygame.display.update() 
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            R2 = Rect(pos[0],pos[1],10,10,"white")
            R2.draw()
            pygame.display.update()