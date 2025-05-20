from datetime import datetime
from config.logger import get_logger

logger = get_logger(__name__)


def clean_weather_data(raw_data: dict) -> dict:
    """Validate and clean raw weather data."""
    try:
        if not raw_data:
            logger.warning("Empty raw_data passed to cleaner.")
            return {}

        required_keys = ["timestamp", "latitude", "longitude", "temperature_c", "humidity_percent", "wind_speed_kph"]
        for key in required_keys:
            if key not in raw_data:
                logger.error(f"Missing key in data: {key}")
                return {}

        # Convert timestamp to datetime object
        timestamp = raw_data["timestamp"]
        try:
            raw_data["timestamp"] = datetime.fromisoformat(timestamp)
        except ValueError:
            logger.error(f"Invalid timestamp format: {timestamp}")
            return {}

        # Round numeric fields to 2 decimal places
        raw_data["temperature_c"] = round(float(raw_data["temperature_c"]), 2)
        raw_data["humidity_percent"] = round(float(raw_data["humidity_percent"]), 2)
        raw_data["wind_speed_kph"] = round(float(raw_data["wind_speed_kph"]), 2)

        logger.info("Weather data cleaned and validated.")
        return raw_data

    except Exception as e:
        logger.exception(f"Error during cleaning: {e}")
        return {}
