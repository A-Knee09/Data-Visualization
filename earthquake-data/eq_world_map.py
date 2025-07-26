from pathlib import Path
import json

import plotly.express as px

path = Path("./eq-data/eq_data_30_day_m1.geojson")
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examining all earthquakes in the dataset
all_eq_dicts = all_eq_data["features"]
print(f"Length of all feautres: {len(all_eq_dicts)}")

# Extracting magnitudes and location data
mags, longitudes, latitudes, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    longitudes.append(lon)
    latitudes.append(lat)
    eq_titles.append(eq_title)

title = "Global Earthquakes"

fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
