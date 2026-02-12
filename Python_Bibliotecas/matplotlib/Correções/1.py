import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../CSVs/gols_pr.csv', sep=',')

athletico = df[df['clube'] == 'athletico-pr']
parana = df[df['clube'] == 'parana']
coritiba = df[df['clube'] == 'coritiba']

plt.plot(athletico['ano'], athletico['gols_pro'], marker='o')
plt.plot(parana['ano'], parana['gols_pro'], marker='o')
plt.plot(coritiba['ano'], coritiba['gols_pro'], marker='o')

plt.xticks(df['ano'])

plt.legend()

plt.grid(True)

plt.show()