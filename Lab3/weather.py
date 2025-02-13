import requests
import json

# WeatherAPI key
WEATHER_API_KEY = '0dfa696056104b94a1533127251302'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(url)
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        data = response.json()
        current_temp = data['current']['temp_f']
        feels_like = data['current']['feelslike_f']
        weather_condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_mph']
        wind_direction = data['current']['wind_dir']
        pressure = data['current']['pressure_mb']
        uv_index = data['current']['uv']
        cloud_cover = data['current']['cloud']
        visibility = data['current']['vis_miles']

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        print(f"Current temperature: {current_temp}°F")
        print(f"Feels like: {feels_like}°F")
        print(f"Weather condition: {weather_condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} mph")
        print(f"Wind direction: {wind_direction}")
        print(f"Pressure: {pressure} mb")
        print(f"UV index: {uv_index}")
        print(f"Cloud cover: {cloud_cover}%")
        print(f"Visibility: {visibility} miles")
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter city name: ")
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
    pass
