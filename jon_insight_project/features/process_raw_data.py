# Script to process data scraped from DGCR
import pandas as pd
import numpy as np
import json

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


# Fill missing 'year_established'
df['year_established'].replace('--', -666,  inplace=True)
df['year_established'] = df['year_established'].astype(float)
df['year_established'].replace(-666, np.nan,  inplace=True)

# Fill missing 'rating'
df['rating'].replace('', -666,  inplace=True)
df['rating'] = df['rating'].astype(float)
df['rating'].replace(-666, np.nan,  inplace=True)


# Fill missing 'rating'
df['rating_count'].replace('', -666,  inplace=True)
df['rating_count'].replace('--', -666,  inplace=True)
df['rating_count'] = df['rating_count'].astype(float)
df['rating_count'].replace(-666, np.nan,  inplace=True)

# Fill missing 'par'
df['par'].replace('', -666,  inplace=True)
df['par'].replace('--', -666,  inplace=True)
df['par'] = df['par'].astype(float)
df['par'].replace(-666, np.nan,  inplace=True)

df['sse'].replace('', -666,  inplace=True)
df['sse'].replace('--', -666,  inplace=True)
df['sse'] = df['sse'].astype(float)
df['sse'].replace(-666, np.nan,  inplace=True)

# Compress 'length' data:
def largestNumber(in_str):
    l=[int(x) for x in in_str.split() if x.isdigit()]
    return max(l) if l else -666

new_lengths = []
for entry in df['length']:
    new_lengths.append(largestNumber(entry))

df['length'] = new_lengths
df['length'] = df['length'].astype(float)
df['length'].replace(-666, np.nan,  inplace=True)









# Compress holes data:
new_holes = []
for entry in df['holes']:
    new_holes.append(largestNumber(entry))

df['holes'] = new_holes
df['holes'] = df['holes'].astype(float)
df['holes'].replace(-666, np.nan,  inplace=True)






# Save list of lat/long coordinates
x = []
for pos_x, pos_y in zip(df['longitude'].values, df['latitude'].values):
    x.append((pos_x, pos_y))
with open("pa_positions.txt", 'w') as f:
    for s in x:
        f.write(str(s) + '\n')




# Save processed dataframe
save_name = 'pa_course_database_processed'
df.to_pickle(save_name + '.plk')








print('Finished.')



