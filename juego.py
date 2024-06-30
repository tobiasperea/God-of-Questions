import pygame
from opciones import *
from constantes import *
import json
import os


imagen_juego = pygame.image.load("imagenes/zeus.png")#Se carga la imagen de fondo
marco_pregunta = pygame.image.load("imagenes/cuadrado_prueba.png")

marco_pregunta_1 = marco_pregunta.get_rect(topleft=(40, 250))
marco_pregunta_4 = marco_pregunta.get_rect(topleft=(250, 350))
marco_pregunta_3 = marco_pregunta.get_rect(topleft=(40, 350))
marco_pregunta_2 = marco_pregunta.get_rect(topleft=(250, 250))

click_sonido = pygame.mixer.Sound("musicaysonidos/Taco Bell Bong - Sound Effect (HD).mp3")
click_sonido.set_volume(volumen_sonidos)

def mostrar_juego(pantalla:pygame.Surface,eventos):
    retorno = "juego"#Un estado de la ventana en la que estoy parado
    click_sonido.set_volume(volumen_sonidos)
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if marco_pregunta_1.collidepoint(evento.pos):
                print("Respuesta 1")
            elif marco_pregunta_2.collidepoint(evento.pos):
                print("respuesta 2")
            elif marco_pregunta_3.collidepoint(evento.pos):
                print("Respuesta 3")
            elif marco_pregunta_4.collidepoint(evento.pos):
                print("respues 4")
        elif evento.type == pygame.QUIT:
            retorno = "salir" #El estado salir -> Cuando se le da a la X

    pantalla.blit(imagen_juego,(0,0))# se carga el fondo
    pantalla.blit(marco_pregunta, marco_pregunta_1.topleft) #--se cargan los rectangulos
    pantalla.blit(marco_pregunta, marco_pregunta_2.topleft)
    pantalla.blit(marco_pregunta, marco_pregunta_3.topleft)
    pantalla.blit(marco_pregunta, marco_pregunta_4.topleft)

    return retorno