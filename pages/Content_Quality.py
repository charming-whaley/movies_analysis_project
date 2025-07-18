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
