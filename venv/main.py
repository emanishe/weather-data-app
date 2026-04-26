import streamlit as st

st.title("Weather Forecast")
place = st.text_input("Place :")
days = st.text_input("Forecast days :")
# , min_value=1 , max_value=5, help="Select number of days between 1 and 5 for forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")