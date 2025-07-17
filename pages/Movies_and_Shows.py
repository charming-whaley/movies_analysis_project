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
movies = movies.sort_values(by='release_year')

shows = data[data['type'] == 'SHOW']
shows = shows[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]
shows = shows.sort_values(by='release_year')

st.title("First steps")
st.write("Before we start to analyze the data, we need to divide that into two categories: Movies and Shows. For this, I am going to do the following: ")
code = '''
movies = data[data['type'] == 'MOVIE']
movies = movies[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]
movies = movies.sort_values(by='release_year')

shows = data[data['type'] == 'SHOW']
shows = shows[['index', 'title', 'type', 'release_year', 'imdb_score', 'imdb_votes']]
shows = shows.sort_values(by='release_year')
'''
st.code(code, language='python')
st.write("After this, we obtain the following datasets, which are ready for analysis:")

st.text("Movies:")
movies

st.text("Shows:")
shows

st.title("Each analysis separately")
st.write("Now you can choose whatever analysis you want:")

def movies_analysis():
    st.title("Agenda")
    st.write("In this section, I am going to analyze the necessary stuff for the future hypothesis. I divided each item with Roman numbers (I., II., III. ...)")

    st.title("IMDB scores tendency")
    st.write("First things first, let's see how the average IMDB score change during the whole period of movies production on Netflix:")

    unique_movies = movies.drop_duplicates(subset="imdb_score", keep='first').reset_index(drop=True)
    figure = px.line(unique_movies, x="release_year", y="imdb_score", title="Average IMDB score each year")
    slope, intercept = np.polyfit(unique_movies['release_year'], unique_movies['imdb_score'], 1)
    figure.add_trace(go.Scatter(
        x=unique_movies['release_year'],
        y=slope * unique_movies['release_year'] + intercept,
        mode='lines',
        name='Decreasing tendency',
        line=dict(color='white')
    ))
    st.plotly_chart(figure, key="First chart")
    st.write("As we can see, since 1960s the average IMDB score of movies felt significantly. This may caused by the poor quality of movies made by Netflix studios")


def shows_analysis():
    pass


categories = st.selectbox("Select what you need", ["Movies", "Shows"])
if categories == "Movies":
    movies_analysis()
else:
    shows_analysis()
