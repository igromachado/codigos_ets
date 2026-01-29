from lib import *

pixel = 10
altura = 40
largura = 40

background = get_map(largura,altura,pixel)

# x1 = int(input("Digite o ponto inicial: "))
# if x1 > 39:
#     diferença = x1 - 39
#     x1 = x1 - diferença
# y1 = x1

# x2 = int(input("Digite o ponto final: "))
# if x2 > 39:
#     diferença = x2 - 39
#     x2 = x2 - diferença
# y2 = x2

x1 = int(input("Digite a linha inicial: "))
x2 = int(input("Digite a linha final: "))
y1 = int(input("Digite a coluna inicial: "))
y2 = int(input("Digite a coluna final: "))

def quadrado_vazado(y1,y2,x1,x2):

    for i in range(y1,y2+1):
        background[i][y1] = (255,0,255)
        background[i][y2] = (255,0,255)
        
    for i in range(x1,x2+1):
        background[x1][i] = (255,0,0)
        background[x2][i] = (255,0,0)
    
    start(bg_map=background)

# quadrado_vazado(y1,y2,x1,x2)
        

def quadrado_preenchido(y1,y2,x1,x2):

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            background[i][j] = (255,0,255)
        
    start(bg_map=background)

quadrado_preenchido(y1,y2,x1,x2)