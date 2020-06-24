import pygame
import random
import sys
pygame.init()

frstr = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Operatiunea Mona")

ceas = pygame.time.Clock()
bgpng = pygame.image.load("Img/bg.png")
playerpng = pygame.image.load("Img/player.png")
glontpng = pygame.image.load("Img/glont.png")
asteroidpng = pygame.image.load("Img/asteroid.png")
spirtpng = pygame.image.load("Img/spirt.png")
spirtwav = pygame.mixer.Sound("Aud/spirt.wav")

spirtscr = 0
scorprec = 0

font = pygame.font.SysFont("arial", 40)

def scr():
    text = font.render("Scor:" + str(spirtscr), True, (0, 200, 255))
    text2 = font.render("Scorul precedent:" + str(scorprec), True, (0, 150, 205))
    textRect = text.get_rect()
    textRect.center = (65, 740)
    textRect2 = text.get_rect()
    textRect2.center = (65, 780)
    frstr.blit(text, textRect)
    frstr.blit(text2, textRect2)
    
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(playerpng, (80, 110))
        self.rect = self.image.get_rect()
        self.rect.x = 400 - 80
        self.rect.y = 800 - 110
        self.vit = 6
    def update(self):
        self.taste = pygame.key.get_pressed()
        if self.taste[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.vit
        if self.taste[pygame.K_DOWN] and self.rect.y < 800 - 110:
            self.rect.y += self.vit
        if self.taste[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.vit
        if self.taste[pygame.K_RIGHT] and self.rect.x < 800 - 80:
            self.rect.x += self.vit

class glont(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(glontpng, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vit = 12
    def update(self):
        self.rect.y -= self.vit
        if self.rect.y < -32:
            self.kill()

class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(asteroidpng, (129, 118))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - 129)
        self.rect.y = random.randrange(-118, -236, -1)
        self.vit = random.randrange(4, 6)
    def update(self):
        self.rect.y += self.vit
        if self.rect.y > 918:
            self.rect.y = random.randrange(-118, -236, -1)
            self.rect.x = random.randrange(0, 800 - 129)
        elif lovitply:
            self.kill()

class spirt(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(spirtpng, (53, 122))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800 - 53)
        self.rect.y = random.randrange(0, 800 - 122)   
            
toate = pygame.sprite.Group()
gloante = pygame.sprite.Group()
asteroizi = pygame.sprite.Group()
jucatori = pygame.sprite.Group()
spirturi = pygame.sprite.Group()
ply = player()
jucatori.add(ply)
toate.add(ply)
sprt = spirt()
toate.add(sprt)
spirturi.add(sprt)

rulare = True
while rulare:
    ceas.tick(120)
    frstr.blit(bgpng, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gl = glont(ply.rect.x + 25, ply.rect.y - 20)
                gloante.add(gl)
                toate.add(gl)

    lovitaster = pygame.sprite.groupcollide(asteroizi, gloante, True, True)
    lovitply = pygame.sprite.groupcollide(jucatori, asteroizi, False, False)
    lovitsprt = pygame.sprite.groupcollide(spirturi, jucatori, True, False)
    
    if lovitaster:
        aster = asteroid()
        toate.add(aster)
        asteroizi.add(aster)
        
    if lovitsprt:
        sprt = spirt()
        spirtwav.play()
        toate.add(sprt)
        spirturi.add(sprt)
        aster = asteroid()
        toate.add(aster)
        asteroizi.add(aster)
        spirtscr += 1

    if lovitply:
        scorprec = spirtscr
        spirtscr = 0
        sprt.rect.x = random.randrange(0, 800 - 53)
        sprt.rect.y = random.randrange(0, 800 - 122)
        ply.rect.x = 400 - 80
        ply.rect.y = 800 - 110
            

            
    toate.update()
    toate.draw(frstr)
    scr()
    pygame.display.flip()
