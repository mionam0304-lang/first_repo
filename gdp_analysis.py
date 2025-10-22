# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 20:22:59 2025

@author: miona
"""
import sys
from data import read_data, clean_data, plot_data

df = read_data("data.csv")
df_c_dict = clean_data(df)

for key in df_c_dict.keys():
    plot_data(df_c_dict,key)