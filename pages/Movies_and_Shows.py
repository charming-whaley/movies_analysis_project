import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

with st.sidebar:
    st.title("🎥 Movies vs. Shows")
    st.markdown("Movies vs. Shows battle never ends. On these page, I analyze the given data about movies & shows")

data = pd.read_csv("b.csv")
movies = data[data['type'] == 'MOVIE']
movies = movies[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]

shows = data[data['type'] == 'SHOW']
shows = shows[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]

st.title("First steps")
st.write("Before we start to analyze the data, we need to divide that into two categories: Movies and Shows. For this, I am going to do the following: ")
code = '''
movies = data[data['type'] == 'MOVIE'] # only movies data
shows = data[data['type'] == 'SHOW'] # only shows data

# A little bit of cleaning
movies = movies[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]
shows = shows[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]
'''
st.code(code, language='python')
st.write("After this, we obtain the following datasets, which are ready for analysis:")

st.text("Movies:")
movies

st.text("Shows:")
shows


def movies_analysis():
    pass

def shows_analysis():
    pass


categories = st.selectbox("Select necessary analysis", ["Movies", "Shows"])
if categories == "Movies":
    movies_analysis()
else:
    shows_analysis()
