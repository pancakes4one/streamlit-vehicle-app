import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['odometer'] = pd.to_numeric(df['odometer'], errors='coerce')
df = df[df['price'].notna() & df['odometer'].notna()]

st.header('Used Car Advertisement Data Set')
st.dataframe(df)

# Scatterplot
df_filtered = df[df['price'] < 80000]

st.header('Price vs. Odometer by Vehicle Type')

remove_outliers = st.checkbox('Exclude sale prices greater than 80,000)', value=True)

if remove_outliers:
    df_filtered = df[(df['price'] < 80000) & (df['odometer'].notna()) & (df['price'].notna())]
else:
    df_filtered = df[df['odometer'].notna() & df['price'].notna()]

fig = px.scatter(df_filtered, x='odometer', y='price', color='type', height=600, width=600)
st.write(fig)

# Histogram
filter_long = st.checkbox('Exclude listings over 100 days', value=True)

if filter_long:
    df_filtered = df[df['days_listed'] < 100]
else:
    df_filtered = df.copy()

st.header('Days Listed Distibution')
fig = px.histogram(df_filtered, x='days_listed', color='condition')
st.plotly_chart(fig)