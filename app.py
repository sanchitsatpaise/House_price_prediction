# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:34:06 2025

@author: Sanchit Satpaise
"""

import streamlit as st
import joblib
import numpy as np

model=joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house. For using this app you can enter the inputs from this UI and then use predict button")

st.divider()

bedrooms = st.number_input("Number of Bedrooms(1-33)", min_value=0,value=0)
bathrooms = st.number_input("Number of Bathrooms(0-8)", min_value=0,value=0)
livingarea = st.number_input("Living area (370-13540)", min_value=0,value=0)
condition = st.number_input("Condition(0-5)", min_value=0,value=0)
numberofschools = st.number_input("Number of schools nearby(1-3)", min_value=0,value=0)

st.divider()

x=[[bedrooms,bathrooms,livingarea,condition,numberofschools]]

predictbutton = st.button("Predict Price!")

if predictbutton:
    st.balloons()
    x_array = np.array(x)
    prediction = model.predict(x_array)
    
    st.write(f"Price prediction is {prediction}")
    
else:
    st.write("Please use predict button after entering values")