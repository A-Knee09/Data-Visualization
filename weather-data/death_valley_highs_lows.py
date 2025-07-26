from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path("./weather-data/death_valley_2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

highs, lows, dates = [], [], []

for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily High and Low Temperatures 2021 \nDeath Valley, CA", fontsize=24)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=16)
plt.show()
