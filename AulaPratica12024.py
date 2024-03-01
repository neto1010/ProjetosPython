import pygame
from pygame import Surface
from pygame.locals import Rect

W_WIDTH = 576
W_HEIGHT = 324

# Inicializar o módulo PyGame
pygame.init()
print('setup start')
# Criação de janela do pygame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superfície. Primeiro desenha o fundo e depois a nave para o fundo não sobrepor a nave, caso seja feito o contrário
bg_surf = pygame.image.load('./asset/bg.png').convert_alpha() #convert alpha serve para otimizar a renderização da imagem
player1_surf = pygame.image.load('./asset/player1.png').convert_alpha() #convert alpha serve para otimizar a renderização da imagem

# Obter o retângulo a partir da superfície
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1_surf.get_rect(left=100, top=100)


# Desenhar na janela (window)
window.blit(source=bg_surf, dest=(bg_rect))
window.blit(source=player1_surf, dest=(player1_rect))

# Atualizar a janela
pygame.display.flip()



# Colocar um relógio no nosso jogo
clock = pygame.time.Clock()

# Carregar música e deixar ela tocando
pygame.mixer_music.load('./asset/song.wav')
pygame.mixer_music.play(-1)
# pygame.mixer_music.set_volume(0.3) # Controla o volume da música. Vai de 0 a 1
print('setup end')
print('loop start')
while True:
    clock.tick(140) # Esse loop está acontecendo 30 vezes por segundo
    print(f'{clock.get_fps() :.0f}') # Executar o print do fps
    window.blit(source=bg_surf, dest=(bg_rect))  # Atualiza o fundo
    window.blit(source=player1_surf, dest=(player1_rect))  # Atualiza a nave
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('loop end')
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player1_rect.centery -= 1 # Faz o retângulo (nave) subir
    if pressed_key[pygame.K_s]:
        player1_rect.centery += 1  # Faz o retângulo (nave) subir
    if pressed_key[pygame.K_d]:
        player1_rect.centerx += 1  # Faz o retângulo (nave) subir
    if pressed_key[pygame.K_a]:
        player1_rect.centerx -= 1  # Faz o retângulo (nave) subir
        pass

#
