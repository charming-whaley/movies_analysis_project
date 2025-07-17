import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

with st.sidebar:
    st.title("🎥 Movies vs. Shows")
    st.markdown("Movies vs. Shows battle never ends. On these page, I analyze the given data about movies & shows")

data = pd.read_csv("b.csv")

st.title("First steps")
st.write("Before we start to analyze the data, we need to divide that into two categories: Movies and Shows:")


def movies_analysis():
    pass

def shows_analysis():
    pass


categories = st.selectbox("Select necessary analysis", ["Movies", "Shows"])
if categories == "Movies":
    movies_analysis()
else:
    shows_analysis()
