import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\user\Downloads\imdb_top_1000.csv')

#Q1: most common genres
print("\nTop 10 Most Common Genres:")
print(df['Genre'].value_counts().head(10))

df['Genre'].value_counts().head(10).plot(kind='bar',title= 'Top 10 Most Common Genres')
plt.ylabel('Number of Movies')
plt.xlabel('Genre')
plt.tight_layout()
plt.savefig(r'C:\Users\user\Downloads\top_genres.png')
plt.show()

#Q2: the year with most movies
df['Released_Year']= pd.to_numeric(df['Released_Year'],errors ='coerce')
df = df.dropna(subset=['Released_Year'])
df['Released_Year']=df['Released_Year'].astype(int)

year_counts= df['Released_Year'].value_counts().sort_index()

plt.figure(figsize=(12,5))
ax = year_counts.plot(kind= 'bar', figsize=(12,5), title= 'Movies Released Per Year')
plt.ylabel('Number of Movies')
plt.xlabel('Year')

ax.set_xticks(range(0,len(year_counts),5))
ax.set_xticklabels(year_counts.index[::5],rotation=45)

plt.tight_layout()
plt.savefig(r'C:\Users\user\Downloads\movies_per_year.png')
plt.show()

#Q3: the genre with highest average rating
print("\nAverage IMDB Rating by Genre:")
avg_rating = df.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False)
print(avg_rating.head(10))

avg_rating.head(10).plot(kind='bar', title='Top 10 Genres by Average IMDB Rating', color= 'orange')
plt.ylabel('Average Rating')
plt.xlabel('Genre')
plt.tight_layout()
plt.savefig(r'C:\Users\user\Downloads\top_genre_ratings.png')
plt.show()