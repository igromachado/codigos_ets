'''
=============================================
Desenvolva uma maneira de encontrar onde 
está o maior valor da matriz.

Exiba o indice de linha e coluna onde o
maior valor se encontra
=============================================
'''

from peak_lib import gen_peak

lines = 10
columns = 10
valor = 0

montanha = gen_peak(lines,columns,100)
for linha in range(len(montanha)):

    for coluna in range(len(montanha)):

        print(f'{montanha[linha][coluna]}', end= ' ')

    print()
    
i = 0
for linhas in montanha:
    j = 0
    for colunas in linhas:
        if colunas > valor:
            valor = colunas
            pos = (i,j)
        j += 1
    i += 1
            
print(f"Sua posição é {pos}, e o maior valor da matriz é {valor}")