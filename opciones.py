import pygame
from constantes import *

pygame.init()
#fondo
imagen_opciones = pygame.image.load("imagenes/fondo-opciones.png")#Se carga la imagen de fondo
imagen_opciones = pygame.transform.scale(imagen_opciones, (500,500))#Se escala la imagen de fondo
volumen_musica = 100
volumen_sonidos = 100
marco_actual_musica = "mariano"
marco_actual_sonidos = "mariano"
#imagenes
musica_activada = pygame.image.load("imagenes/sonido.png")
musica_desactivada = pygame.image.load("imagenes/Muteado.png")
flecha = pygame.image.load("imagenes/flecha.png")
flecha_subida = pygame.image.load("imagenes/flecha_subida.png")

#marco objetivo
marco_salir = flecha.get_rect(topleft=(10,10))
marco_musica = musica_activada.get_rect(topleft=(225,150))
marco_sonidos = musica_activada.get_rect(topleft=(225,350))
sonido_flecha_subida = flecha_subida.get_rect(topleft=(150,150))
sonido_flecha_bajada = flecha.get_rect(topleft=(300,150))
musica_flecha_subida = flecha_subida.get_rect(topleft=(150,350))
musica_flecha_bajada = flecha.get_rect(topleft=(300,350))
def mostrar_opciones(pantalla:pygame.Surface,eventos):
    global volumen_musica
    global volumen_sonidos
    global marco_actual_musica
    global marco_actual_sonidos
    retorno = "opciones"#Un estado de la ventana en la que estoy parado
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            if marco_salir.collidepoint(evento.pos):
                print("saliendo")
                retorno = "menu"
            elif marco_musica.collidepoint(evento.pos):
                volumen_musica = 0
                MUSICA_MENU.stop()
                if marco_actual_musica == "mute":
                    marco_actual_musica = "mariano"
                else:
                    marco_actual_musica = "mute"
            elif marco_sonidos.collidepoint(evento.pos):
                volumen_sonidos = 0
                MUSICA_MENU.stop()
                if marco_actual_sonidos == "mute":
                    MUSICA_MENU.play()
                    marco_actual_sonidos = "mariano"
                else:
                    marco_actual_sonidos = "mute"
            elif musica_flecha_subida.collidepoint(evento.pos):
                print("SUBE")
                if volumen_musica < 96:
                    volumen_musica += 5
            elif musica_flecha_bajada.collidepoint(evento.pos):
                print("BAJA")
                if volumen_musica > 0:
                    volumen_musica -= 5
            elif sonido_flecha_subida.collidepoint(evento.pos):
                print("SUBE")
                if volumen_sonidos < 96:
                    volumen_sonidos += 5
            elif sonido_flecha_bajada.collidepoint(evento.pos):
                print("BAJA")
                if volumen_sonidos > 0:
                    volumen_musica -= 0

    pantalla.blit(imagen_opciones,(0,0))
    if marco_actual_musica == "mute":
        pantalla.blit(musica_desactivada,marco_musica.topleft)
    else:
        pantalla.blit(musica_activada,marco_musica.topleft)
    if marco_actual_sonidos == "mute":
        pantalla.blit(musica_desactivada,marco_sonidos.topleft)
    else:
        pantalla.blit(musica_activada,marco_sonidos.topleft)
    
    pantalla.blit(flecha_subida,musica_flecha_bajada.topleft)
    pantalla.blit(flecha,musica_flecha_subida.topleft)
    pantalla.blit(flecha_subida,sonido_flecha_bajada.topleft)
    pantalla.blit(flecha,sonido_flecha_subida.topleft)

    return retorno
    