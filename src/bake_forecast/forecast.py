import csv
from typing import Any
from datetime import datetime
from pathlib import Path


data_dict: dict[Any, Any] = {}


def get_average_bakes(file: str | Path) -> float | list[float]:

    file_path = Path(file)

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read the content
    with open(file_path, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # skip header
        for i, row in enumerate(reader, start=1):
            try:
                data_dict[i] = {"day": row[0], "quantity_sold": int(row[1])}
            except IndexError:
                pass

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
        return False

    return average_today