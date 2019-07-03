import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 500
ICON_SIZE = 32

def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption( "LA GALLINA QUE CRUZA LA CALLE" )
      fuente = pygame.font.Font(None, 30)
      background_image = util.cargar_imagen('imagenes/fondo.png')
      background_sound = util.cargar_sonido ('sonidos/hen.wav')
      pierde_vida = util.cargar_sonido('sonidos/live.wav')
      pygame.mouse.set_visible( False )
      temporizador = pygame.time.Clock()
      heroe = Heroe()
      villano = [Villano((100,90),7),Villano((200,215),18),Villano((300,340),10)]
      background_sound.play(100)
      while jugando:
          heroe.update()
          if heroe.vida <= 0:
              jugando = False
          texto_vida = fuente.render("Vida: " + str(heroe.vida), 1, (250, 250, 250))
	  texto_puntos = fuente.render("Puntos: " + str(heroe.puntos), 1, (200, 250, 250))
          for n in villano:
              n.update()
          heroe.image = heroe.imagenes[0]
          for n in villano:
              if heroe.rect.colliderect(n.rect):
                  heroe.image = heroe.imagenes[1]
                  pierde_vida.play()
		  pygame.time.delay(10)
                  heroe.vida -= 1

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                sys.exit()
          screen.blit(background_image, (0,0))
          screen.blit(heroe.image, heroe.rect)
          for n in villano:
              screen.blit(n.image, n.rect)
          screen.blit(texto_vida, (20, 10))
          pygame.display.update()
          pygame.time.delay(10)
          
          """ 
          for n in rect:
            if heroe.rect.height(n.rect):
				heroe.puntos +=1
          """          
          screen.blit(texto_puntos, (500, 10))

if __name__ == '__main__':
      game()
