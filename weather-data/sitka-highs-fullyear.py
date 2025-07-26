from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

data_path = Path("./weather-data/sitka_weather_2021_simple.csv")
lines = data_path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

seperator = "-" * 35
print(f"{'Index':<15} {'Column Name'}")
print(seperator)

for index, header in enumerate(header_row):
    print(f"{index:<15} {header}")

dates, highs = [], []

for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    dates.append(date)
    highs.append(high)

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")

ax.set_title("Daily High Temperatures 2021")
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperatures (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)
plt.show()
