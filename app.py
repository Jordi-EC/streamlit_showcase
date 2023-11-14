import streamlit as st
import pandas as pd
import matplotlib as plt


print("hello world")

st.title("ñañaañ")

df = pd.read_csv("UCI_Credit_Card.csv")

st.dataframe(df)