import streamlit as st
import pandas as pd
import numpy as np





st.title("Police Incident Reports from 2018 to 2020 in San Francisco")

df = pd.read_csv("Policev1.csv")

df

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with each case such as date, day of the week police district, neighborhood in which it happened...')

mapa=pd.DataFrame()
mapa['Date']=df['Incident Date']
mapa['Day']=df['Indicent Day of Week']
mapa['Police District']=df['Police district']
mapa['Neighborhood']=df['Analysis Neighborhood']
mapa['Incident Category']= df['Incident Category']
mapa['Incident Subcategory']=df['Incident Subcategory']
mapa['Resolution']=df['Resolution']
mapa['lat']=df['Latitude']
mapa['lon']=df['Longitude']
mapa=mapa.dropna()

subset_data2=mapa
police_district_input=st.sidebar.multiselect('Police District', mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input>0:
  subset_data2=mapa[mapa['Police District'].isin(police_district_input)]

