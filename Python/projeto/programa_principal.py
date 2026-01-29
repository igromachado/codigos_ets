from main import *
from ascii_pokemons import *

print("-=-="*8, "BEM VINDO A POKEDEX", "-=-="*8, "\n\n-=- POKÉMONS -=-\n 1 = Bulbasaur\n 2 = Charmander\n 3 = Squirtle\n")
escolha = int(input("Escolha um Pokemon: "))

if escolha == 1:
    print("-=-="*4, " -BULBASAUR- ", "-=-="*4)
    printar_pokemon(bulbasaur)
    pokemon_selecionado = Bulbasaur

elif escolha == 2:
    print("-=-="*4, " -CHARMANDER- ", "-=-="*4)
    printar_pokemon(charmander)
    pokemon_selecionado = Charmander

elif escolha == 3:
    print("-=-="*4, " -SQUIRTLE- ", "-=-="*4)
    printar_pokemon(squirtle)
    pokemon_selecionado = Squirtle

else:
    print("Algo deu errado!!!")

level = input("Digite o nível desejado para o Pokémon (1 a 15):\n>> ")
try:
    level = int(level)
    if not (level >= 1 and level <= 15):
        raise ValueError('Valor excede o nível maximo!')
except ValueError as e: 
    print(e)

#printa o status do nível desejado
hp, ataque, defesa, velocidade = printar_status(pokemon_selecionado, level)

#mostra as opções de ataque do usuário
verifica = True

while verifica == True:
    print("-=-="*4, " -ATAQUES- ", "-=-="*4)
    auxiliar = 0
    for i in pokemon_selecionado['Ataques']:
        auxiliar+=1
        print(f"{auxiliar} - {i}")

    #usuário dá o input de qual ataque deseja
    print("-=-="*4, " -SELEÇÃO- ", "-=-="*4)
    selecionar_ataque = int(input("Selecione o ataque:\n>> "))

    #verifica qual ataque foi selecionado
    contador = 0
    for i in pokemon_selecionado["Ataques"]:
        contador += 1
        if contador == selecionar_ataque:
            ataque_selecionado = i

    #mostra os status do ataque selecionado
    for nome_ataque, descricao in Ataques.items():
        if ataque_selecionado == nome_ataque:
            print("-=-="*4, " -STATUS- ", "-=-="*4)
            if len(descricao) == 5:
                print(f"Nome: {nome_ataque}\nTipo: {descricao['Tipo']}\nPoder: {descricao['Poder']}\nPrecisão: {descricao['Precisão']}\nPP:{descricao['PP']}\nDescrição: {descricao['Descrição']}\n")
            elif len(descricao) == 6:
                 print(f"Nome: {nome_ataque}\nTipo: {descricao['Tipo']}\nPoder: {descricao['Poder']}\nPrecisão: {descricao['Precisão']}\nPP:{descricao['PP']}\nDescrição: {descricao['Descrição']}\nEfeito adicional: {descricao['Efeito adicional']}\n")
            opção = int(input("Deseja visualizar outro ataque?\n1 - Sim\n2 - Não\n>> "))

            if opção == 1:
                True
            if opção == 2:
                verifica = False
                break

print("É ISSO. Status do Pokemon salvo com sucesso!")

textoParaSalvar = "Nome Pokemon: %s\nNível: %s\n\nHP: %s\nAtaque: %s\nDefesa: %s\nVelocidade: %s\nTipo: %s\nAtaques: %s" % (pokemon_selecionado['Nome Pokemon'], level, hp, ataque, defesa, velocidade, pokemon_selecionado['Tipo'], pokemon_selecionado['Ataques'])

with open("Status do Pokemon.TXT", 'w')  as arquivo:
    arquivo.write(textoParaSalvar)