import pygame
from funciones import *
from constantes import *
from zeustereta import *
from juego import *
from opciones import *
from menu import *
from configurar_preguntas import *
from terminado import *
import juego
from ranking import *
import opciones
#from juego import *
pygame.init() #Se inicializa pygame
#------------------fondo----------------------------
pantalla = pygame.display.set_mode([500, 500])
pygame.display.set_caption("God of Questions")


    
ventana_actual = 'menu' #Ventana en la que se inicia el juego
corriendo = True #Estado del juego
bandera_juego = True
FPS = 60
clock = pygame.time.Clock() 
pygame.display.flip()
#----------------musica--------------------------
MUSICA_MENU.play(-1)
MUSICA_MENU.set_volume(volumen_musica)



aux = 1
while corriendo:
    clock.tick(FPS)
    
    if ventana_actual == 'menu': #Carga la ventana menu
        ventana_actual = mostrar_menu(pantalla,pygame.event.get())
    elif ventana_actual == 'puntuaciones': #Carga la ventana Puntuaciones
        ventana_actual = mostrar_ranking(pantalla,pygame.event.get())
    elif ventana_actual == "juego": #Carga el juego
        if bandera_juego:
            bandera_juego = False
        ventana_actual = mostrar_juego(pantalla,pygame.event.get()) 
    elif ventana_actual == "opciones": #Carga las  opciones
        ventana_actual = mostrar_opciones(pantalla,pygame.event.get())
    elif ventana_actual == "agregar": #Carga la ventana configurar preguntas
        ventana_actual = mostrar_agregar_opciones(pantalla,pygame.event.get())
    elif ventana_actual == "terminado": 
        if bandera_juego == False:
            bandera_juego = True
       
        ventana_actual = mostrar_juego_terminado(pantalla,pygame.event.get(),juego.puntuacion)
          
       
    
            

    elif ventana_actual == "salir": #Sale del juego
        corriendo = False
                       
    pygame.display.flip() #ACTUALIZA LA INFORMACION

pygame.quit()