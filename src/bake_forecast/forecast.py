import csv
from typing import Any
from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger("bake_forecast")


def get_average_bakes(file_path: Path) -> float:
    """
    Calculate the average number of bakes for one file based on the current day.

    Args:
        file_path: A single CSV file (Path).

    Returns:
        Average number of cookies sold today as a float.
    """
    count: int = 0
    data_dict: dict[Any, Any] = {}

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read the content
    with open(file_path, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # skip header
        for i, row in enumerate(reader, start=1):
            if len(row) < 2 or not row[0].strip() or not row[1].strip():
                continue
            try:
                data_dict[i] = {"day": row[0], "quantity_sold": int(row[1])}
                count += 1
            except ValueError:
                continue

    logger.info(f"Proccesed {count} rows.")

    today_day = datetime.today().strftime("%A")  # ex. Monday / Tuesday... /

    # Select only those that match today’s date
    quantities_today = [
        record["quantity_sold"]
        for record in data_dict.values()
        if record["day"] == today_day
    ]

    if quantities_today:
        average_today = sum(quantities_today) / len(quantities_today)
    else:
        print(f"Some error occured or no historical data for {today_day}")
        return 0.0

    return average_today
