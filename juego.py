import pygame
from constantes import *
pygame.init() #Se inicializa pygame
#------------------fondo----------------------------
pantalla = pygame.display.set_mode([500, 500])
pygame.display.set_caption("God of Questions")
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

#---------------Fondo y preguntas-----------------------
pantalla.blit(imagen,(0,0))# se carga el fondo
pantalla.blit(marco_jugar, marco_rect1.topleft) #--se cargan los rectangulos
pantalla.blit(marco_rankign, marco_rect2.topleft)
pantalla.blit(marco_opciones, marco_rect3.topleft)
pantalla.blit(marco_salir, marco_rect4.topleft)
#jugar= "Jugar"
#fuente = pygame.font.SysFont("Arial Narrow", 48)
#texto = fuente.render(jugar, False, (0,0,0))
#pantalla.blit(texto,(200,230))
pygame.display.flip()
corriendo = True
#---------------Musica-----------------------
MUSICA_MENU.play(-1)
aux = 1
while corriendo:
   #print(segundos)
   contador = 0
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if marco_rect1.collidepoint(mouse_pos):
                segundos = pygame.time.get_ticks()/1000
                if aux == segundos:
                    aux +=1
                pantalla.fill((0,0,0))
                pygame.display.flip()
                print("JUGAR")
                pygame.mixer.stop()
                musica_smash = pygame.mixer.Sound("musicaysonidos\zeus-aparece.mp3")
                musica_smash.play()
                zeus = pygame.image.load("imagenes/zeus.png")
                duelo = pygame.image.load("imagenes/zeus-te-reta.png") 
                pantalla.blit(duelo,(0,0))
                pygame.display.flip()

            elif marco_rect2.collidepoint(mouse_pos):
                print("RANKING")
            elif marco_rect3.collidepoint(mouse_pos):
                print("OPCIONES")
            elif marco_rect4.collidepoint(mouse_pos):
                print("SALIENDO")
                corriendo = False
   

