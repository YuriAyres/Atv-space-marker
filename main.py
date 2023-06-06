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
 

tela.blit(fundo,(0,0))     
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da Estrela:")
            if item == "":
                item = "desconhecido"+str(pos)
            estrelas[item]= pos
            print(item)
            for key, value in estrelas.items():
                font = pygame.font.Font(None, 20)
                text = font.render(item, True, white)
                tela.blit(text, (pos))
                pygame.draw.circle(tela, white, pos, 3.5)


       
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()