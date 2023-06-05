import pygame
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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        tela.blit(fundo,(0,0))
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()