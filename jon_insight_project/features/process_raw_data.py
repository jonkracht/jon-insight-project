# Script to process data scraped from DGCR
import pandas as pd

file_name = '/home/jon/PycharmProjects/jon-insight-project/data/raw/pa_course_database.json'
df = pd.read_json(file_name)

# Create 'hilliness' and 'woodedness' columns; drop 'landscape' column; map to numeric values
new = df['landscape'].str.split("&", n=1, expand = True)
df['hilliness'] = new[0]
df['woodedness'] = new[1]

df = df.drop(columns=['landscape'])

hill_dict = {"Mostly Flat": 0, "Moderately Hilly": 1, "Very Hilly": 2}
wood_dict = {"Lightly Wooded": 0, "Moderately Wooded": 1, "Heavily Wooded": 2}

df['hilliness'] = df['hilliness'].str.strip().map(hill_dict)
df['woodedness'] = df['woodedness'].str.strip().map(wood_dict)


# Recast multiple tees/pins column as multiple layouts
df['multiple_layouts'] = df['multiple_tees_pins'].str.contains('Yes', regex = False)
df = df.drop(columns=['multiple_tees_pins'])

print('Finished.')