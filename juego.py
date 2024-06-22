import pygame

pygame.init() #Se inicializa pygame
imagen = pygame.image.load("god of questions.jfif")
print(type(imagen))
pantalla = pygame.display.set_mode([500, 500])
pantalla.blit(imagen,(50,50))
pygame.display.set_caption("God of Questions")

corriendo = True

while corriendo:
   # Se verifica si el usuario cerro la ventana
   for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False