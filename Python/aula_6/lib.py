import pygame
import sys
import inspect

PADDING_TOP = 40
SL = False

screen = None

pixel = None
width = None
height = None
aps = 60
ID = 0

clock = pygame.time.Clock()

__e_map = []
__bg_map = []
entities = {}

spawn_objs = []
spawn_pos = {}
kill_objs = {}
move_objs = {}
move_pos = {}

entities_count_surface = None

min_z = 0

bg_color = None
len_color = None

#=============================================LIB=INTERNAL======================================================

def __render():
    global screen, entities, entities_count_surface
    global __bg_map

    screen.fill(bg_color)

    # Background
    for y in range(height):
        for x in range(width):
            pygame.draw.rect(
                screen,
                __bg_map[y][x],
                (
                    x * pixel,
                    y * pixel + (PADDING_TOP if SL else 0),
                    pixel,
                    pixel
                )
            )
    
    # Entities
    for obj in sorted(entities.values(), key=lambda e: e['z']):
        pygame.draw.rect(
            screen,
            obj['color'],
            (
                obj['x'] * pixel,
                obj['y'] * pixel + (PADDING_TOP if SL else 0),
                pixel,
                pixel
            )
        )
    
    # Count
    if SL:
        screen.blit(entities_count_surface, (5, 5))

    pygame.display.flip()

def __move(obj):
    global move_objs

    if obj == None:
        return
    x = obj['x']
    y = obj['y']

    if x == None or x < 0 or x > width-1  or y == None  or y < 0  or y > height-1:
        return
    
    if (y in move_pos.keys() and move_pos[y][0] == x):
        return
    move_pos[y] = (x, obj['id'])
    move_objs[obj['id']] = obj

def __kill_for_real():
    global kill_objs, move_objs, __e_map

    for key, obj in kill_objs.items():
        
        x = obj['x']
        y = obj['y']

        __e_map[y][x] = None

        entities.pop(key, None)
        move_objs.pop(key, None)

    kill_objs = {}

def __spawn_for_real():
    global spawn_objs, min_z, spawn_pos, ID

    for obj in spawn_objs:
        y = obj['y']
        x = obj['x']

        if __e_map[y][x] != None:
            continue
    
        if obj.get('z') == None:
            obj['z'] = min_z-1
            min_z -= 1
        
        obj['id'] = ID
        __e_map[y][x] = obj
        entities[ID] = obj
        ID += 1

    spawn_objs = []
    spawn_pos = {}

def __move_for_real():
    global __e_map, entities, move_objs, move_pos

    for key, m in move_objs.items():
        if __e_map[m['y']][m['x']] != None and __e_map[m['y']][m['x']]['id'] != m['id']:# and (__e_map[m['y']][m['x']]['func'] != None) and (move_objs[__e_map[m['y']][m['x']]['id']]['y'] != entities[__e_map[m['y']][m['x']]['id']]['y'] and move_objs[__e_map[m['y']][m['x']]['id']]['x'] != entities[__e_map[m['y']][m['x']]['id']]['x']):
            
            m['y'] = entities[key]['y']
            m['x'] = entities[key]['x']



        x_, y_ = entities[key]['x'], entities[key]['y']
        __e_map[y_][x_] = None
        entities[key] = m
        __e_map[m['y']][m['x']] = entities[key]
    move_objs = {}
    move_pos = {}

def __loop():
    global entities, entities_count_surface

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
        return

    for key, e in entities.items():
        entities[key]['age'] += 1
        ent = entities[key].copy()
        if ent['func'] == None:
            continue
        
        args = [ent, __e_map, __bg_map, keys]
        sig = inspect.signature(ent['func'])
        n_params = len(sig.parameters)
        args = args[:n_params]
        ent['func'](*args)
        
        __move(ent)

    __kill_for_real()
    __move_for_real()
    __spawn_for_real()

    if SL:
        font = pygame.font.SysFont("Arial", PADDING_TOP // 3)
        text = f"Entities -> {len(entities)}"
        color = len_color if len_color else __inverted_color(bg_color)
        entities_count_surface = font.render(text, True, color)

    __render()

#=============================================LIB=UTILS======================================================

def __inverted_color(rgb):
    return (255-rgb[0],255-rgb[1],255-rgb[2])

#===========================================USER-FUNCTION====================================================

def get_map(w=30, h=30, px=15):

    global pixel, width, height
    
    pixel = px
    width = w
    height = h

    return [[None for x in range(width)] for y in range(height)]

def kill(obj):
    global kill_objs
    kill_objs[obj['id']] = obj

def spawn(obj):
    global spawn_objs
    if obj == None:
        return
    x = obj['x']
    y = obj['y']

    if x == None or x < 0 or x > width-1  or y == None  or y < 0  or y > height-1:
        return


    if y in spawn_pos and spawn_pos[y] == x:
        return
    spawn_pos[y] = x
    obj['age'] = 0
    
    spawn_objs.append(obj)

def get_key():
    return pygame

def start(e_map = None, bg_map = None, bg=(0,0,0), actions_per_second=60, show_len = False, l_color = None):
    global __e_map, __bg_map, entities, aps, ID
    global SL, screen

    global min_z, bg_color, len_color
    global PADDING_TOP

    SL = show_len
    bg_color = bg
    len_color = l_color

    pygame.init()

    aps = actions_per_second

    screen = pygame.display.set_mode(
        (width * pixel, height * pixel + (PADDING_TOP if SL else 0))
    )
    pygame.display.set_caption("Trueman")

    # Backgound
    __bg_map = [[bg for x in range(width)] for y in range(height)]
    if bg_map != None:
        for i in range(height):
            for j in range(width):
                if bg_map[i][j] != None:
                    __bg_map[i][j] = bg_map[i][j]
                
    # Entities
    __e_map = [[None for x in range(width)] for y in range(height)]
    if e_map != None:
        for i in range(height):
            for j in range(width):
                
                if(e_map[i][j] != None):
                    e = e_map[i][j]
                    e['y'] = i
                    e['x'] = j
                    e['age'] = 0
                    e['id'] = ID
                    entities[ID] = e
                    __e_map[i][j] = e
                    ID += 1

    # Iniciador
    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        __loop()
        clock.tick(aps)
