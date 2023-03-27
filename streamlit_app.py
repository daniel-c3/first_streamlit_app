import streamlit as st

st.title("My Parents New Healthy Diner")

st.subheader("Breakfast Menu")

option1 = "Omega 3 & Blueberry Oatmeal"
option2 = "Kale, Spinach & Rocket Smoothie"
option3 = "Hard-Boiled Free-Range Egg"

option = st.selectbox("Selecciona una opción", [option1, option2, option3])

st.write("Has seleccionado:", option)
