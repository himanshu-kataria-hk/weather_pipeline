# ingest/fetch_weather.py

import requests
from datetime import datetime
from config.logger import get_logger

logger = get_logger(__name__)

def fetch_weather(latitude: float, longitude: float) -> dict:
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    try:
        logger.info(f"Fetching weather for lat={latitude}, lon={longitude}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data.get("current", {})
        weather_data = {
            "timestamp": current.get("time", datetime.utcnow().isoformat()),
            "latitude": latitude,
            "longitude": longitude,
            "temperature_c": current.get("temperature_2m"),
            "humidity_percent": current.get("relative_humidity_2m"),
            "wind_speed_kph": current.get("wind_speed_10m")
        }
        logger.debug(f"Weather data: {weather_data}")
        return weather_data

    except requests.RequestException as e:
        logger.error(f"Failed to fetch weather: {e}")
        return {}
