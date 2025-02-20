import streamlit as st
import os

def get_weather_icon(icon_code: str):
    """
    Returns the path to the weather icon image based on the icon code.
    """
    icon_path = f"assets/weather_icons/{icon_code}.png"
    return icon_path if os.path.exists(icon_path) else "assets/weather_icons/default.png"

# def display_weather_info(weather_data):
#     """
#     Displays weather information in a well-structured format with icons and styling.
#     """
#     st.markdown(
#         """
#         <style>
#             .weather-container {
#                 background: #1E293B;
#                 padding: 30px;
#                 border-radius: 15px;
#                 box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
#                 color: #E2E8F0;
#                 text-align: center;
#                 max-width: 500px;
#                 margin: auto;
#             }
#             .weather-title {
#                 font-size: 28px;
#                 font-weight: bold;
#                 color: #FFFFFF;
#             }
#             .weather-info {
#                 font-size: 20px;
#                 margin: 10px 0;
#             }
#             .weather-icon {
#                 width: 80px;
#                 margin: 10px auto;
#                 display: block;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
    
#     icon_code = weather_data['weather'][0]['icon']
#     icon_path = get_weather_icon(icon_code)
    
#     st.markdown(
#         f'''
#         <div class="weather-container">
#             <p class="weather-title">🌍 Weather in {weather_data["name"]}, {weather_data["sys"]["country"]}</p>
#             <img src="{icon_path}" class="weather-icon"/>
#             <p class="weather-info">🌡️ Temperature: {weather_data['main']['temp']}°C</p>
#             <p class="weather-info">💧 Humidity: {weather_data['main']['humidity']}%</p>
#             <p class="weather-info">💨 Wind Speed: {weather_data['wind']['speed']} m/s</p>
#             <p class="weather-info">🌥️ Condition: {weather_data['weather'][0]['description'].title()}</p>
#         </div>
#         ''',
#         unsafe_allow_html=True
#     )


def display_weather(weather_data, temperature, temp_unit, rtemperature):
    """Displays the weather information with a structured layout."""

    # Display City Name and Country at the Top
    st.subheader(f"**Weather in {weather_data['name']}, {weather_data['sys']['country']}**")
    weather_condition = weather_data['weather'][0]['description']

    # Create a two-column layout for icon and temperature
    col1, col2 = st.columns([1, 2])

    with col1:
        # Weather Icon
        icon_code = weather_data['weather'][0]['icon']
        st.image(f"https://openweathermap.org/img/wn/{icon_code}@2x.png", width=150)
        st.markdown(f"**{weather_condition.capitalize()}**")

    with col2:
        # Temperature in bold
        st.markdown(f"<h1 style='color: white;'>{temperature} {temp_unit}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='color: gray;'>Real Feel: {rtemperature} {temp_unit}</h5>", unsafe_allow_html=True)

    # Weather condition details below the columns

    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # Styled Weather Info Box
    st.markdown(
        """
        <style>
            .info-box {
                background-color: black;
                color: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 8px rgba(255,255,255,0.1);
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
        unsafe_allow_html=True
    )