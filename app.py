import streamlit as st
from modules.api_handler import get_weather_data
from modules.ui_components import display_weather
from modules.utils import celsius_to_farenheit


def main():
    st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

    st.title("Weather App")
    st.markdown("Enter a city to get the current weather details.")
    st.session_state.first_time = True
    # User input for city name
    city = st.text_input("Enter City", "")
    if city:
        weather_data = get_weather_data(city)
        if weather_data:
            temperature = int(weather_data['main']['temp'])
            temp_unit = "°C"
            real_feel_temperature = int(weather_data['main']['feels_like'])
            
            if st.checkbox('Show temperature in Fahrenheit'):
                temperature, real_feel_temperature = celsius_to_farenheit(temperature, real_feel_temperature)
                temp_unit = "°F"
        
            # Display weather data
            display_weather(weather_data, temperature, temp_unit, real_feel_temperature)
            st.session_state.first_time = False
        else:
            st.error("Unable to fetch weather data. Please check the city name or try again later.")
    if not city and not st.session_state.first_time:
        st.error("He")


if __name__ == "__main__":
    main()
