import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------
st.set_page_config(
    page_title="HCC Greenhouse Dashboard",
    page_icon="🌱",
    layout="wide"
)

# ---------------------------------------
# TITLE
# ---------------------------------------
st.title("🌱 HCC Greenhouse Environmental Dashboard")
st.markdown("Temperature and humidity monitoring for hydroponic towers")

# ---------------------------------------
# LOAD DATA
# ---------------------------------------
@st.cache_data

def load_data():
    df = pd.read_csv("data/greenhouse_readings.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


df = load_data()

# ---------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------
st.sidebar.header("Filters")

selected_towers = st.sidebar.multiselect(
    "Select Towers",
    options=df["tower"].unique(),
    default=df["tower"].unique()
)

filtered_df = df[df["tower"].isin(selected_towers)]

# ---------------------------------------
# METRICS
# ---------------------------------------
col1, col2 = st.columns(2)

avg_temp = filtered_df["temperature_c"].mean()
avg_humidity = filtered_df["humidity"].mean()

with col1:
    st.metric("Average Temperature (°C)", f"{avg_temp:.1f}")

with col2:
    st.metric("Average Humidity (%)", f"{avg_humidity:.1f}")

# ---------------------------------------
# TEMPERATURE GRAPH
# ---------------------------------------
st.subheader("Temperature Trends")

fig_temp = px.line(
    filtered_df,
    x="timestamp",
    y="temperature_c",
    color="tower",
    markers=True,
    title="Tower Temperatures"
)

st.plotly_chart(fig_temp, use_container_width=True)

# ---------------------------------------
# HUMIDITY GRAPH
# ---------------------------------------
st.subheader("Humidity Trends")

fig_humidity = px.line(
    filtered_df,
    x="timestamp",
    y="humidity",
    color="tower",
    markers=True,
    title="Tower Humidity"
)

st.plotly_chart(fig_humidity, use_container_width=True)

# ---------------------------------------
# RAW DATA
# ---------------------------------------
st.subheader("Raw Sensor Data")
st.dataframe(filtered_df, use_container_width=True)
