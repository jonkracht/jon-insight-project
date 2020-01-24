# Script to plot longitude/latitude points on a shapefile
import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon


map_file = '/home/jon/PycharmProjects/jon-insight-project/data/external/PA/tl_2017_42_place.shp'

file_name = '/home/jon/PycharmProjects/jon-insight-project/data/processed/pa_course_database_processed.plk'
df = pd.read_pickle(file_name)

crs = {'init': 'eosg:4326'}

street_map = gpd.read_file(map_file)

fig, ax = plt.subplots(figsize = (15, 15))
street_map.plot(ax = ax)

plt.show()

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]

geo_df = gpd.GeoDataFrame(df, crs = crs, geometry= geometry)

geo_df.head()

fig, ax = plt.subplots(figsize = (15, 15))
street_map.plot(ax = ax, alpha = 0.4, color = 'grey')
geo_df.plot(ax=ax, markersize = 20, color = 'blue', marker = 'o')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Disc golf courses in Pennsylvania')
plt.show()