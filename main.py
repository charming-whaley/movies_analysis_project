import streamlit as st

url = "https://www.kaggle.com/datasets/sufyan145/netflix-movies-and-shows-imdb-scores"

with st.sidebar:
    st.title("Homepage")
    st.markdown("Here you can find some info about the dataset and what I am going to analyze. To explore the dataset, please go to [Kaggle](%s)" % url)