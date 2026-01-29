def chamar_matriz():
    return [[0 for _ in range(7)] for _ in range(7)]

    
def mostrar_matriz(matriz):
    print("|1|2|3|4|5|6|7|")
    for linha in matriz:
        for celula in linha:
            if celula == 0:
                print("|_",end="")
            elif celula == 1:
                print("|X",end="")
            elif celula == 2:
                print("|O",end="")
        print("|")
    print()


    
    
    
        
    
    


