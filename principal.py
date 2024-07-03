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

#def cargar_animacion():
#   zeus = pygame.image.load("imagenes/zeus.png")
#   duelo = pygame.image.load("imagenes/zeus-te-reta.png") 
#   pantalla.blit(duelo,(0,0))
    
ventana_actual = 'menu'
corriendo = True
bandera_juego = True
FPS = 60
clock = pygame.time.Clock() 
pygame.display.flip()
MUSICA_MENU.play(-1)
MUSICA_MENU.set_volume(volumen_musica)



aux = 1
while corriendo:
    clock.tick(FPS)
    
    if ventana_actual == 'menu':
        ventana_actual = mostrar_menu(pantalla,pygame.event.get())
    elif ventana_actual == 'puntuaciones':
        ventana_actual = mostrar_ranking(pantalla,pygame.event.get())
    elif ventana_actual == "juego":
        if bandera_juego:
            bandera_juego = False
        ventana_actual = mostrar_juego(pantalla,pygame.event.get())
    elif ventana_actual == "opciones":
        ventana_actual = mostrar_opciones(pantalla,pygame.event.get())
    elif ventana_actual == "agregar":
        ventana_actual = mostrar_agregar_opciones(pantalla,pygame.event.get())
    elif ventana_actual == "terminado":
        if bandera_juego == False:
            bandera_juego = True
       
        ventana_actual = mostrar_juego_terminado(pantalla,pygame.event.get(),juego.puntuacion)
          
       
    
            
#       if bandera_juego:
#           pygame.mixer.music.load("musica.mp3") #Define musica de fondo mientras juego
#           pygame.mixer.music.play(-1)
#           pygame.mixer.music.set_volume(opciones.volumen / 100) #Ajusta el sonido de la música de fondo para que sea el mismo que en las opciones
#           bandera_juego = False
#       ventana_actual = mostrar_juego(pantalla,pygame.event.get())
#   elif ventana_actual == 'puntuaciones':
#       ventana_actual = mostrar_puntuaciones(pantalla,pygame.event.get())
#   elif ventana_actual == 'terminado':
#       if bandera_juego == False:
#           pygame.mixer.music.stop() #Detiene mi música de fondo
#           bandera_juego = True
#       ventana_actual = mostrar_juego_terminado(pantalla,pygame.event.get(),juego.puntuacion)

    elif ventana_actual == "salir":
        corriendo = False
                       
    pygame.display.flip() #ACTUALIZA LA INFORMACION

pygame.quit()