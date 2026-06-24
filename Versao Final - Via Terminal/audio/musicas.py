"""
Esse arquivo contém as funções que inicializam as músicas no jogo
"""


import pygame

def inicializaMusicaPrincipal():

    audio1 = "assets\\music\\lost_in_the_unknown.flac"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio1)
    pygame.mixer.music.play(-1)

    return

def inicializaMusicaBatalha():

    audio2 = "assets\\music\\BattleTheme2.mp3"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio2)
    pygame.mixer.music.play(-1)

    return

def inicializaMusicaUparSkills():

    audio3 = "assets\\music\\8bitBossa.mp3"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio3)
    pygame.mixer.music.play(-1)

    return