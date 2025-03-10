import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
        body{
            background-color: #121212;
            color: white;
        }
        .stApp{
            background: linear-gradient(135deg, #2c2c2c, #3a3a3a);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        }
        h1{
            text-align: center;
            font-size: 36px;
            color: white;
        }
        .stButton>button{
            background: #444;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            box-shadow: 0px 5px 15px rgba(255,255,255,0.2);
        }
        .stButton>button:hover{
            transform: scale(1.05);
            background: linear-gradient(45deg, #1e90ff, #00fa9a);
            color: black;
        }
        .result-box{
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.2);
        }
        .footer{
            text-align: center;
            margin-top: 50px;
            font-size: 15px;
            color: white;
        }
    </style>    
    """, 
    unsafe_allow_html=True
)

# Title
st.title("Unit Converter")

# Description
st.write("Easily convert between units of length, weight, and temperature.")

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Choose conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meter", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meter", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meter': 1, 'Centimeters': 100, 'Millimeters': 1000, 'Miles': 0.000621371, 'Yards': 1.09361, 'Inches': 39.37, 'Feet': 3.28
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.2046, 'Ounces': 35.27   
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Button for conversion
if st.button("Convert 🔁"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created by Huzaifa Rehan </div>", unsafe_allow_html=True)
