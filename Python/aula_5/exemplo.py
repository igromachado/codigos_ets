import random as rd
from lib import *

H = 50
W = 50 
P = 10


def spawn_new_if_key(e, _, __, key):
    if key[get_key().K_SPACE]:
        new = e.copy()
        new['y'] -= 1
        new['x'] -= 1
        spawn(new)

def random_teleport(e):
    e['y'] = rd.randint(0, H-1)
    e['x'] = rd.randint(0, W-1)

def suicide(e, _, __, key):

    if key[get_key().K_w]:
        e['y'] -= 1
    if key[get_key().K_s]:
        e['y'] += 1
    if key[get_key().K_d]:
        e['x'] += 1
    if key[get_key().K_a]:
        e['x'] -= 1

    if e['y'] >= H-1 or e['y'] <= 0 or e['x'] >= W-1 or e['x'] <= 0:
        kill(e)



e_map  = get_map(W, H, P)
bg_map = get_map(W, H, P)

obj0 = {
    'label' : 'BEING',
    'color' : (255,0,0),
    'z'     : 1,
    'func'  : random_teleport 
}
obj1 = {
    'label' : 'BEING',
    'color' : (0,255,0),
    'z'     : 1,
    'func'  : suicide
}
obj2 = {
    'label' : 'BEING',
    'color' : (0,0,255),
    'z'     : 1,
    'func'  : spawn_new_if_key
}

e_map[H//2+1][W//2+1]   = obj0
e_map[H//2][W//2]       = obj1
e_map[H//2-1][W//2-1]   = obj2

for i in range(H):
    for j in range(W):
        bg_map[i][j] = (90,90,90) 

start(e_map=e_map, bg_map=bg_map, bg=(255,255,255), actions_per_second=60, show_len=True)