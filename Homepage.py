import streamlit as st
import pandas as pd

url = "https://www.kaggle.com/datasets/sufyan145/netflix-movies-and-shows-imdb-scores"

with st.sidebar:
    st.title("Homepage")
    st.markdown("Here you can find some info about the dataset and what I am going to analyze. To explore the dataset, please go to [Kaggle](%s)" % url)

st.title("Agenda")
st.write("Hi! I'm Fedya, and I'm a bit interested in Data Science & ML-engineering fields. Today, I'm going to analyze the Netflix Movies & Shows dataset. ")
st.write("Here's some info about it:")
data = pd.read_csv("b.csv")
st.write(data)

st.write("This is a little project for practice, so don't be sooo picky :)")

st.title("🌍 Socials")

st.write("Aw, almost forgot. You can find me here:")

first_url = "https://github.com/charming-whaley"
second_url = "https://www.codewars.com/users/charming_whaley"
third_url = "https://www.kaggle.com/fedyakatkov"
fourth_url = "www.linkedin.com/in/fskatkov"

st.write("[Github](%s) - Github with all projects" % first_url)
st.write("[Codewars](%s) - Codewars account" % second_url)
st.write("[Kaggle](%s) - Kaggle account with all badges and activity" % third_url)
st.write("[LinkedIn](%s) - LinkedIn account to hire me ;)" % fourth_url)
