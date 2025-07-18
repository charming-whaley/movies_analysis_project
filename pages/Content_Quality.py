import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

with st.sidebar:
    st.title("⭐️ Content Quality")
    st.markdown("\"Old movies are better than modern ones\" — or are they? In this dashboard, we explore how the quality and quantity of Netflix content have evolved over time.")


data = pd.read_csv("b.csv")
movies = data[data['type'] == 'MOVIE']
movies = movies[['index', 'title', 'type', 'release_year', 'runtime', 'imdb_score', 'imdb_votes']]
movies = movies.sort_values(by='release_year')

shows = data[data['type'] == 'SHOW']
shows = shows[['index', 'title', 'type', 'release_year', 'runtime', 'imdb_score', 'imdb_votes']]
shows = shows.sort_values(by='release_year')

st.title("⭐️ Content Quality")
st.write("To begin our analysis, we first separate the dataset into two distinct content types: movies and TV shows. This allows us to explore trends more precisely for each format.")

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
st.write("Let’s start by examining the volume of Netflix content produced annually between 1950 and 2022.")

movies_and_shows_comparison = data.groupby(['release_year', 'type']).size().reset_index(name='count')
figure = px.line(movies_and_shows_comparison, x='release_year', y='count', color='type', title='Movies and Shows quantity')
st.plotly_chart(figure, key="First chart")

st.write("The line chart above shows that historically, Netflix produced significantly more movies than shows. However, starting in the early 2000s, the number of TV shows began to rise sharply. This shift likely reflects changing viewer preferences and Netflix's strategic expansion into serialized content.")

st.write("Next, we identify the top 10 years with the highest volume of content production.")

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

st.write("The chart shows that the years 2017–2021 were particularly productive for Netflix. This surge may be attributed to increased demand during the COVID-19 pandemic, the rise of streaming services, and Netflix's global expansion strategy.")

st.title("Hypothesis")
st.write("Let’s test the hypothesis: Has Netflix significantly increased its content production in recent years?")
st.write("Returning to our previous findings, it’s evident that content production spiked between 2017 and 2021. This growth may be linked to the pandemic-driven shift toward remote work and the increased accessibility of digital content platforms.")

st.title("Content duration")
st.write("In the final part of our analysis, we examine the evolution of Netflix's content production strategy by clustering the content based on its duration and release year. This helps us identify potential shifts in format preferences over time — for example, the transition from full-length movies to shorter series or vice versa.")

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

st.write("This clustering confirms that Netflix has shifted from primarily offering full-length movies to a more diverse content portfolio, including shorter and mid-length productions. The expansion reflects evolving viewer habits and Netflix’s adaptive content strategy in the streaming age.")
