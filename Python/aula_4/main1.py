import math 
# Crie uma função "bhaskara()", que recebe a,b,c, e 
# retorna os dois resultados possíveis da equação de 
# bhasakara (retorna "i", caso dê um número imaginário)

# --------EXEMPLO--------
def f(x):
    return 2 * x + 7

def bhaskara(a,b,c):
    
    delta = (b*b) - (4 * a * c)
    
    resultado1 = ((-1 * b) + (delta ** 0,5)) / (2 * a)
    resultado2 = ((-1 * b) - (delta ** 0,5)) / (2 * a)
    
    return f"Resultado 1: {resultado1} \nResultado 2: {resultado2}"
    
r = bhaskara(2,4,-6)

a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

print(bhaskara(a,b,c)) # esperado -> (1.0, -3.0)