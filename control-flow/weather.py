import requests
import json

def get_weather(city_name, api_key):
    """
    Fetches current weather information for a given city from OpenWeatherMap API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather" # This is the URL

    params = { # These are the parameters for the URL
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
if __name__ == "__main__":
    # IMPORTANT: Replace "YOUR_API_KEY" with the actual API key you got from OpenWeatherMap
    # This is where your API key should be assigned as a string.
    API_KEY = "67dbb70404e4d154ee69c5edb0f71eeb" # Your actual API key, now correctly as a string

    # Example: Get weather for a city
    city = input("Enter the city name to get weather for: ")
    
    # Call the get_weather function with the city and the API_KEY variable
    weather_info = get_weather("Nairobi", "67dbb70404e4d154ee69c5edb0f71eeb")

    if weather_info:
        # Extract and print relevant information
        temperature = weather_info["main"]["temp"]
        feels_like = weather_info["main"]["feels_like"]
        description = weather_info["weather"][0]["description"]
        humidity = weather_info["main"]["humidity"]
        wind_speed = weather_info["wind"]["speed"]
        
        print("\n--- Current Weather Information ---")
        print(f"City: {weather_info['name']}")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Feels like: {feels_like:.1f}°C")
        print(f"Description: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed:.1f} m/s")
        print("-----------------------------------")
    else:
        print("Could not retrieve weather information.")