from lib import *
import random

pixel = 7
altura = 100
largura = 100

def posicao_valida(y,x):
    if x < 0:
        return False
    if x >= largura:
        return False
    
    if y < 0:
        return False
    if y >= altura:
        return False
    
    return True

def verifica_ao_redor(mapa,y,x):
    quantidade = 0
    
    if posicao_valida(y,x-1) and mapa[y][x-1]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y,x+1) and  mapa[y][x+1]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y+1,x) and  mapa[y+1][x]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y-1,x) and  mapa[y-1][x]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y-1,x+1) and  mapa[y-1][x+1]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y-1,x-1) and  mapa[y-1][x-1]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y+1,x-1) and  mapa[y+1][x-1]['color'] == (255,0,0):
        quantidade += 1
    if posicao_valida(y+1,x+1) and  mapa[y+1][x+1]['color'] == (255,0,0):
        quantidade += 1
        
    return quantidade

def comportamento(e, e_map):
    vizinhos = verifica_ao_redor(e_map, e['y'],e['x'])
    
    vivo = e['color'] == (255,0,0)
    
    if vivo:
        if vizinhos < 2 or vizinhos > 4:
            if random.randint(1, 25) != 1:
                e['color'] = (0,0,0)
    else:
        if vizinhos == 3:
            e['color'] = (255,0,0)
        
celula_morta = { 
    'func'  : comportamento,
    'color' : (0,0,0),
    'z'     : 1,
    'label' : 'celula'   
}

celula_viva = { 
    'func'  : comportamento,
    'color' : (255,0,0),
    'z'     : 1,
    'label' : 'celula'   
}

mapa_de_entidade = get_map(largura,altura,pixel)

for i in range(altura):
    for j in range(largura):
        mapa_de_entidade[i][j] = celula_morta.copy()
        
mapa_de_entidade[49][50] = celula_viva.copy()
mapa_de_entidade[50][50] = celula_viva.copy()
mapa_de_entidade[51][50] = celula_viva.copy()     

start(e_map=mapa_de_entidade)