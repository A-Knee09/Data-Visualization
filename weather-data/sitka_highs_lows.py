import matplotlib.pyplot as plt
import csv
from datetime import datetime
from pathlib import Path

path = Path("./weather-data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []

for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])

    dates.append(date)
    highs.append(high)
    lows.append(low)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily High and Low Temperatures 2021", fontsize=24)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)
plt.show()
