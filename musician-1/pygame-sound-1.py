# Simple Sound with PyGame - Python Code - Elizabeth Tweedale

import pygame

pygame.init()

screen = pygame.display.set_mode([400, 400])

pygame.display.set_caption('Super Skills')

click_sound = pygame.mixer.Sound("whirl.ogg")

soundboard = True

while soundboard:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            soundboard = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

print ("Goodbye Soundboard!")
pygame.quit()
