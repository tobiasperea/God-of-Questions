import pygame

pygame.init() #Se inicializa pygame
#------------------fondo----------------------------
pantalla = pygame.display.set_mode([500, 500])
pygame.display.set_caption("God of Questions")
imagen = pygame.image.load("imagenes/god-of-questions.png")#Se carga la imagen de fondo
imagen = pygame.transform.scale(imagen, (500,500))#Se escala la imagen de fondo
#---------------Cartas preguntas-----------------------
carta_pregunta = pygame.Surface(((350,150)))
carta_pregunta = {"superficie":pygame.Surface((150,55)),"rectangulo":pygame.Rect(0,0,0,0)}#se crea el marco que servira de objetivo
carta_pregunta['superficie'].fill((250,125,51))
carta_pregunta['rectangulo'] = pantalla.blit(carta_pregunta['superficie'],(170,220))
pantalla.blit(imagen,(170,220)) # se carga el marco objetivo
marco_pregunta = pygame.image.load("imagenes/marco.png") #se carga el marco de la pregunta que se vera
pantalla.blit(imagen,(0,0))# se carga el fondo
pantalla.blit(marco_pregunta,(40,250))#se carga el marco objetivo
pantalla.blit(marco_pregunta,(40,380))
pantalla.blit(marco_pregunta,(300,250))
pantalla.blit(marco_pregunta,(300,380))
#jugar= "Jugar"
#fuente = pygame.font.SysFont("Arial Narrow", 48)
#texto = fuente.render(jugar, False, (0,0,0))
#pantalla.blit(texto,(200,230))
pygame.display.flip()
corriendo = True


while corriendo:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False


   

