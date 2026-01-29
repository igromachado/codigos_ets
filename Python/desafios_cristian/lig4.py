# Função para criar o tabuleiro
def criar_matriz():
    return [[0 for _ in range(6)] for _ in range(7)]  # 7 linhas, 6 colunas

# Função para mostrar o tabuleiro na tela
def mostrar_matriz(matriz):
    print("\n|1|2|3|4|5|6|")
    for linha in matriz:
        for celula in linha:
            if celula == 0:
                print("|_", end="")
            elif celula == 1:
                print("|X", end="")  # Jogador 1
            elif celula == 2:
                print("|O", end="")  # Jogador 21
        print("|")
    print()  # Linha em branco

# Função para colocar a peça em uma coluna
def jogar(matriz, coluna, jogador):
    # coluna vem como 1–6, mas o índice começa em 0
    coluna -= 1
    # Procurar a posição mais baixa (de baixo pra cima)
    for i in range(6, -1, -1):  # começa do fim
        if matriz[i][coluna] == 0:
            matriz[i][coluna] = jogador
            return True
    return False  # se a coluna estiver cheia

# Função para verificar vitória
def verificar_vitoria(matriz, jogador):
    # Horizontal
    for i in range(7):
        for j in range(3):
            if (matriz[i][j] == jogador and
                matriz[i][j+1] == jogador and
                matriz[i][j+2] == jogador and
                matriz[i][j+3] == jogador):
                return True

    # Vertical
    for i in range(4):
        for j in range(6):
            if (matriz[i][j] == jogador and
                matriz[i+1][j] == jogador and
                matriz[i+2][j] == jogador and
                matriz[i+3][j] == jogador):
                return True

    # Diagonal ↘
    for i in range(4):
        for j in range(3):
            if (matriz[i][j] == jogador and
                matriz[i+1][j+1] == jogador and
                matriz[i+2][j+2] == jogador and
                matriz[i+3][j+3] == jogador):
                return True

    # Diagonal ↙
    for i in range(3, 7):
        for j in range(3):
            if (matriz[i][j] == jogador and
                matriz[i-1][j+1] == jogador and
                matriz[i-2][j+2] == jogador and
                matriz[i-3][j+3] == jogador):
                return True

    return False

# -------- PROGRAMA PRINCIPAL --------
matriz = criar_matriz()
game_over = False
jogador = 1

while not game_over:
    mostrar_matriz(matriz)
    jogada = int(input(f"Jogador {jogador}, escolha uma coluna (1-6): "))

    if jogar(matriz, jogada, jogador):
        if verificar_vitoria(matriz, jogador):
            mostrar_matriz(matriz)
            print(f"Jogador {jogador} venceu!")
            game_over = True
        else:
            # Alternar jogador
            jogador = 2 if jogador == 1 else 1
    else:
        print("Coluna cheia! Tente outra.")
