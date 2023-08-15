'''
Criar um programa em Python que abra e reproduza o audio de um arquivo MP3
'''
import pygame
pygame.init()
pygame.mixer.music.load('ex20.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
