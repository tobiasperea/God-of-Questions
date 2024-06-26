import pygame 
from constantes import *

pygame.init()

fuente =  pygame.font.SysFont("Arial Narrow",40)
cuadro = {"superficie":pygame.Surface(),"rectangulo":pygame.Rect(0,0,0,0)}
#cuadro['superficie'].fill(COLOR_AZUL)
nombre = ""

def mostrar_juego_terminado(pantalla:pygame.Surface,eventos,puntaje):
    global nombre
    retorno = "terminado"
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        if evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)
                        
            if letra_presionada == 'backspace' and len(nombre) > 0:
                nombre = nombre[:-1]#Elimino el último
                #cuadro['superficie'].fill(COLOR_AZUL)# limpio la superficie de su texto anterior

            if letra_presionada == 'space':
                nombre += " "
            
            if len(letra_presionada) == 1 and letra_presionada.isalpha(): 
                if bloc_mayus:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada        
        elif evento.type == pygame.QUIT:
            retorno = "salir"