import pygame
from opciones import *
from constantes import *
from funciones import *
from configurar_preguntas import *
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
marco_pregunta1 = pygame.image.load("imagenes/marco_pregunta1.png")
marco_respuesta = pygame.image.load("imagenes/marco_respuesta.png")
carta_pregunta = {"superficie": pygame.Surface((280, 100)), "rectangulo": pygame.Rect((0, 0, 0, 0))}
carta_pregunta["superficie"].blit(marco_pregunta1, (0, 0))

imagen_juego = pygame.image.load("imagenes/zeus.png")  # Se carga la imagen de fondo

cartas_respuestas = [
    {"superficie": pygame.Surface((100, 60)), "rectangulo": pygame.Rect((0, 0, 0, 0))},  # R1 -> 0
    {"superficie": pygame.Surface((100, 60)), "rectangulo": pygame.Rect((0, 0, 0, 0))},  # R2 -> 1
    {"superficie": pygame.Surface((100, 60)), "rectangulo": pygame.Rect((0, 0, 0, 0))},  # R3 -> 2
    {"superficie": pygame.Surface((100, 60)), "rectangulo": pygame.Rect((0, 0, 0, 0))}  # R4 -> 3
]
for carta in cartas_respuestas:
    carta['superficie'].blit(marco_respuesta, (0, 0))
fuente_pregunta = pygame.font.SysFont("Argelian", 30)
fuente_respuesta = pygame.font.SysFont("Argelian", 20)
fuente_puntuacion = pygame.font.SysFont("Argelian", 20)

click_sonido = pygame.mixer.Sound("musicaysonidos/Taco Bell Bong - Sound Effect (HD).mp3")
click_sonido.set_volume(volumen_sonidos)

def inicializar_juego():
    global indice_pregunta
    global puntuacion
    global vidas
    global limite_tiempo
    global tiempo_inicial
    global tiempo_inicializado
    global puntos
   

    indice_pregunta = 0
    puntuacion = 0  # Asegúrate de reiniciar la puntuación aquí
    vidas = cantidad_oportunidades
    limite_tiempo = cantidad_tiempo
    tiempo_inicial = 0
    tiempo_inicializado = False
    puntos = cantidad_puntos
    
    
random.shuffle(lista_preguntas)

# Inicializar los valores del juego al inicio
inicializar_juego()

def mostrar_juego(pantalla: pygame.Surface, eventos):
    global indice_pregunta
    global limite_tiempo
    global tiempo_inicial
    global tiempo_inicializado
    global puntuacion
    global vidas
    global cantidad_puntos
    
    retorno = "juego"  # Un estado de la ventana en la que estoy parado
    if not tiempo_inicializado:
        tiempo_inicial = pygame.time.get_ticks()
        tiempo_inicializado = True
    
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = (tiempo_actual - tiempo_inicial) / 1000
    tiempo_restante = limite_tiempo - tiempo_transcurrido

    if tiempo_restante <= 0:
        retorno = "terminado"
        

    pregunta = lista_preguntas[indice_pregunta]

    click_sonido.set_volume(volumen_sonidos)
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    if pregunta["correcta"] == (i + 1):
                        click_sonido.play()
                        print("RESPUESTA CORRECTA") 
                        carta_pregunta['superficie'].blit(marco_pregunta1, (0, 0))
                        for carta in cartas_respuestas:
                            carta['superficie'].blit(marco_respuesta, (0, 0))

                        indice_pregunta += 1    

                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        else:
                            # TERMINO EL JUEGO
                            retorno = "terminado"
                            inicializar_juego()  # Reiniciar los valores del juego cuando termina
                        puntuacion += cantidad_puntos
                        
                    else:
                        print("RESPUESTA INCORRECTA")
                        carta_pregunta['superficie'].blit(marco_pregunta1, (0, 0))
                        for carta in cartas_respuestas:
                            carta['superficie'].blit(marco_respuesta, (0, 0))
                        
                        vidas -= 1
                        if vidas <= 0:
                            retorno = "terminado"
                            inicializar_juego()  # Reiniciar los valores del juego cuando termina
                        else:
                            indice_pregunta += 1    
                        
                        if indice_pregunta != len(lista_preguntas):
                            pregunta = lista_preguntas[indice_pregunta]
                        
                        puntuacion -= 50
                        

        if evento.type == pygame.QUIT:
            retorno = "salir" 

    pantalla.blit(imagen_juego, (0, 0))  # se carga el fondo

    pantalla.blit(carta_pregunta['superficie'], (100, 150))
    # Muestro el texto (USANDO PANTALLA)
    blit_text(carta_pregunta['superficie'], pregunta['preguntas'], (10, 10), fuente_pregunta, (255, 243, 0))
    
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'], (50, 300))
    blit_text(cartas_respuestas[0]["superficie"], pregunta['respuesta_1'], (20, 20), fuente_respuesta, (255, 243, 0))
   
    # IMPRIMO EN PANTALLA LA CARTA R2 Y SU TEXTO
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'], (300, 300))
    blit_text(cartas_respuestas[1]["superficie"], pregunta['respuesta_2'], (20, 20), fuente_respuesta, (255, 243, 0))
   
    # IMPRIMO EN PANTALLA LA CARTA R3 Y SU TEXTO
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'], (50, 400))
    blit_text(cartas_respuestas[2]["superficie"], pregunta['respuesta_3'], (20, 20), fuente_respuesta, (255, 243, 0))
   
    # IMPRIMO EN PANTALLA LA CARTA R4 Y SU TEXTO
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'], (300, 400))
    blit_text(cartas_respuestas[3]["superficie"], pregunta['respuesta_4'], (20, 20), fuente_respuesta, (255, 243, 0))

    blit_text(pantalla, f"Puntuación: {puntuacion} puntos", (10, 10), fuente_puntuacion, (255, 243, 0))

    blit_text(pantalla, f"Tiempo: {int(tiempo_restante)}", (10, 50), fuente_puntuacion, (255, 243, 0))

    blit_text(pantalla, f"Vidas: {int(vidas)}", (10, 80), fuente_puntuacion, (255, 243, 0))
    
    return retorno
