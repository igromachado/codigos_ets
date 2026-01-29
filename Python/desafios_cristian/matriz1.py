from peak_lib import gen_peak

lines = 10
columns = 10

montanha = gen_peak(lines,columns,10)

maiorc = 0
maior = montanha[0][0]

for linha in range(len(montanha)):

    for coluna in range(len(montanha)):

        print(f'{montanha[linha][coluna]}', end= ' ')

    print()

for i in range(10):
    if montanha[0][i] > montanha[0][maiorc]:
        maiorc = i
    
maior_valor = montanha[0][maiorc]
        
for i in range(10):
    if montanha[i][maiorc] > maior_valor:
        maior_valor = montanha[i][maiorc]
        
print(maior)