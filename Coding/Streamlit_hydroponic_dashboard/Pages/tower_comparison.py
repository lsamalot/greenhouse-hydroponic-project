import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Tower Comparison")

# Load Data

df = pd.read_csv("data/greenhouse_readings.csv")

# Average temperature per tower

avg_temp = (
    df.groupby("tower")["temperature_c"]
    .mean()
    .reset_index()
)

fig = px.bar(
    avg_temp,
    x="tower",
    y="temperature_c",
    title="Average Temperature by Tower"
)

st.plotly_chart(fig, use_container_width=True)