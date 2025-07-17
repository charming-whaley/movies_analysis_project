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
shows = shows.sort_values(by='release_year')'''
st.code(code, language='python')
st.write("After this, we obtain the following datasets, which are ready for analysis:")

st.text("Movies:")
movies

st.text("Shows:")
shows

st.title("Each analysis separately")
st.write("Now you can choose whatever analysis you want:")

def movies_analysis():
    before_millenium_period = movies[movies['release_year'] < 2000]
    tens_period = movies[movies['release_year'].between(2000, 2010)].copy()
    modern_period = movies[movies['release_year'] > 2010]

    median_before_millenium_period = before_millenium_period['imdb_score'].median()
    median_tens_period = tens_period['imdb_score'].median()
    median_modern_period = modern_period['imdb_score'].median()

    mean_before_millenium_period = before_millenium_period['imdb_score'].mean()
    mean_tens_period = tens_period['imdb_score'].mean()
    mean_modern_period = modern_period['imdb_score'].mean()

    st.title("Agenda")
    st.write("In this section, I am going to analyze the necessary stuff for the future hypothesis.")

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

    st.title("Mean & Median")
    st.write("Now we are to find the mean and median value of three periods: before 2000s, between 2000 and 2010, and 2010 and modern days. I made for clarity to actually see how the IMDB score has been during the whole period")

    st.write("Here is the code for each period:")
    code = '''
before_millenium_period = movies[movies['release_year'] < 2000]
tens_period = movies[movies['release_year'].between(2000, 2010)].copy()
modern_period = movies[movies['release_year'] > 2010]'''
    st.code(code, language='python')

    st.write("We first compute median value:")
    code = '''
median_before_millenium_period = before_millenium_period['imdb_score'].median()
median_tens_period = tens_period['imdb_score'].median()
median_modern_period = modern_period['imdb_score'].median()'''
    st.code(code, language='python')

    st.write("Next we compute mean value:")
    code = '''
mean_before_millenium_period = before_millenium_period['imdb_score'].mean()
mean_tens_period = tens_period['imdb_score'].mean()
mean_modern_period = modern_period['imdb_score'].mean()'''
    st.code(code, language='python')

    st.write("Here you can find the bar chart that displays the division of each period in percentage")
    figure = px.pie(
        names=['Before millenium', 'Tens', 'Modern days'], 
        values=[median_before_millenium_period, median_tens_period, median_modern_period],
        title='Medians',
        hole=0
    )
    st.plotly_chart(figure, key="Second chart")

    figure = px.pie(
        names=['Before millenium', 'Tens', 'Modern days'], 
        values=[mean_before_millenium_period, mean_tens_period, mean_modern_period],
        title='Medians',
        hole=0
    )
    st.plotly_chart(figure, key="Third chart")

    st.write("Here is a more detailed version of Mean & Medians comparison using the table:")
    st.dataframe(
        pd.DataFrame({
            "Before 2000s": [median_before_millenium_period, mean_before_millenium_period],
            "Between 2000 and 2010": [median_tens_period, mean_tens_period],
            "After 2010s": [median_modern_period, mean_modern_period]
        }, index=["Median", "Mean"])
    )


def shows_analysis():
    before_millenium_period = shows[shows['release_year'] < 2000]
    tens_period = shows[shows['release_year'].between(2000, 2010)].copy()
    modern_period = shows[shows['release_year'] > 2010]

    median_before_millenium_period = before_millenium_period['imdb_score'].median()
    median_tens_period = tens_period['imdb_score'].median()
    median_modern_period = modern_period['imdb_score'].median()

    mean_before_millenium_period = before_millenium_period['imdb_score'].mean()
    mean_tens_period = tens_period['imdb_score'].mean()
    mean_modern_period = modern_period['imdb_score'].mean()

    st.title("Agenda")
    st.write("In this section, I am going to analyze the necessary stuff for the future hypothesis.")

    st.title("IMDB scores tendency")
    st.write("First things first, let's see how the average IMDB score change during the whole period of shows production on Netflix:")

    unique_shows = shows.drop_duplicates(subset="imdb_score", keep='first').reset_index(drop=True)
    figure = px.line(unique_shows, x="release_year", y="imdb_score", title="Average IMDB score each year")
    slope, intercept = np.polyfit(unique_shows['release_year'], unique_shows['imdb_score'], 1)
    figure.add_trace(go.Scatter(
        x=unique_shows['release_year'],
        y=slope * unique_shows['release_year'] + intercept,
        mode='lines',
        name='Decreasing tendency',
        line=dict(color='white')
    ))
    st.plotly_chart(figure, key="First chart")

    st.write("As we can see, since 1960s the average IMDB score of movies completely felt. This may caused by the poor quality of shows made by Netflix studios")

    st.title("Mean & Median")
    st.write("Now we are to find the mean and median value of three periods: before 2000s, between 2000 and 2010, and 2010 and modern days. I made for clarity to actually see how the IMDB score has been during the whole period")


categories = st.selectbox("Select what you need", ["Movies", "Shows"])
if categories == "Movies":
    movies_analysis()
else:
    shows_analysis()
