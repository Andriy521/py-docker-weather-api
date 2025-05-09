import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable not set.")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Paris",
        "appid": api_key,
        "units": "metric",  # або "imperial" для Fahrenheit
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return

    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Current weather in Paris: {temp}°C, {description}")


if __name__ == "__main__":
    get_weather()
