import time

import pygame

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/GameOn.png'
LOGO_IMAGE = "assets/Enemic2.png"

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Galactic Battle")
logo = pygame.image.load(LOGO_IMAGE)
pygame.display.set_icon(logo)

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
def animacio_inici():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    pygame.display.update()
    # time.sleep(3)
    # FONT I TEXT de tamany 64
    font = pygame.font.SysFont(None, 35)
    for i in range(120):
        time.sleep(0.01)
        imprimir_pantalla_fons(BACKGROUND_IMAGE)
        img = font.render("Enjoy!", True, (255, 255, 255))
        pantalla.blit(img, (20, 200-i))
        pygame.display.update()
    time.sleep(1)


def imprimir_menu():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    # CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
    seccio_transparent = pygame.Surface((240, 120), pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent, (0, 0, 0, 100), (0, 0, 240, 120))
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    pantalla.blit(seccio_transparent, (40, 40))
    # FONT I TEXT de tamany 64
    font = pygame.font.SysFont(None, 36)
    img = font.render("1.- Crèdits", True, (255, 255, 255))
    img2 = font.render("2.- Jugar", True, (255, 255, 255))
    img3 = font.render("3.- Sortir", True, (255, 255, 255))
    # dibuixem el text
    pantalla.blit(img, (70, 50))
    pantalla.blit(img2, (70, 90))
    pantalla.blit(img3, (70, 130))
    pygame.display.update()



def musica_fons(musica):
    ambient_music = pygame.mixer.Sound(musica)
    music_chanel = pygame.mixer.Channel(0)
    ambient_music.play()
    while True:
        ambient_music.set_volume(0.3)
        time.sleep(0)
        break

musica_fons('assets/MusicaArcade.mp3')
animacio_inici()
imprimir_menu()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
