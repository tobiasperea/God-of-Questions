import pygame


pygame.init() #Se inicializa pygame
pantalla_tamaño = (500, 500)
pantalla = pygame.display.set_mode(pantalla_tamaño)
pygame.display.set_caption("God of Questions")
imagen = pygame.image.load('C:/Users/12345/Desktop/segund par/god-of-questions.png')
imagen = pygame.transform.scale(imagen, (500,500))
carta_pregunta = pygame.Surface(((350,150)))

pantalla.blit(imagen,(0,0))
carta_pregunta = {"superficie":pygame.Surface((150,100)),"rectangulo":pygame.Rect(0,0,0,0)}
carta_pregunta['superficie'].fill((250,125,51))
carta_pregunta['rectangulo'] = pantalla.blit(carta_pregunta['superficie'],(200,230))
jugar= "Jugar"
fuente = pygame.font.SysFont("Arial Narrow", 48)
texto = fuente.render(jugar, False, (0,0,0))
pantalla.blit(texto,(200,230))
pygame.display.flip()
corriendo = True

while corriendo:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False

   

