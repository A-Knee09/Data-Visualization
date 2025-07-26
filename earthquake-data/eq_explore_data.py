# json.loads() = converts a JSON-formatted string into a Python object
# json.dumps() = converts a Python object into a JSON-formatted string

from pathlib import Path
import json

# Read data as a string and convert to a python object

path = Path("./eq-data/eq_data_1_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examining all earthquakes in the dataset
all_eq_dicts = all_eq_data["features"]
print(f"Length of all feautres: {len(all_eq_dicts)}")

# Extracting magnitudes and location data
mags, longitudes, latitudes = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    longitudes.append(lon)
    latitudes.append(lat)

print(f"Magnitudes of the first 10: {mags[:10]}")
print(f"First five longitudes: {longitudes[:5]}")
print(f"First five latitudes: {latitudes[:5]}")

# Create a more readable version of the data file
# path = Path("./eq-data/readable_eq_data.geojson")
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)
