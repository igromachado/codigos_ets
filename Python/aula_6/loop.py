import os
import time


#===============================================
#   Crie uma funlçao que move a imagem
#   em X como se fosse uma esteira, portanto
#   o que está na ultima coluna case ande 1
#   para o lado a coluna vai para a primeira
#   coluna 
#===============================================

scene = [
    '    X                         X               X   ',
    '    X                        XX  X           XX   ',
    '   XX       X               XXXX XX          XXX  ',
    '   XXX      XX       X      XXXXXXXX         XXXX ',
    '  XXXXX    XXXX     XX     XXXXXXXXX        XXXXX ',
    ' XXXXXX   XXXXX    XXX    XXXXXXXXXXX       XXXXXX',
    ' XXXXXX  XXXXXXX   XXX    XXXXXXXXXXX      XXXXXXX',
    ' XXXXXXX XXXXXXX  XXXXX   XXXXXXXXXXXX     XXXXXXX',
    ' XXXXXXX XXXXXXXXXXXXXX  XXXXXXXXXXXXXX   XXXXXXXX',
]


def moveX(
        # DEFINA OS PARAMETROS
):

    #==============
    #    CODE
    #==============

    pass


for i in range(1000):
    scene = moveX(
        # PASSE OS PARAMETROS
    )

    for s in scene:
        print(s)
        
    time.sleep(0.01)
    os.system('cls')
