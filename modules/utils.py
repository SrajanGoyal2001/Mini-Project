def celsius_to_farenheit(temperature: float, real_feel_temperature: float) -> tuple:
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        temperature (float): The temperature in Celsius to be converted.
        real_feel_temperature (float): The real_feel_temperature in Celcius to be converted

    Returns:
        tuple: The temperature and real_feel_temperature converted to Fahrenheit, rounded to the nearest integer.
    """
    return int((temperature) * 9/5 + 32), int((real_feel_temperature) * 9/5 + 32)


def farenheit_to_celsius(temperature: float, real_feel_temperature: float) -> tuple:
    """Converts Fahrenheit temperature to Celsius.
    Args:
        temperature (float): The temperature in Farenheit to be converted.
        real_feel_temperature (float): The real_feel_temperature in Farenheit to be converted

    Returns:
        tuple: The temperature and real_feel_temperature converted to Fahrenheit, rounded to the nearest integer.
    """
    celsius_temp = (temperature - 32) * 5/9
    celsius_real_feel_temp = (real_feel_temperature - 32) * 5/9
    return round(celsius_temp), round(celsius_real_feel_temp)
