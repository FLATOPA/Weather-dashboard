from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENWEATHER_API_KEY")

# Check if the API key is loaded
if not api_key:
    print("API Key is missing. Please check your .env file.")
    exit()

# Example city to fetch weather data for
city = "Chicago"

# Construct the URL to get weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

# Fetch the weather data
response = requests.get(url)

# Check the response
if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°F")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description}")
else:
    print(f"Failed to get data for {city}: {response.status_code}")
    print("No weather data found.")
