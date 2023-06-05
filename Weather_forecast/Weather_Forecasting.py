import requests
import json
import argparse

def get_weather(city):
    api_key = "4ad55236ac002885716669d0e486ec53" # API key from openweathermap.org replace it with your actual OpenWeatherMap API key.
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # Send GET request to OpenWeatherMap API endpoint
    try:
        response = requests.get(f"{base_url}?q={city}&appid={api_key}")
         # Raise an exception for non-2xx status codes
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)
    # Parse the JSON response
    try:
        data = response.json()
        if data["cod"] != 200:
            print("Error:", data["message"])
            return None
        else:
            weather = data["weather"][0]["main"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            return {
                "weather": weather,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed
            }
    except (json.JSONDecodeError, KeyError) as e:
        print("Error occurred while parsing weather data:", e)
        return None
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the current weather forecast for a city.")
    parser.add_argument("city", help="Name of the city")
    args = parser.parse_args()

    city_name = args.city

    weather_data = get_weather(city_name)

    if weather_data:
        print("Weather forecast for", city_name)
        print("Weather:", weather_data["weather"])
        print("Temperature[in kelvin]:", weather_data["temperature"])
        print("Humidity:", weather_data["humidity"])
        print("Wind Speed:", weather_data["wind_speed"])