import random as rd
from lib import init, get_height, get_width

# A função recebe o objeto que esta sendo simulado, os outros objetos presentes na tela, e o tempo desde a última movimentação.
# Cada objeto tem a seguinte estrutura:

# =========================================
# ||                                     ||
# ||    obj : {                          ||
# ||              x             : _      ||
# ||              y             : _      ||
# ||              velocity_x    : _      ||
# ||              velocity_y    : _      ||
# ||              ray           : _      ||
# ||    }                                ||
# ||                                     ||
# =========================================


# Implemente uma função chamada 'dvd()', que tem o comportamento igual ao de televisões quando ficam ociosas
# Implemente uma função chamada 'gravidade()' que aplica gravidade aos objetos | aceleração = 980 (pixels/s², 100px -> 1m, 980px -> 9.8m)
# Se divirta e fique livre para implementar o que quiser dentro de sua simulação :)


def gravidade_terra(obj, objs, t):
    
    a = 980
    
    obj['velocity_y'] = obj['velocity_y'] + a * t
    obj['y'] = obj['y'] + obj["velocity_y"]* t

    
def dvd(obj,objs,t):
    
    obj['y'] = obj['y'] + obj["velocity_y"]
    obj['x'] = obj['x'] + obj["velocity_x"]
    
    chao = get_height()
    parede = get_width()
    teto = 0
    paredeE = 0
    
    if obj['y'] + obj['ray'] > chao:
        obj['velocity_y'] = obj['velocity_y'] * -1

    if obj['x'] + obj['ray'] > parede:
        obj['velocity_x'] = obj['velocity_x'] * -1

    if obj['y'] - obj['ray'] < teto:
        obj['velocity_y'] = obj['velocity_y'] * -1

    if obj['x'] - obj['ray'] < paredeE:
        obj['velocity_x'] = obj['velocity_x'] * -1

e = [
    {'label' : 'DVD',
     'pos_xy' : (500,500),
     'velocities_xy' : (5,5),
     'aceleration'   : 980,
     'color' : 'gray', 
     'ray' : 30,
     'behavior' : dvd
     }
]

init(entities=e, fps=60)