import pygame
from opciones import *
from constantes import *
from funciones import *
import random
import json
import os
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

pygame.init()
carta_pregunta = {"superficie":pygame.Surface((250,150)),"rectangulo":pygame.Rect((0,0,0,0))}

imagen_juego = pygame.image.load("imagenes/zeus.png")#Se carga la imagen de fondo
marco_pregunta = pygame.image.load("imagenes/cuadrado_prueba.png")

marco_pregunta_1 = marco_pregunta.get_rect(topleft=(40, 250))
marco_pregunta_4 = marco_pregunta.get_rect(topleft=(250, 350))
marco_pregunta_3 = marco_pregunta.get_rect(topleft=(40, 350))
marco_pregunta_2 = marco_pregunta.get_rect(topleft=(250, 250))

cartas_respuestas = [
    {"superficie":pygame.Surface((100,60)),"rectangulo":pygame.Rect((0,0,0,0))},#R1 -> 0
    {"superficie":pygame.Surface((100,60)),"rectangulo":pygame.Rect((0,0,0,0))},#R2 -> 1
    {"superficie":pygame.Surface((100,60)),"rectangulo":pygame.Rect((0,0,0,0))},#R3 -> 2
    {"superficie":pygame.Surface((100,60)),"rectangulo":pygame.Rect((0,0,0,0))} #R4 -> 3
]
fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow",20)

click_sonido = pygame.mixer.Sound("musicaysonidos/Taco Bell Bong - Sound Effect (HD).mp3")
click_sonido.set_volume(volumen_sonidos)
random.shuffle(lista_preguntas)
indice_pregunta = 0

def mostrar_juego(pantalla:pygame.Surface,eventos):
    global indice_pregunta
    
    retorno = "juego"#Un estado de la ventana en la que estoy parado

    pregunta = lista_preguntas[indice_pregunta]
    

    
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

    pantalla.blit(carta_pregunta['superficie'],(80,50))
    #Muestro el texto (USANDO PANTALLA)
    blit_text(carta_pregunta['superficie'],pregunta['preguntas'],(10,10),fuente_pregunta,(255,255,255))
    
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(40, 250))
    blit_text(cartas_respuestas[0]['superficie'],pregunta['respuesta_1'],(10,10),fuente_respuesta,(255,255,255))
   
    #IMPRIMO EN PANTALLA LA CARTA R2 Y SU TEXTO
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(250, 250))
    blit_text(cartas_respuestas[1]['superficie'],pregunta['respuesta_2'],(10,10),fuente_respuesta,(255,255,255))
   
    #IMPRIMO EN PANTALLA LA CARTA R3 Y SU TEXTO
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(40, 350))
    blit_text(cartas_respuestas[2]['superficie'],pregunta['respuesta_3'],(10,10),fuente_respuesta,(255,255,255))
   
    #IMPRIMO EN PANTALLA LA CARTA R4 Y SU TEXTO
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'],(250, 350))
    blit_text(cartas_respuestas[3]['superficie'],pregunta['respuesta_4'],(10,10),fuente_respuesta,(255,255,255))
    return retorno