import pygame

AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/Game On.png'

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Galactic Battle")
background = pygame.image.load(BACKGROUND_IMAGE).convert()

# CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
seccio_transparent = pygame.Surface((240,120),pygame.SRCALPHA)
pygame.draw.rect(seccio_transparent,(200,0,200,100),(0,0,240,120))

#FONT I TEXT de tamany 64
font = pygame.font.SysFont(None,32)
img = font.render("1.- Crèdits", True, (255,255,255))
img2 = font.render("2.- Jugar", True, (255,255,255))
img3= font.render("3.- Sortir", True, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Imprimeixo imatge de fons:
    pantalla.blit(background, (0,0))
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    pantalla.blit(seccio_transparent, (40, 40))
    # dibuixem el text
    pantalla.blit(img, (50, 50))
    pantalla.blit(img2, (50, 80))
    pantalla.blit(img3, (50, 110))

    pygame.display.update()
