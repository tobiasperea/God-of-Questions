import pygame
import pygame.locals
from opciones import *
from constantes import *
from funciones import *
import juego

pygame.init()

fondo_agregar = pygame.image.load("imagenes/fondo_agregar.png")


marco_pregunta = pygame.image.load("imagenes/marco_solo.png")
flecha_aumentar = pygame.image.load("imagenes/flecha_subida.png")
flecha_disminuir = pygame.image.load("imagenes/flecha.png")
salida = pygame.image.load("imagenes/flecha_salida.png")
#----------------------rect-----------------------
#--salida--
marco_salida = flecha_salida.get_rect(topleft=(10,10))
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

cantidad_puntos = 40
cantidad_oportunidades = 3
cantidad_respuestas = 4
cantidad_tiempo = 120

def mostrar_agregar_opciones(pantalla:pygame.Surface,eventos):
    retorno = "agregar"
    global cantidad_puntos
    global cantidad_oportunidades
    global cantidad_respuestas
    global cantidad_tiempo
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
                if cantidad_oportunidades >= 4:
                    cantidad_oportunidades += 1
            elif marco_flecha_menos_oportunidades.collidepoint(evento.pos):
                print("Disminuyeros las vidas")
                if cantidad_oportunidades <= 2:
                    cantidad_oportunidades -= 1
            elif marco_flecha_mas_respuestas.collidepoint(evento.pos):
                print("Aumentaron las respuestas")
                if cantidad_respuestas >= 3:
                    cantidad_respuestas += 1
            elif marco_flecha_menos_respuestas.collidepoint(evento.pos):  
                print("Disminuyeros las respuestas") 
                if cantidad_respuestas <= 3:
                    cantidad_respuestas -= 1
            elif marco_flecha_mas_tiempo.collidepoint(evento.pos):
                print("Aumento el tiempo")
                if cantidad_tiempo >= 119:
                    cantidad_tiempo += 20
            elif marco_flecha_menos_tiempo.collidepoint(evento.pos):
                print("Disminuyo el tiempo")
                if cantidad_tiempo <= 30:
                    cantidad_tiempo -= 20
        elif evento.type == pygame.QUIT:
            retorno = "salir" #El estado salir -> Cuando se le da a la X


    pantalla.blit(fondo_agregar,(0,0))
    pantalla.blit(salida,marco_salida)
    pantalla.blit(marco_pregunta,(100,220))
    pantalla.blit(marco_pregunta,(100,390))
    pantalla.blit(marco_pregunta,(375,220))
    pantalla.blit(marco_pregunta,(375,390))
    pantalla.blit(flecha_subida,marco_flecha_mas_puntos)
    pantalla.blit(flecha,marco_flecha_menos_puntos)
    pantalla.blit(flecha_subida,marco_flecha_mas_oportunidades)
    pantalla.blit(flecha,marco_flecha_menos_oportunidades)
    pantalla.blit(flecha_subida,marco_flecha_mas_respuestas)
    pantalla.blit(flecha,marco_flecha_menos_respuestas)
    pantalla.blit(flecha_subida,marco_flecha_mas_tiempo)
    pantalla.blit(flecha,marco_flecha_menos_tiempo)
            
            
                                                   
    return retorno



