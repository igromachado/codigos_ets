import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return x**2
def g(x):
    return x**3


f_dominio = [i for i in range(-20, 21)]
f_imagem = [f(d) for d in f_dominio]
#===============alternativa====================
# f_d = []
# for i in range(-20, 21):
#     f_d.append(i)
#==============================================
g_dominio = [i for i in range(-20, 21)]
g_imagem = [g(d) for d in f_dominio]

fig, mtrz = plt.subplots(1, 2)
mtrz[0].plot(f_dominio, f_imagem)
mtrz[1].plot(g_dominio, g_imagem)

plt.show()