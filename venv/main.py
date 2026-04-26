import streamlit as st
import plotly.express as px

st.title("Weather Forecast")
place = st.text_input("Place :")
days = st.text_input("Forecast days :")
# , min_value=1 , max_value=5, help="Select number of days between 1 and 5 for forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):

    dates = ["2026-04-26","2026-04-25","2026-04-24"]
    temperatures = [1,2,3]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d,t = get_data(days)

figure = px.line(x = d, y = t, labels={"x": "Dates", "y": "Temperature"})
st.plotly_chart(figure)