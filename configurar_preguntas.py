import pygame
import pygame.locals
from opciones import *
from constantes import *
from funciones import *
import juego

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

fondo_agregar = pygame.image.load("imagenes/fondo_agregar.png")


#marco_pregunta = pygame.image.load("imagenes/marco_solo.png")
flecha_aumentar = pygame.image.load("imagenes/flecha_subida.png")
flecha_disminuir = pygame.image.load("imagenes/flecha.png")
cartel_puntos = pygame.image.load("imagenes/cartel_puntos.png")
cartel_vidas = pygame.image.load("imagenes/cartel_vidas.png")
cartel_tiempo = pygame.image.load("imagenes/cartel_tiempo.png")
cartel_respuestas = pygame.image.load("imagenes/cartel_respuestas.png")
salida = pygame.image.load("imagenes/flecha_salida.png")
#----------------------rect-----------------------
#--salida--
marco_salida = flecha_salida.get_rect(topleft=(10,10))

#rect_puntos = marco_pregunta.get_rect(topleft=(80,230))
#--puntos--
marco_flecha_menos_puntos = flecha_aumentar.get_rect(topleft=(30,230))
marco_flecha_mas_puntos = flecha_disminuir.get_rect(topleft=(170,230))
#---aportunidades---
marco_flecha_menos_oportunidades = flecha_aumentar.get_rect(topleft=(30,400))
marco_flecha_mas_oportunidades = flecha_disminuir.get_rect(topleft=(170,400))
#----mas respuestas------
marco_flecha_menos_respuestas = flecha_aumentar.get_rect(topleft=(300,230))
marco_flecha_mas_respuestas = flecha_disminuir.get_rect(topleft=(450,230))
#-----mas tiempo------
marco_flecha_menos_tiempo = flecha_aumentar.get_rect(topleft=(300,400))
marco_flecha_mas_tiempo = flecha_disminuir.get_rect(topleft=(450,400))

cantidad_puntos = 100
cantidad_oportunidades = 3
cantidad_respuestas = 4
cantidad_tiempo = 90
fuente_datos = pygame.font.SysFont("Argelian",20)

def mostrar_agregar_opciones(pantalla:pygame.Surface,eventos):
    retorno = "agregar"
    global cantidad_puntos
    global cantidad_oportunidades
    global cantidad_respuestas
    global cantidad_tiempo
    marco_puntos = pygame.image.load("imagenes/marco_solo.png")
    marco_vidas = pygame.image.load("imagenes/marco_solo.png")
    marco_respuestas = pygame.image.load("imagenes/marco_solo.png")
    marco_tiempo = pygame.image.load("imagenes/marco_solo.png")
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if marco_salida.collidepoint(evento.pos):
                print("salir")
                retorno = "menu"
            elif marco_flecha_mas_puntos.collidepoint(evento.pos):
                print("Aumentaron los puntos")
                if cantidad_puntos <= 199:
                    cantidad_puntos += 10
            elif marco_flecha_menos_puntos.collidepoint(evento.pos):
                print("Disminuyeros los puntos")
                if cantidad_puntos >= 39:
                    cantidad_puntos -= 10
            elif marco_flecha_mas_oportunidades.collidepoint(evento.pos):
                print("Aumentaron las vidas")
                if cantidad_oportunidades <= 4:
                    cantidad_oportunidades += 1
            elif marco_flecha_menos_oportunidades.collidepoint(evento.pos):
                print("Disminuyeros las vidas")
                if cantidad_oportunidades >= 2:
                    cantidad_oportunidades -= 1
            elif marco_flecha_mas_respuestas.collidepoint(evento.pos):
                print("Aumentaron las respuestas")
                if cantidad_respuestas <= 3:
                    cantidad_respuestas += 1
            elif marco_flecha_menos_respuestas.collidepoint(evento.pos):  
                print("Disminuyeros las respuestas") 
                if cantidad_respuestas >= 3:
                    cantidad_respuestas -= 1
            elif marco_flecha_mas_tiempo.collidepoint(evento.pos):
                print("Aumento el tiempo")
                if cantidad_tiempo <= 119:
                    cantidad_tiempo += 20
            elif marco_flecha_menos_tiempo.collidepoint(evento.pos):
                print("Disminuyo el tiempo")
                if cantidad_tiempo >= 30:
                    cantidad_tiempo -= 20
        elif evento.type == pygame.QUIT:
            retorno = "salir" #El estado salir -> Cuando se le da a la X


    pantalla.blit(fondo_agregar,(0,0))
    pantalla.blit(salida,marco_salida)
    pantalla.blit(cartel_vidas,(0,170))
    pantalla.blit(cartel_puntos,(0,0))
    pantalla.blit(cartel_tiempo,(270,170))
    blit_text(marco_puntos,str(cantidad_puntos),(15,20),fuente_datos,(0,255,0))
    pantalla.blit(marco_puntos,(100,220))
    #blit_text(marco_respuestas,str(cantidad_respuestas),(10,10),fuente_datos,(0,255,0))
    pantalla.blit(marco_respuestas,(375,220))
    blit_text(marco_vidas,str(cantidad_oportunidades),(20,20),fuente_datos,(0,255,0))
    pantalla.blit(marco_vidas,(100,390))
    blit_text(marco_tiempo,str(cantidad_tiempo),(15,20),fuente_datos,(0,255,0))
    pantalla.blit(marco_tiempo,(375,390))
    pantalla.blit(flecha_subida,marco_flecha_mas_puntos)
    pantalla.blit(flecha,marco_flecha_menos_puntos)
    pantalla.blit(flecha_subida,marco_flecha_mas_oportunidades)
    pantalla.blit(flecha,marco_flecha_menos_oportunidades)
    pantalla.blit(flecha_subida,marco_flecha_mas_respuestas)
    pantalla.blit(flecha,marco_flecha_menos_respuestas)
    pantalla.blit(flecha_subida,marco_flecha_mas_tiempo)
    pantalla.blit(flecha,marco_flecha_menos_tiempo)
    pantalla.blit(cartel_respuestas,(270,0)) 
            
                                                   
    return retorno



