import requests
from config import API_KEY, BASE_URL
import streamlit as st


def get_weather_data(city: str) -> dict:
    """Fetches weather data from OpenWeatherMap API for a given city.

    Args:
        city (str): The name of the city for which the weather data is to be fetched.

    Returns:
        dict: A dictionary containing the weather data if the request is successful.
              The data includes information like temperature, humidity, weather description, etc.
              Returns None if there is an error or failure in the request.
    """
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response = response.json()
        if response['cod'] == 200:
            return response
        else:
            raise Exception(response['message'])
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None
    except Exception as e:
        print(e)
        st.error(f'❌{str(e).title()}')
