import pygame
from constantes import *
pygame.init() #Se inicializa pygame
#------------------fondo----------------------------
pantalla = pygame.display.set_mode([500, 500])
pygame.display.set_caption("God of Questions")
imagen = pygame.image.load("imagenes/god-of-questions.png")#Se carga la imagen de fondo
imagen = pygame.transform.scale(imagen, (500,500))#Se escala la imagen de fondo
#---------------Marco-----------------------
marco_pregunta = pygame.image.load("imagenes/marco.png") #se carga el marco de la pregunta que se vera
#---------------Rectangulos-----------------------
marco_rect1 = marco_pregunta.get_rect(topleft=(40, 250))
marco_rect2 = marco_pregunta.get_rect(topleft=(40, 380))
marco_rect3 = marco_pregunta.get_rect(topleft=(300, 250))
marco_rect4 = marco_pregunta.get_rect(topleft=(300, 380))

#---------------Fondo y preguntas-----------------------
pantalla.blit(imagen,(0,0))# se carga el fondo
pantalla.blit(marco_pregunta, marco_rect1.topleft) #--se cargan los rectangulos
pantalla.blit(marco_pregunta, marco_rect2.topleft)
pantalla.blit(marco_pregunta, marco_rect3.topleft)
pantalla.blit(marco_pregunta, marco_rect4.topleft)
#jugar= "Jugar"
#fuente = pygame.font.SysFont("Arial Narrow", 48)
#texto = fuente.render(jugar, False, (0,0,0))
#pantalla.blit(texto,(200,230))
pygame.display.flip()
corriendo = True
#---------------Musica-----------------------
MUSICA_MENU.play(-1)

while corriendo:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if marco_rect1.collidepoint(mouse_pos):
                print("Marco 1 presionado")
            elif marco_rect2.collidepoint(mouse_pos):
                print("Marco 2 presionado")
            elif marco_rect3.collidepoint(mouse_pos):
                print("Marco 3 presionado")
            elif marco_rect4.collidepoint(mouse_pos):
                print("Marco 4 presionado")
   

