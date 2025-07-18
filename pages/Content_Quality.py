import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

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
