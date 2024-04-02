import time
from pygame.locals import *
import pygame

AMPLADA = 320
ALTURA = 200
LOGO_IMAGE = "assets/Enemic2.png"
BACKGROUND_IMAGE = 'assets/FondoJuego.png'
player_image = pygame.image.load('assets/NauJoc.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 2
#MUSICA_FONS = 'assets/music.mp3'

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Galactic Battle")
logo = pygame.image.load(LOGO_IMAGE)
pygame.display.set_icon(logo)

# Control de FPS
clock = pygame.time.Clock()
fps = 60

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Moviment del jugador
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect.x -= velocitat_nau
    if keys[K_d]:
        player_rect.x += velocitat_nau

    # Mantenir al jugador dins de la pantalla
    player_rect.clamp_ip(pantalla.get_rect())
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    pantalla.blit(player_image, player_rect)
    pygame.display.update()
    clock.tick(fps)
