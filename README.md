# 🌦️ Weather Data Pipeline

This project is a modular and extendable data pipeline that fetches, cleans, and stores real-time weather data using the [Open-Meteo API](https://open-meteo.com/). It is designed with clean code practices and serves as a foundational project for learning **data engineering**.

---

## ✅ Features

- 📡 Fetches hourly weather data using Open-Meteo's free API
- 🧼 Cleans and validates raw JSON response
- 💾 Saves data locally in partitioned **Parquet** files (for efficient analytics)
- 📁 Organized folder structure for scalability
- 🎯 Modular design using layers: `ingest/`, `transform/`, `load/`
- 📋 Logs to terminal and file using a centralized, color-coded logger

---

## 🧱 Project Structure

```

weather-pipeline/
├── config/
│   └── logger.py              # Centralized colorful logger
├── ingest/
│   └── fetch\_weather.py       # API data fetching
├── transform/
│   └── clean\_weather.py       # Data cleaning
├── load/
│   └── save\_parquet.py        # Save to Parquet
├── data/                      # Partitioned data files
├── main.py                    # Entry point for the pipeline
├── .gitignore
├── requirements.txt
└── README.md

````

---

## 📦 How It Works

1. **Fetch Weather Data**  
   Calls the Open-Meteo API for a given location (default: New Delhi).

2. **Clean & Transform**  
   Parses and filters the raw response, converting it into a structured pandas DataFrame.

3. **Save as Parquet**  
   The cleaned data is saved to a local folder as `.parquet` files, partitioned by date.

---

## 📋 How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt
````

2. **Run the pipeline**:

```bash
python main.py
```

3. **Check output**:

   * Logs will appear in the terminal and `logs/pipeline.log`
   * Data will be saved in `data/YYYY-MM-DD/weather.parquet`

---

## 📌 Dependencies

* `pandas`
* `requests`
* `pyarrow` (for Parquet support)
* `rich` (for colorful logging)

---

## 📈 What's Next?

* Add unit tests for each module
* Support multiple cities
* Load data into a PostgreSQL database
* Automate using Airflow or Prefect
* Add a simple dashboard using Streamlit or Superset

---

## 📚 Learning Goals

This project helps you learn:

* API ingestion
* Data cleaning with pandas
* File formats for big data (Parquet)
* Project modularization
* Logging and error handling

---

## 📄 License

MIT License

---
