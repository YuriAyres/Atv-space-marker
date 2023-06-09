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
start_pos = None
white = (255, 255, 255)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
tela.blit(fundo,(0,0))     
font2 = pygame.font.Font(None, 25)
text2 = font2.render("Pressione F10 para Salvar os Pontos", True, white)
text3 = font2.render("Pressione F11 para Carregar os Pontos", True, white)
text4 = font2.render("Pressione F12 para Deletar os Pontos", True, white)
tela.blit(text2,(10,10))
tela.blit(text3,(10,30))
tela.blit(text4,(10,50))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if start_pos is None:
                        start_pos = pos
            else:
                end_pos = pos
                pygame.draw.line(tela, white, start_pos, end_pos , 2)
                start_pos = pos                      
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