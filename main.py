import pygame
from tkinter import simpledialog
from funcoes import analisar_tupla
from funcoes import sutrair_tupla
pygame.init()
tamanho = (1000,563)
tela = pygame.display.set_mode(tamanho)
branco = (255,255,255)
preto = (0,0,0)
pygame.display.set_caption("Space Marker")
clock = pygame.time.Clock()
running = True
fundo = pygame.image.load("bg.jpg")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
estrelas = {}
lista_pos = []
white = (255, 255, 255)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
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
            for key, value in estrelas.items():
                font = pygame.font.Font(None, 20)
                text = font.render(item, True, white)
                pygame.draw.circle(tela, white, pos, 3.5)
                limite = analisar_tupla(pos,852,550)
                if limite == False:
                    tela.blit(text, (pos))
                else:
                    pos2 = sutrair_tupla(pos)
                    tela.blit(text, (pos2))
                    


       
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()