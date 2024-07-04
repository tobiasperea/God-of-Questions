import pygame
import json
from datetime import datetime
from constantes import *
from juego import *


pygame.init()
#------imagenes-----
fondo = pygame.image.load("imagenes/caronte.png")
fondo = pygame.transform.scale(fondo, (500, 500))
cuadro_texto = pygame.image.load("imagenes/cuadrado_prueba.png")
fuente = pygame.font.SysFont("Arial Narrow", 40)
cuadro = {"superficie": pygame.Surface((250, 50)), "rectangulo": pygame.Rect(0, 0, 0, 0)}
cuadro['superficie'].blit(cuadro_texto, (0, 0))

nombre = ""

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
#--------guarda los datos------
def guardar_nombre(nombre, puntuacion):
    datos = {
        "nombre": nombre,
        "puntuacion": puntuacion,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        with open("partidas.json", "r") as archivo:
            try:
                partidas = json.load(archivo)
            except json.JSONDecodeError:
                partidas = []
    except FileNotFoundError:
        partidas = []

    partidas.append(datos)
    
    with open("partidas.json", "w") as archivo:
        json.dump(partidas, archivo, indent=4)
#---------restablece el nombre---
def restablecer_nombre():
    global nombre
    nombre = ""

def restablecer_puntuacion():
    global puntuacion
    puntuacion = 0

#------MUESTRA LA VENTANA DE FIN DEL JUEGO---
def mostrar_juego_terminado(pantalla:pygame.Surface, eventos, puntuacion):
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
                cuadro['superficie'].fill((0,0,0))# limpio la superficie de su texto anterior

            """if letra_presionada == 'space':
                nombre += " """
            
            if len(letra_presionada) == 1 and letra_presionada.isalpha(): 
                if bloc_mayus:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada  

            if len(nombre) == 4:
                guardar_nombre(nombre,puntuacion)
                inicializar_juego(0)
                restablecer_nombre()
                puntuacion = 0
                cuadro['superficie'].fill((0,0,0))
                retorno="menu"
                  
        elif evento.type == pygame.QUIT:
            retorno = "salir"
        pantalla.blit(fondo,(0,0))

        cuadro['rectangulo'] = pantalla.blit(cuadro['superficie'],(100,320))
    
        blit_text(cuadro['superficie'],nombre,(10,0),fuente,(250,250,250))
        blit_text(pantalla,f"Obtuviste {puntuacion} puntos mortal, cual es tu nombre",(100,250),fuente,(250,250,250))
        
    return retorno

    