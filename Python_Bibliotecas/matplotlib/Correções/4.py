import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('../CSVs/netflix_titles.csv', sep=',')

df = df.dropna()

df = df[
    (df['release_year'] >= 2015 )& 
    (df['release_year'] <= 2020) & 
    (df['type'] == 'Movie')  
]

usa_by_year = df[df['country'] == 'United States']
usa_by_year = usa_by_year.groupby('release_year').agg(
    total=('show_id', 'count')
).reset_index()

br_by_year = df[df['country'] == 'Brazil']
br_by_year['duration'] = br_by_year['duration'].str[:-3].astype(int)
br_by_year = br_by_year.sort_values(by='duration', ascending=False).head(5)


fig, mtrz = plt.subplots(1,2)
mtrz[0].bar(usa_by_year['release_year'], usa_by_year['total'])
mtrz[1].bar(br_by_year['title'], br_by_year['duration'])

plt.show()