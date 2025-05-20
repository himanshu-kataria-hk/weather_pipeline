from ingest.fetch_weather import fetch_weather
from transform.clean_weather import clean_weather_data
from load.save_parquet import save_to_parquet

if __name__ == "__main__":
    lat = 28.61
    lon = 77.23

    raw = fetch_weather(lat, lon)
    cleaned = clean_weather_data(raw)
    save_to_parquet(cleaned)
