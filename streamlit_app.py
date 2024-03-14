import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import pickle
import datetime

model = pickle.load(open('model.pkl', 'rb'))

# Icon and Title
image = Image.open("./assets/icons8-car-100.png")
st.set_page_config(
    page_icon=image,
    page_title="Car Price Predict"
)

st.title("Car Price Prediction")

# Hide "Made with streamlit"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

Year = st.text_input('Which year model lanuch?', '')
Present_Price = st.text_input('Currently, how many price of car?', '')
Kms_Driven = st.text_input('How many car has driven? (KM)', '')
Owner = st.selectbox("Number of owner?", (0, 1, 2, 3, 4))
Fuel_Type_Petrol = st.selectbox("Fuel Type", ('Petrol', 'Diesel', 'CNG'))
Seller_Type_Individual = st.selectbox("Seller type?", ('Dealer', 'Individual'))
Transmission_Mannual = st.selectbox(
    "Transmission type?", ('Manual', 'Automatic'))
# Kms_Driven2 = np.log(Kms_Driven, dtype=int)

Fuel_Type_Diesel = 0
if (Fuel_Type_Petrol == 'Petrol'):
    Fuel_Type_Petrol = 1
    Fuel_Type_Diesel = 0
else:
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 1

# current_year = int(datetime.datetime.now())
# Year = current_year.year - int(Year)

if (Seller_Type_Individual == 'Individual'):
    Seller_Type_Individual = 1
else:
    Seller_Type_Individual = 0

# Transmission type (Mannual or Automatic)
if (Transmission_Mannual == 'Mannual'):
    Transmission_Mannual = 1
else:
    Transmission_Mannual = 0


def predict_car_price():
    data = [[Year, Present_Price, Kms_Driven, Owner, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]]
    pred = model.predict(data)
    price = f"Car price is: {round(pred[0], 2)} lakh"
    return price


if st.button("Predict Car Price"):
    st.header(predict_car_price())
