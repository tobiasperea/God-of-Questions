import pygame
from constantes import *

pygame.init()
#fondo
imagen = pygame.image.load("imagenes/god-of-questions.png")#Se carga la imagen de fondo
imagen = pygame.transform.scale(imagen, (500,500))#Se escala la imagen de fondo

#---------------Marco-----------------------
marco_jugar = pygame.image.load("imagenes/jugar.png") #se carga el marco de la pregunta que se vera
marco_opciones = pygame.image.load("imagenes/opciones.png")
marco_rankign = pygame.image.load("imagenes/ranking.png")
marco_salir = pygame.image.load("imagenes/salir.png")
#---------------Rectangulos-----------------------
marco_rect1 = marco_jugar.get_rect(topleft=(40, 250))
marco_rect2 = marco_rankign.get_rect(topleft=(40, 380))
marco_rect3 = marco_opciones.get_rect(topleft=(300, 250))
marco_rect4 = marco_salir.get_rect(topleft=(300, 380))
#-------------Sonido------------------------------
click_sonido = pygame.mixer.Sound("musicaysonidos/Taco Bell Bong - Sound Effect (HD).mp3")
click_sonido.set_volume(1)
musica_smash = pygame.mixer.Sound("musicaysonidos/zeus-aparece.mp3")

    



def mostrar_menu(pantalla:pygame.Surface,eventos):
    retorno = "menu"#Un estado de la ventana en la que estoy parado
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if marco_rect1.collidepoint(evento.pos):
                print("JUGAR")
                click_sonido.play()
                musica_smash.play()
                retorno = "juego"
            elif marco_rect3.collidepoint(evento.pos):
                print("OPCIONES")
                click_sonido.play()
                #retorno = "opciones"
            elif marco_rect2.collidepoint(evento.pos):
                print("PUNTUACIONES")
                click_sonido.play()
                #retorno = "puntuaciones"
            elif marco_rect4.collidepoint(evento.pos):
                click_sonido.play()
                print("SALIR")
                retorno = "salir"
        elif evento.type == pygame.QUIT:
            retorno = "salir" #El estado salir -> Cuando se le da a la X

    pantalla.blit(imagen,(0,0))# se carga el fondo
    pantalla.blit(marco_jugar, marco_rect1.topleft) #--se cargan los rectangulos
    pantalla.blit(marco_rankign, marco_rect2.topleft)
    pantalla.blit(marco_opciones, marco_rect3.topleft)
    pantalla.blit(marco_salir, marco_rect4.topleft)

    return retorno

