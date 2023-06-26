import pygame
import pickle
from tkinter import simpledialog
from tkinter import messagebox
from funcoes import analisar_tupla
from funcoes import sutrair_tupla
from funcoes import medias_tuplas
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
medias = []
dist_marcs = []
marc = {}
chaves_percorridas = []
nome_arquivo = "estrelas.pkl"
start_pos = None
white = (255, 255, 255)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
tela.blit(fundo,(0,0))
font = pygame.font.Font(None, 20)     
font2 = pygame.font.Font(None, 25)
text2 = font2.render("Pressione F10 para Salvar os Pontos", True, white)
text3 = font2.render("Pressione F11 para Carregar os Pontos", True, white)
text4 = font2.render("Pressione F12 para Deletar os Pontos", True, white)
tela.blit(text2,(10,10))
tela.blit(text3,(10,30))
tela.blit(text4,(10,50))
reiniciar_da_tela = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if start_pos is None:
                start_pos = pos
            else:
                end_pos = pos
                pygame.draw.line(tela, white, start_pos, end_pos , 1)
                start_pos = pos                      
            item = simpledialog.askstring("Space","Nome da Estrela:")
            if item == "":
                item = "desconhecido"+str(pos)
            estrelas[item]= pos
            for key, value in estrelas.items():
                text = font.render(item, True, white)
                pygame.draw.circle(tela, white, pos, 3.5)
                limite = analisar_tupla(pos,852,550)
                if key not in chaves_percorridas:
                    chaves_percorridas.append(key)
                    if limite == False:
                        tela.blit(text, (pos))
                    else:
                        pos2 = sutrair_tupla(pos)
                        tela.blit(text, (pos2))
                medias_tuplas(estrelas,medias,dist_marcs)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
             with open(nome_arquivo, 'wb') as arquivo:
                pickle.dump(estrelas, arquivo)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                with open(nome_arquivo, 'rb') as arquivo:
                    estrelas = pickle.load(arquivo)
                    for key, value in estrelas.items():
                        text = font.render(key, True, white)
                        pygame.draw.circle(tela, white, value, 3.5)
                        limite = analisar_tupla(value,852,550)
                        if key not in chaves_percorridas:
                            chaves_percorridas.append(key)
                            if limite == False:
                                tela.blit(text, (value))
                            else:
                                pos2 = sutrair_tupla(value)
                                tela.blit(text, (pos2))
                        if start_pos is None:
                            start_pos = value
                        else:
                            end_pos = value
                            pygame.draw.line(tela, white, start_pos, end_pos , 1)
                            start_pos = value
                    medias_tuplas(estrelas,medias,dist_marcs)
            except:
                messagebox.showinfo("Erro", "Não existem marcações salvas!")               
               
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
             with open(nome_arquivo, 'w') as arquivo:
                pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11 or event.type == pygame.MOUSEBUTTONUP:
            for dist in dist_marcs:
                marc[dist] = None
            for media in medias:
                marc[dist] = media
            chaves = marc.keys()
            for i, valor in enumerate(medias):
                if i < len(chaves):
                    chave = list(chaves)[i]
                marc[chave] = valor
            for key, value in marc.items():
                if key not in chaves_percorridas:
                    chaves_percorridas.append(key)
                    text = font.render(key, True, white)
                    tela.blit(text, (value))

        

       
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()