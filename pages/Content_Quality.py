import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

with st.sidebar:
    st.title("⭐️ Content Quality")
    st.markdown("\"Old movies are better than modern ones\". On this page, I analyze if the quality of content increased/decreased")


data = pd.read_csv("b.csv")
movies = data[data['type'] == 'MOVIE']
movies = movies[['index', 'title', 'type', 'release_year', 'runtime', 'imdb_score', 'imdb_votes']]
movies = movies.sort_values(by='release_year')

shows = data[data['type'] == 'SHOW']
shows = shows[['index', 'title', 'type', 'release_year', 'runtime', 'imdb_score', 'imdb_votes']]
shows = shows.sort_values(by='release_year')

st.title("⭐️ Content Quality")
st.write("Before we start to analyze the data, we need to divide that into two categories: Movies and Shows. For this, I am going to do the following: ")

code = '''
movies = data[data['type'] == 'MOVIE']
movies = movies[['index', 'title', 'type', 'release_year', 'runtime', 'imdb_score', 'imdb_votes']]
movies = movies.sort_values(by='release_year')

shows = data[data['type'] == 'SHOW']
shows = shows[['index', 'title', 'type', 'release_year', 'runtime', 'imdb_score', 'imdb_votes']]
shows = shows.sort_values(by='release_year')'''
st.code(code, language='python')

st.text("Movies:")
movies

st.text("Shows:")
shows

st.title("Content production")
st.write("Let's first display how much content has been produced during the whole period of 1950-2022:")

movies_and_shows_comparison = data.groupby(['release_year', 'type']).size().reset_index(name='count')
figure = px.line(movies_and_shows_comparison, x='release_year', y='count', color='type', title='Movies and Shows quantity')
st.plotly_chart(figure, key="First chart")

st.write("As we can see from the line graph above, the quantity of movies produced by Netflix was much larger than the number of shows made in the same period. However, since the start of millenium period the quantity of shows made by Netflix significantly increased, which shows that nowadays people mostly prefer shows rather than movies")

st.write("Next, let's find top-10 content-production years during the whole period.")

movies_and_shows_comparison = data['release_year'].value_counts().nlargest(10).sort_index()
years = movies_and_shows_comparison.index.astype(str)
values = movies_and_shows_comparison.values

figure = go.Figure(data=[go.Bar(x=years, y=values, text=values, textposition="auto", marker=dict(color='lightblue'))])
figure.update_layout(
    title="Top 10 years by content quality",
    xaxis_title="Years",
    yaxis_title="Content quality"
)
st.plotly_chart(figure, key="Second chart")

st.write("Here, we can see that the period from 2017 to 2021 was the most productive for Netflix. This may be caused by the COVID-19 pandemic, as well as the decrease in Netflix prices and increase in popularity of streaming services")

st.title("Hypothesis")
st.write("We need to prove the following hypothesis: is it true that for the last couple of years, the quantity of content produced by Neflix significantly increased?")

st.write("Let's come back to the data obtained during the research above. We can clearly see that from 2017 to 2021 the number of movies/shows increased significantly which caused by the COVID-19 pandemic and the tendency of remote work. Also, this may happen due to the fact that the opportunity to get content online has become more available for people")

st.title("Content duration")
st.write("In the end, let's check Netflix production strategy. For this, ")

new_data = data[['runtime', 'release_year']].dropna()
X = StandardScaler().fit_transform(new_data)

kmeans = KMeans(n_clusters=3, random_state=42)
new_data['cluster'] = kmeans.fit_predict(X)
figure = px.scatter(
    new_data,
    x='release_year',
    y='runtime',
    color='cluster',
    title='Content duration cluster',
    labels={
        'release_year': 'Release year', 
        'runtime': 'Duration (minutes)'
    },
    color_continuous_scale='viridis'
)

st.plotly_chart(figure, key="Third chart")
