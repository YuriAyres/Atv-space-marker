import pygame
from tkinter import simpledialog
pygame.init()
pygame.display.set_caption("Space Marker")
tamanho = (1000,563)
tela = pygame.display.set_mode(tamanho)
branco = (255,255,255)
preto = (0,0,0)
clock = pygame.time.Clock()
running = True
fundo = pygame.image.load("bg.jpg")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
estrelas = {}
white = (255, 255, 255)

pygame.display.set_caption('Show Text')
 

 
while running:
    tela.blit(fundo,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da Estrela:")
            if item == None:
                item = "desconhecido"+str(pos)
            estrelas[item]= pos
            pygame.surface.Surface
        for key, value in estrelas.items():
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render(key, True, white)
            textRect = text.get_rect()
            tela.blit(text, textRect)
        
       
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()