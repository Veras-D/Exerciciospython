import pygame
pygame.init()
pygame.mixer.music.load('ex021py.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
input()
pygame.event.wait()
