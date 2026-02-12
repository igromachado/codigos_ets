import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../CSVs/cat_breeds_clean.csv', sep=';')

df = df.groupby('Body_length').agg(
    mean_weight=('Weight', 'mean')
).reset_index()

plt.bar(df['Body_length'], df['mean_weight'])
plt.show()