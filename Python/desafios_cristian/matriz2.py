from teste.peak_lib import gen_peak

lines = 10
columns = 10
valor = 0

montanha = gen_peak(lines,columns,100)

for linhas in montanha:
    for colunas in linhas:
        if montanha[linhas][colunas] > valor:
            valor = montanha[linhas][colunas]
            
print(f"O maior valor é {valor}")
        