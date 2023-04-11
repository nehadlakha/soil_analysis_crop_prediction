import streamlit as st
import pickle
import numpy as np

#st.markdown("# SOIL ANALYSIS")


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        dataa = pickle.load(file)
    return dataa


dataa = load_model()

classifierr = dataa["model"]


def soil_analytics():
    st.header("SOIL ANALYSIS")

    st.write("""Enter the details:""")

    N = st.number_input("Sodium")
    P = st.number_input("Phosphorous")
    K = st.number_input("Potassium")
    temperature = st.number_input("Temperature")
    humidity = st.number_input("humidity")
    ph = st.number_input("pH")
    rainfall = st.number_input("Rainfall")
    crop = st.text_input("CROP ")

    ok = st.button("Submit")

    if(ok):
        a = classifierr.predict([[N, P, K, temperature, humidity, rainfall]])
        st.header(
            "  ACCORDING TO THE MENTIONED SOIL CONDITIONS THE MOST SUITABLE CROP TO BE GROWN IS  ")
        a = classifierr.predict([[N, P, K, temperature, humidity, rainfall]])
        # st.write(a)
        if(a == 0):
            st.write('APPLE')
        if(a == 1):
            st.write('BANANA')
        if(a == 2):
            st.write('BLACKGRAM')
        if(a == 3):
            st.write('CHICKPEA')
        if(a == 4):
            st.write('COCONUT')
        if(a == 5):
            st.write('COFFEE')
        if(a == 6):
            st.write('COTTON')
        if(a == 7):
            st.write('GRAPES')
        if(a == 8):
            st.write('JUTE')
        if(a == 9):
            st.write('KIDNEYBEANS')
        if(a == 10):
            st.write('LENTIL')
        if(a == 11):
            st.write('MAIZE')
        if(a == 12):
            st.write('MANGO')
        if(a == 13):
            st.write('MOTHBEANS')
        if(a == 14):
            st.write('MUGBEANS')
        if(a == 15):
            st.write('MUSKMELON')
        if(a == 16):
            st.write('ORANGE')
        if(a == 17):
            st.write('PAPAYA')
        if(a == 18):
            st.write('PIGEONPEAS')
        if(a == 19):
            st.write('POMEGRANATE')
        if(a == 20):
            st.write('RICE')
        if(a == 21):
            st.write('WATERMELON')

        st.header("  APPROPRIATE VALUES REQUIRED TO GROW THE GIVEN CROP  ")
        if(crop == 'APPLE'):
            st.write(
                'Sodium: 24 Phosphorus: 128 Potassium: 196  Temperature: 22.7508 Humidity: 90.6948 pH: 5.5214 Rainfall: 110.4317')
        elif(crop == 'BANANA'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')

        elif(crop == 'BLACKGRAM'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'CHICKPEA'):
            st.write(
                'Sodium: 40 Phosphorus: 77  Potassium: 17.1311  Temperature: 16.877   Humidity: 7.4859 pH: Rainfall: 88.5512 ')
        elif(crop == 'COCONUT'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'COFFEE'):
            st.write(
                'Sodium: 104  Phosphorus: 18  Potassium: 30 Temperature: 23.6030K Humidity: 60.3017 pH: Rainfall: 6.7798 ')
        elif(crop == 'COTTON'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'GRAPES'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'JUTE'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'KIDNEYBEANS'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'LENTIL'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'MAIZE'):
            st.write(
                'Sodium: 71 Phosphorus: 54 Potassium: 16 Temperature: 22.6135 Humidity: 5.7 pH: Rainfall: 287.57')
        elif(crop == 'MANGO'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH:  Rainfall: ')
        elif(crop == 'MOTHBEANS'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH:  Rainfall: ')
        elif(crop == 'MUGBEANS'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'MUSKMELON'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        if(crop == 'ORANGE'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        if(crop == 'PAPAYA'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'PIGEONPEAS'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'POMEGRANATE'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        elif(crop == 'RICE'):
            st.write(
                'Sodium: 90 Phosphorus: 42 Potassium: 43 Temperature:20.89 Humidity: 6.50 pH:  Rainfall: 202.9355 ')
        elif(crop == 'WATERMELON'):
            st.write(
                'Sodium: Phosphorus: Potassium: Temperature: Humidity: pH: Rainfall: ')
        else:
            st.write('Invalid crop name !!! data is not available')
