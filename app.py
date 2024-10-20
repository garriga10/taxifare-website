import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np

st.set_page_config(
    page_title= "TaxiFare", # => Quick reference - Streamlit
    page_icon= "🐍",
    layout= "wide", # wide
    initial_sidebar_state= "auto") # collapsed

'''
# Taxi Fare
'''

with st.sidebar:
    with st.form(key= 'params_for_api'):

        pickup_date = st.date_input('pickup datetime')
        pickup_time = st.time_input('pickup datetime')
        pickup_datetime = f'{pickup_date} {pickup_time}'
        pickup_longitude = st.number_input('pickup longitude', value= 40.7614327)
        pickup_latitude = st.number_input('pickup latitude', value= -73.9798156)
        dropoff_longitude = st.number_input('dropoff longitude', value =40.6413111)
        dropoff_latitude = st.number_input('dropoff latitude', value= -73.7803331)
        passenger_count = st.number_input('passenger_count', min_value= 1, max_value= 8, step= 1, value= 1)

        st.form_submit_button('Submit')


params = dict(
    pickup_datetime= pickup_datetime,
    pickup_longitude= pickup_longitude,
    pickup_latitude= pickup_latitude,
    dropoff_longitude= dropoff_longitude,
    dropoff_latitude= dropoff_latitude,
    passenger_count= passenger_count)

wagon_cab_api_url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(wagon_cab_api_url, params= params)

prediction = response.json()

pred = prediction['fare']

st.header(f'Fare amount: ${round(pred, 2)}')

def get_map_data(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude):
    data = {
        'lon': [pickup_longitude, dropoff_longitude],
        'lat': [pickup_latitude, dropoff_latitude]
    }
    df = pd.DataFrame(data)
    return df

df = get_map_data(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude)

st.map(df)
