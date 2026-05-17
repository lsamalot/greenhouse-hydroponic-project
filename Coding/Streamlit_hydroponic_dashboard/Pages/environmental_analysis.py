import streamlit as st
import pandas as pd

st.title("Environmental Analysis")

# Load data

df = pd.read_csv("data/greenhouse_readings.csv")

# Define thresholds

HIGH_TEMP = 32
HIGH_HUMIDITY = 80

# Analyze

high_temp_events = df[df["temperature_c"] > HIGH_TEMP]
high_humidity_events = df[df["humidity"] > HIGH_HUMIDITY]

# Display

st.subheader("High Temperature Events")
st.dataframe(high_temp_events)

st.subheader("High Humidity Events")
st.dataframe(high_humidity_events)