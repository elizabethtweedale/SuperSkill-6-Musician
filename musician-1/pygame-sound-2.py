# Simple Sound 2 with PyGame - Python Code - Elizabeth Tweedale

import pygame

pygame.init()

screen = pygame.display.set_mode([400, 400])

pygame.display.set_caption('Super Skills')

mouse_sound = pygame.mixer.Sound("whirl.ogg")
key_sound = pygame.mixer.Sound("blip.ogg")

soundboard = True

while soundboard:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            soundboard = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_sound.play()
        elif event.type == pygame.KEYDOWN:
            key_sound.play()

print ("Goodbye Soundboard!")
pygame.quit()
