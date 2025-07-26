from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("./weather-data/sitka_weather_07-2021_simple.csv")
lines = path.read_text(encoding="utf-8").splitlines()

reader = csv.reader(lines)
header_row = next(reader)

separator = "-" * 30
print(f"{'Index':<15} {'Column Name'}")
print(separator)

for index, column_header in enumerate(header_row):
    print(f"{index:<15} {column_header}")

# Extracting high temperatures and dates
dates, highs = [], []
for row in reader:
    curr_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    dates.append(curr_date)
    highs.append(high)

# Plot the high temps
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")

# Format the plot
ax.set_title("Daily Temperatures, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
