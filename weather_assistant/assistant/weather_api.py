import requests
from assistant.config import OPENWEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_current_weather(city: str):
    if not OPENWEATHER_API_KEY:
        return {"error": "OpenWeather API key not configured"}

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    # Send HTTP GET request to OpenWeather
    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        return {
            "error": "OpenWeather API error",
            "status_code": response.status_code,
            "response": response.text
        }

    data = response.json()

    # Return only the fields we actually need
    return {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "temperature_c": data.get("main", {}).get("temp"),
        "humidity_percent": data.get("main", {}).get("humidity"),
        "weather_description": data.get("weather", [{}])[0].get("description"),
        "wind_speed_m_s": data.get("wind", {}).get("speed")
    }
