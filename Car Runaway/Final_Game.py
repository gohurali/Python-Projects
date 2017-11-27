import pygame, random, math, sys
from pygame.locals import *

#Gohur Ali- Final Game
#Music Credits go to Dr Dre and Snoop Dogg

class Player(pygame.sprite.Sprite):
    def __init__(self, starty):
        pygame.sprite.Sprite.__init__(self)
        # Images
        self.aliveImage = pygame.image.load("playercar.png").convert_alpha()
        #self.deadImage = pygame.image.load("data/PlayerExplode.png").convert_alpha()
        self.image = self.aliveImage
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = starty - self.rect.height
        self.speed = 7
        self.dead = False
        self.score = 0


    # Explode if you get hit, lose a life
    def explode(self):
        if not self.dead:
            self.dead = True
            self.image = self.deadImage
            pygame.mixer.stop()
            self.channel = self.explodeSound.play()
            game.playerShots.empty()
            game.enemyShots.empty()
            game.wave.mship.empty()
            game.lives.update(-1)

    def score(self):
        self.score += 1



class pedestrian_cars(pygame.sprite.Sprite):
    def __init__(self, starty,startx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pedcar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = starty - self.rect.height
        self.rect.x = startx - self.rect.width
        self.delta_y = 5 # 5
        self.gravity = .5 #.5
        self.has_spawned = False

    def update(self):
        self.rect.y += self.delta_y

    def spawn(self):
        if self.rect.y == 480 or self.has_spawned == False:
            self.has_spawned = True
            self.rect.x = random.randint(60,300)
            self.rect.y = -10


def main():
    """ Set up the game and run the main game loop """
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init() # prepare the pygame module for use
    pygame.font.init
    surfaceSz = 480 # Desired physical surface size, in pixels.
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surfaceSz, surfaceSz))

    #SPRITES###############################################################
    user_car = Player(450)
    enemy = pedestrian_cars(10,200)
    #SPRITES################################################################
    background_image = pygame.image.load("background2.png")

    all_sprites = pygame.sprite.Group()



    user_car.add(all_sprites)
    enemy.add(all_sprites)

    clock = pygame.time.Clock()

    b1 = "background2.png"
    back = pygame.image.load(b1).convert()
    back2 = pygame.image.load(b1).convert()
    y = 0
    screenWidth = 600
    screenHeight = 480

    calibri = pygame.font.SysFont("Calibri", 25, False, False)

#Sound/Music#####################################
    pygame.mixer.music.load("stilldre.wav")
    pygame.mixer.music.play(-1)
#-################################################


    while True:
        #user_car.score()
        #Score = calibri.render("score ={0}".format(), True, (0,0,0))
        ev = pygame.event.poll() # look for any event
        if ev.type == pygame.QUIT: # window close button clicked?
            break # ... leave game loop
            sys.exit()

        if not user_car.dead:
            # Move the player
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                user_car.rect.x = max(user_car.rect.x - user_car.speed, 116-user_car.rect.width)
            elif keys[pygame.K_RIGHT]:
                user_car.rect.x = min(user_car.rect.x + user_car.speed, 395-user_car.rect.width)

        else:
            # Go back to playing after the explosion sound finishes
            if not self.channel.get_busy():
                self.image = self.aliveImage
                self.dead = False
                self.rect.x = 200

        if user_car.rect.colliderect(enemy.rect):
            break


        # Update your game objects and data structures here...

        all_sprites.update()
        enemy.spawn()

        main_surface.fill((0,200,255))
        main_surface.blit(background_image, (0, 0))

        main_surface.blit(back, (0,y))
        main_surface.blit(back2,(0,y-screenHeight))
        #main_surface.blit(Score, (0,0))
        y = y + 8
        if y == screenWidth:
            y = 0

##        if enemy.alive.x ==
##        msElapsed = clock.tick(100)
##        pygame.display.flip()


        all_sprites.draw(main_surface)


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        clock.tick(200)
        msElapsed = clock.tick(100)

    pygame.quit() # once we leave the loop, close the window.

main()
