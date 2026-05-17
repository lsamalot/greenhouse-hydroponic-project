import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Historical Trends")

# Load data

df = pd.read_csv("data/greenhouse_readings.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Daily averages

df["date"] = df["timestamp"].dt.date

avg_daily = (
    df.groupby("date")[["temperature_c", "humidity"]]
    .mean()
    .reset_index()
)

fig = px.line(
    avg_daily,
    x="date",
    y="temperature_c",
    title="Average Daily Temperature"
)

st.plotly_chart(fig, use_container_width=True)