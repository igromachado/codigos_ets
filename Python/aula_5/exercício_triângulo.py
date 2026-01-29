from lib import *

pixel = 10
altura = 20
largura = 20

background = get_map(largura,altura,pixel)

base_esquerda = int(input("Digite o início da base: "))
base_direita = int(input('Digite o final da base: '))

meio = base_direita - base_esquerda

start(bg_map=background)