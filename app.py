import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Used Car Advertisement Data Set')

st.dataframe(df)

# Scatterplot
df_filtered = df[df['price'] < 300000]

st.header('Price vs. Odometer by Vehicle Type (Outliers Removed)')
fig = px.scatter(df_filtered, x='odometer', y='price', color='type', height=600, width=600)
st.write(fig)

# Histogram
st.header('How long are cars typically listed?')
fig = px.histogram(df, x='days_listed', color='condition')
st.write(fig)

print(df.columns)