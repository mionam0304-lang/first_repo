# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 15:53:49 2025

@author: miona
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

###read data
def read_data(filename) -> pd.DataFrame:
    df = pd.read_csv("data.csv")
    return df

###clean data
def clean_data(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    df_c = df[["Reference area","TIME_PERIOD","OBS_VALUE"]] #necessarily columns only
    df_c = df_c.sort_values("TIME_PERIOD")
    df_c_dict = dict(tuple(df_c.groupby("Reference area")))
    return df_c_dict

###plot data
def plot_data(df_dict: dict[str, pd.DataFrame], country: str):
    data = df_dict[country]
    plt.plot(data["TIME_PERIOD"], data["OBS_VALUE"])
    plt.title(country)
    plt.ylabel("GDP_growh")
    
    plt.xticks(
    data["TIME_PERIOD"][::8],
    [str(x)[:4] for x in data["TIME_PERIOD"][::8]],  # ← 先頭4文字だけ表示
    rotation=45, ha="right"
    )
    
    plt.tight_layout()
    
    plt.show()

