import pygame
def cargar_animacion(pantalla, eventos):
    retorno = "juego"
    
    

    for evento in eventos:   
        
        if evento.type == pygame.QUIT:
            retorno= "salir"
    zeus = pygame.image.load("imagenes/zeus.png")
    duelo = pygame.image.load("imagenes/zeus-te-reta.png")
    
    pantalla.blit(duelo,(0,0))
    
        
    
    return retorno