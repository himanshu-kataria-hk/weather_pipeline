# load/save_parquet.py

import os
import pandas as pd
from datetime import datetime
from config.logger import get_logger

logger = get_logger(__name__)


def save_to_parquet(cleaned_data: dict, base_dir="data") -> str:
    """Saves cleaned weather data to a partitioned parquet file."""

    if not cleaned_data:
        logger.warning("No data passed to save_to_parquet.")
        return ""

    try:
        # Use timestamp to determine folder
        timestamp: datetime = cleaned_data["timestamp"]
        date_str = timestamp.strftime("%Y-%m-%d")

        folder_path = os.path.join(base_dir, date_str)
        os.makedirs(folder_path, exist_ok=True)

        file_name = f"{timestamp.strftime('%H-%M-%S')}.parquet"
        file_path = os.path.join(folder_path, file_name)

        df = pd.DataFrame([cleaned_data])
        df.to_parquet(file_path, index=False, engine="pyarrow")

        logger.info(f"Saved weather data to: {file_path}")
        return file_path

    except Exception as e:
        logger.exception(f"Failed to save to Parquet: {e}")
        return ""
