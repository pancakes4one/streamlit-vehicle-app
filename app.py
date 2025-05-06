import streamlit as st
import pandas as pd
import plotly_express as px


df = pd.read_csv('vehicles_us.csv')

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Data Viewer')

st.dataframe(df)