import csv
from typing import Any
from datetime import datetime

data_dict: dict[Any,Any] = {}

with open("sold_items.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    next(reader)  # skip header
    for i, row in enumerate(reader, start=1):
        try:
            data_dict[i] = {"day": row[0], "quantity_sold": int(row[1])}
        except IndexError as e:
            print (f"IndexErorr: {e}")

today_day = datetime.today().strftime("%A")

quantities_today = [record["quantity_sold"]
                    for record in data_dict.values()
                    if record["day"] == today_day]

if quantities_today:
    average_today = sum(quantities_today)/len(quantities_today)
    print (f"Recommended amount for baking today is: {average_today:.0f}")
else:
    print (f"Some error occured or no historical data for {today_day}")