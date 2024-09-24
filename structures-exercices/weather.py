# weather.py

import requests

# Your API key for the weather API (you need to get one from weatherapi.com or similar)
API_KEY = "68401df8d2e54719ab5164908242409"
CITY = 'New York'
URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}'

# Fetch weather data
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant weather information
    city_name = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temp_c']
    weather_description = data['current']['condition']['text']
    
    # Print the weather information
    print(f"City: {city_name}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather_description}")
else:
    print("Failed to retrieve weather data.")
