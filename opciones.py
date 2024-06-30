import pygame
from constantes import *

pygame.init()
#fondo
imagen_opciones = pygame.image.load("imagenes/fondo-opciones.png")#Se carga la imagen de fondo
imagen_opciones = pygame.transform.scale(imagen_opciones, (500,500))#Se escala la imagen de fondo
volumen_musica = 1
volumen_sonidos = 1
marco_actual_musica = "mariano"
marco_actual_sonidos = "mariano"
#imagenes
musica_activada = pygame.image.load("imagenes/sonido.png")
musica_desactivada = pygame.image.load("imagenes/Muteado.png")
flecha = pygame.image.load("imagenes/flecha.png")
flecha_subida = pygame.image.load("imagenes/flecha_subida.png")
cartel_musica = pygame.image.load("imagenes/musica_cartel.png")
cartel_sonidos = pygame.image.load("imagenes/sonidos_cartel.png")
flecha_salida = pygame.image.load("imagenes/flecha_salida.png")

#marco objetivo
marco_salir = flecha_salida.get_rect(topleft=(10,10))
marco_musica = musica_activada.get_rect(topleft=(225,180))
marco_sonidos = musica_activada.get_rect(topleft=(225,380))
sonido_flecha_bajada = flecha.get_rect(topleft=(130,390))
sonido_flecha_subida = flecha_subida.get_rect(topleft=(325,390))
musica_flecha_bajada = flecha.get_rect(topleft=(130,190))
musica_flecha_subida = flecha_subida.get_rect(topleft=(325,190))

click_sonido = pygame.mixer.Sound("musicaysonidos/Taco Bell Bong - Sound Effect (HD).mp3")
click_sonido.set_volume(volumen_sonidos)
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
                MUSICA_MENU.stop()
                if marco_actual_musica == "mute":
                    MUSICA_MENU.play(-1)
                    marco_actual_musica = "mariano"
                else:
                    marco_actual_musica = "mute"
            elif marco_sonidos.collidepoint(evento.pos):
                volumen_sonidos = (0)  
                if marco_actual_sonidos == "mute":
                    marco_actual_sonidos = "mariano"
                else:
                    marco_actual_sonidos = "mute"
            elif musica_flecha_subida.collidepoint(evento.pos):
                print("SUBE musica")
                if volumen_musica < 0.96:
                    volumen_musica += 0.1
                    MUSICA_MENU.set_volume(volumen_musica)
            elif musica_flecha_bajada.collidepoint(evento.pos):
                print("BAJA musica")
                if volumen_musica > 0:
                    volumen_musica -= 0.1
                    MUSICA_MENU.set_volume(volumen_musica)
            elif sonido_flecha_subida.collidepoint(evento.pos):
                print("SUBE sonido ")
                click_sonido.play()
                if volumen_sonidos < 0.96:
                    volumen_sonidos += 0.1
                    click_sonido.set_volume(volumen_sonidos)
            elif sonido_flecha_bajada.collidepoint(evento.pos):
                print("BAJA sonido")
                click_sonido.play()
                if volumen_sonidos > 0:
                    volumen_sonidos -= 0.1
                    click_sonido.set_volume(volumen_sonidos)
                   

    pantalla.blit(imagen_opciones,(0,0))
    pantalla.blit(cartel_sonidos,(125,130))
    pantalla.blit(cartel_musica,(125,0))

    if marco_actual_musica == "mute":
        pantalla.blit(musica_desactivada,marco_musica.topleft)
    else:
        pantalla.blit(musica_activada,marco_musica.topleft)
    if marco_actual_sonidos == "mute":
        pantalla.blit(musica_desactivada,marco_sonidos.topleft)
    else:
        pantalla.blit(musica_activada,marco_sonidos.topleft)
    
    pantalla.blit(flecha,musica_flecha_bajada.topleft)
    pantalla.blit(flecha_subida,musica_flecha_subida.topleft)
    pantalla.blit(flecha,sonido_flecha_bajada.topleft)
    pantalla.blit(flecha_subida,sonido_flecha_subida.topleft)
    pantalla.blit(flecha_salida,marco_salir.topleft)

    return retorno
    