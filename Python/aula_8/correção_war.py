import random as rd

def war(defensores, atacantes):
    qtd_def = min(defensores, 6)
    qtd_ata = min(atacantes-1, 6)

    dados_def = []
    dados_ata = []
    for _ in range(qtd_def):
        dados_def.append(rd.randint(1,6))
    for _ in range(qtd_ata):
        dados_ata.append(rd.randint(1,6))

    dados_def.sort(reverse=True)
    dados_ata.sort(reverse=True)

    qtd = min(len(dados_def), len(dados_ata))
    for i in range(qtd):
        if dados_def[i] >= dados_ata[i]:
            atacantes -= 1
        if dados_def[i] < dados_ata[i]:
            defensores -= 1
    return defensores, atacantes

defensores_vitorias = 0
atacantes_vitorias = 0
batalhas = 1000


for i in range(batalhas):
    defensores = 500
    atacantes = 1000

    while defensores > 0 and atacantes > 1:
        defensores, atacantes = war(defensores, atacantes)

    if defensores > 0:
        defensores_vitorias += 1
    else:
        atacantes_vitorias += 1

print(f'Atacantes: {atacantes_vitorias/batalhas*100}%', end='')
print('\t|\t', end='')
print(f'Defensores: {defensores_vitorias/batalhas*100}%', end='')