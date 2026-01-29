linhas = 6
colunas = 10

def alguem_venceu(tabuleiro) -> bool:
    
    venceu = True
    
    for i in range(linhas):
        for j in range(colunas):
            x = [0, 1, 1, 1, 0, -1, -1, -1]
            y = [-1, -1, 0, 1, 1, 1, 0, -1]
            
            origem = tabuleiro[i][j]
            if origem == 0:            # <-- correção mínima: ignora células vazias
                continue
            for xi, yi in zip(x, y):
                pos_l = i
                pos_c = j
                venceu = True
                
                pos_l += yi
                pos_c += xi
                
                for k in range(3):
                    if pos_l < 0 or pos_l >= linhas or pos_c < 0 or pos_c >= colunas:
                        venceu = False
                        break
                    if tabuleiro[pos_l][pos_c] != origem:
                        venceu = False
                        break
                    pos_l += yi
                    pos_c += xi
                    
                if venceu:
                    return True
    return False

tabuleiro = [[0 for j in range(colunas)] for i in range(linhas)]

no_jogo = True
player = 1

while no_jogo:
    
    for linha in tabuleiro:
        print(linha)
        
    opcao = int(input('Escolha a coluna:\n>>'))
    
    for i in range(linhas-1, -1, -1):
        if tabuleiro[i][opcao] == 0:
            tabuleiro[i][opcao] = player
            break
        
    no_jogo = not alguem_venceu(tabuleiro)
    
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
