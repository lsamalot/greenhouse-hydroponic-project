import pandas as pd


def load_sensor_data(path="data/greenhouse_readings.csv"):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df