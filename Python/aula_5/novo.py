from lib import *

altura = 40
largura = 40
pixel = 10

fundo = get_map(largura,altura,pixel)

# def quadrado_vazado(x,y):

for i in range(largura):        
    fundo[0][i] = (0,255,0)
    fundo[i][39] = (0,255,0)
    fundo[0][i] = (0,255,0)
    fundo[39][i] = (0,255,0)
    
start(bg_map=fundo)

x = input('nao sei:')
    

