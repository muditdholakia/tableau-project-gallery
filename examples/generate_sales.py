import csv
from pathlib import Path
from datetime import date, timedelta

def generate():
    path = Path("data/sales.csv")
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["Sale ID", "Date", "Region", "Quantity", "Unit Price"])
        for i in range(120):
            writer.writerow([i + 1, date(2026, 1, 1) + timedelta(days=i), ["North", "South", "West"][i % 3], 1 + i % 5, 10 + i % 7])
    return path

if __name__ == "__main__":
    print(generate())
