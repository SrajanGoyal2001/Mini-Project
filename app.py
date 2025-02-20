import streamlit as st
from modules.api_handler import get_weather_data
from modules.ui_components import display_weather
from modules.utils import celcius_to_fahrenheit

# Apply page config for better design
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")


def main():
    """Main function to run the Streamlit weather app."""
    
    # Add a title with custom styling
    try:
        st.markdown("<h1 style='text-align: center; color: #4A90E2;'>☁️ Weather App ☀️</h1>", unsafe_allow_html=True)
    
        city = st.text_input("🏙️ Enter city name:", "")
        check_weather_button = st.button("Get Weather")

        if check_weather_button:
            if city:
                weather_data = get_weather_data(city)
                if weather_data:
                    temperature = int(weather_data['main']['temp'])
                    temp_unit = "°C"
                    rtemperature = int(weather_data['main']['feels_like'])

                    # Display weather data
                    display_weather(weather_data, temperature, temp_unit, rtemperature)
                
            else:
                raise Exception('Enter a valid city.')

    except Exception as e:
        st.error(str(e).title())

        
if __name__ == "__main__":
    main()
