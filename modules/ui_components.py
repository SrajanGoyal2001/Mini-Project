import streamlit as st
import os
from typing import Dict, Any

def get_weather_icon(icon_code: str) -> str:
    """
    Returns the path to the weather icon image based on the icon code.
    
    Args:
        icon_code (str): The weather icon code from the API.
    
    Returns:
        str: The file path of the corresponding weather icon or a default icon.
    """
    icon_path = f"assets/weather_icons/{icon_code}.png"
    return icon_path if os.path.exists(icon_path) else "assets/weather_icons/default.png"

def display_weather(
    weather_data: Dict[str, Any], temperature: float, temp_unit: str, rtemperature: float
) -> None:
    """
    Displays the weather information with a structured layout.
    
    Args:
        weather_data (Dict[str, Any]): The weather data retrieved from the API.
        temperature (float): The current temperature.
        temp_unit (str): The unit of temperature (°C or °F).
        rtemperature (float): The real feel temperature.
    
    Returns:
        None
    """
    st.subheader(
        f"**Weather in {weather_data['name']}, {weather_data['sys']['country']}**"
    )
    
    weather_condition: str = weather_data['weather'][0]['description']
    col1, col2 = st.columns([1, 2])

    with col1:
        icon_code: str = weather_data['weather'][0]['icon']
        st.image(
            f"https://openweathermap.org/img/wn/{icon_code}@2x.png", width=150
        )
        st.markdown(f"**{weather_condition.capitalize()}**")

    with col2:
        st.markdown(
            f"<h1 style='color: white;'>{temperature} {temp_unit}</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h5 style='color: gray;'>Real Feel: {rtemperature} {temp_unit}</h5>",
            unsafe_allow_html=True,
        )

    humidity: int = weather_data['main']['humidity']
    wind_speed: float = weather_data['wind']['speed']

    st.markdown(
        """
        <style>
            .info-box {
                background-color: black;
                color: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 8px rgba(255, 255, 255, 0.1);
                margin-top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="info-box">
            <p><strong>💧 Humidity:</strong> {humidity}%</p>
            <p><strong>💨 Wind Speed:</strong> {wind_speed} m/s</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
