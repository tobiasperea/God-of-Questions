import pygame
import json
from menu import *
from opciones import *
from funciones import *

def blit_text(surface, text, pos, font, color=pygame.Color('black')): #Funcion bliteo de texto
    words = [word.split(' ') for word in text.splitlines()]  
    space = font.size(' ')[0] 
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  
        y += word_height  
          
def parse_json(nombre_archivo: str): #Funcion parseo de json
    lista_elementos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            try:
                lista_elementos = json.load(archivo)
            except json.JSONDecodeError:
                lista_elementos = []
    except FileNotFoundError:
        lista_elementos = []
    return lista_elementos

"""lista = parse_json("partidas.json") 
for i in range(len(lista)):
    for j in range(i+1,len(lista),1):
        if(lista[i]['puntuacion'] < lista[j]['puntuacion']):
            aux = lista[i]['puntuacion']
            lista[i]['puntuacion'] = lista[j]['puntuacion']
            lista[j]['puntuacion'] = aux"""




#------------------------imagenes-------------------------------------
imagen_ranking = pygame.image.load("imagenes/fondo_ranking.png") #Carga el fondo del ranking
salida = pygame.image.load("imagenes/flecha_salida.png") #carga la imagen de flecha salida
recarga = pygame.image.load("imagenes/recargar.png") #carga la imagen de recarga
marco_salida = salida.get_rect(topleft=(10,10)) #crea una hitbox en flecha salida
marco_recarga = recarga.get_rect(topleft=(450,450)) #crea una hitbox en recarga

fuente_top = pygame.font.SysFont("Argelian",35) #La fuente en la que se escribe los nombres

def mostrar_ranking(pantalla:pygame.Surface,eventos): #funcion para cargar la ventana puntuaciones
    retorno = 'puntuaciones'
    lista = parse_json("partidas.json") 
    
    """for i in range(len(lista)):
        for j in range(i+1,len(lista),1):
            if(lista[i]['puntuacion'] < lista[j]['puntuacion']):
                aux = lista[i]['puntuacion']
                lista[i]['puntuacion'] = lista[j]['puntuacion']
                lista[j]['puntuacion'] = aux"""
    for i in range(len(lista)):  #Ordena la lista
        for j in range(i + 1, len(lista), 1):
            if lista[i]['puntuacion'] < lista[j]['puntuacion']:
                aux = lista[i]['puntuacion']
                lista[i]['puntuacion'] = lista[j]['puntuacion']
                lista[j]['puntuacion'] = aux
    lista = lista[:10]
    


    for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if marco_salida.collidepoint(evento.pos): #si se apreta la fecha roja devolvera al menu
                    print("saliendo")
                    click_sonido.play()
                    click_sonido.set_volume(volumen_sonidos)
                    retorno = "menu"
                elif marco_recarga.collidepoint(evento.pos): #Recarga la lista
                    print("Recargarndo")
                    click_sonido.play()
                    click_sonido.set_volume(volumen_sonidos)
                    for i in range(len(lista)):
                        for j in range(i+1,len(lista),1):
                            if(lista[i]['puntuacion'] < lista[j]['puntuacion']):
                                aux = lista[i]['puntuacion']
                                lista[i]['puntuacion'] = lista[j]['puntuacion']
                                lista[j]['puntuacion'] = aux
            elif evento.type == pygame.QUIT:
                retorno = "salir" #El estado salir -> Cuando se le da a la X

    pantalla.blit(imagen_ranking,(0,0))# se carga el fondo
    pantalla.blit(salida,marco_salida.topleft) #Se carga la flecha salida
    pantalla.blit(recarga,marco_recarga.topleft) # se carga el cuadro para recargar la lista
    
    if lista: #if por si la lista esta vacia
        texto = mostrar_top(lista)
        blit_text(pantalla,texto,(50,100),fuente_top,(0,0,0))
    else:
        texto_error = "NO HAY PARTIDAS GUARDADAS"
        blit_text(pantalla,texto_error, (50,100),fuente_top,(0,0,0))


    return retorno 
