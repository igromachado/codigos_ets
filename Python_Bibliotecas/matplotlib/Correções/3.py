import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../CSVs/flights.csv', sep=',')
df = df[df['month'] == 'May']

plt.plot(df['year'], df['passengers'], marker='o')
plt.show()