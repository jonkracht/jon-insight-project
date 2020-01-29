# Script to process raw data scraped from DGCR
import pandas as pd
import numpy as np
import json

# Load json file of scraped data
#file_name, save_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/data/pa_course_database.json', 'pa_course_database_processed'
file_name , save_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/data/all_course_database.json', 'all_courses_database_processed'


df = pd.read_json(file_name)









# For brevity, recast URL as DGCR id
df['dgcr_id'] = df['url'].str.split('id=', expand = True).iloc[:, 1]
#df = df.drop(columns = ['url'])




# Create 'hilliness' and 'woodedness' numerical features from 'landscape' categorical feature
landscape_split = df['landscape'].str.split("&", expand = True)
df['hills'], df['woods'] = landscape_split[0], landscape_split[1]

hill_dict = {"Mostly Flat": 0, "Moderately Hilly": 1, "Very Hilly": 2}
wood_dict = {"Lightly Wooded": 0, "Moderately Wooded": 1, "Heavily Wooded": 2}

df['hills'] = df['hills'].str.strip().map(hill_dict)
df['woods'] = df['woods'].str.strip().map(wood_dict)









# Recast 'multiple_tees_pins' into 'multiple_layouts'
df['multiple_layouts'] = df['multiple_tees_pins'].str.contains('Yes', regex = False)






# Fill missing 'year_established'
# df['year_established'].replace('--', -666,  inplace=True)
# df['year_established'] = df['year_established'].astype(float)
# df['year_established'].replace(-666, np.nan,  inplace=True)

#df['year_established'].replace('--', '',  inplace=True)

df['year_established'].replace('--', np.nan,  inplace=True)



# Fill missing 'rating'
# df['rating'].replace('', -666,  inplace=True)
# df['rating'] = df['rating'].astype(float)
# df['rating'].replace(-666, np.nan,  inplace=True)
df['rating'].replace('', np.nan, inplace = True)




# Fill missing 'rating_count'
# df['rating_count'].replace('', -666,  inplace=True)
# df['rating_count'].replace('--', -666,  inplace=True)
# df['rating_count'] = df['rating_count'].astype(float)
# df['rating_count'].replace(-666, np.nan,  inplace=True)
df['rating_count'].replace('--', np.nan,  inplace=True)



# Fill missing 'par'
# df['par'].replace('', -666,  inplace=True)
# df['par'].replace('--', -666,  inplace=True)
# df['par'] = df['par'].astype(float)
# df['par'].replace(-666, np.nan,  inplace=True)
df['par'].replace('--', np.nan,  inplace=True)


# Fill missing "sse"
# df['sse'].replace('', -666,  inplace=True)
# df['sse'].replace('--', -666,  inplace=True)
# df['sse'] = df['sse'].astype(float)
# df['sse'].replace(-666, np.nan,  inplace=True)
df['sse'].replace('--', np.nan,  inplace=True)



# Compress 'length' data:
def largestNumber(in_str):
    l=[int(x) for x in in_str.split() if x.isdigit()]
    return max(l) if l else ''

new_lengths = []
for entry in df['length']:
    new_lengths.append(largestNumber(entry))

df['length'] = new_lengths
# df['length'] = df['length'].astype(float)
# df['length'].replace(-666, np.nan,  inplace=True)
df['length'].replace('--',np.nan, inplace = True)
df['length'].replace('n/a', np.nan, inplace = True)



df['par'].replace('--', np.nan,  inplace=True)



# Compress holes data:
new_holes = []
for entry in df['holes']:
    new_holes.append(largestNumber(entry))

#df['holes'] = new_holes
#df['holes'] = df['holes'].astype(float)
#df['holes'].replace(-666, np.nan,  inplace=True)


df['holes'] = new_holes




# Correct (single) incorrect longitude value
df.loc[df['longitude'] > 0, 'longitude'] *= -1



# Save list of lat/long coordinates
x = []
for pos_x, pos_y in zip(df['longitude'].values, df['latitude'].values):
    x.append((pos_x, pos_y))
with open("pa_positions.txt", 'w') as f:
    for s in x:
        f.write(str(s) + '\n')







# Create column estimating the time it takes to play the course
m = 3/(10742 - 2810)
b = 5 - 10742*m

df['length'] = pd.to_numeric(df['length'])
df['hours_to_play'] = round(df['length'].astype(float) * m + b,2)


# Remove missing data
df = df.loc[~df.isnull().any(axis=1), :]
df = df.loc[~(df['length'] == ''), :]



# Cast columns in correct form
df['hills'] = pd.to_numeric(df['hills']).astype(int)
df['woods'] = pd.to_numeric(df['woods']).astype(int)
df['rating_count'] = pd.to_numeric(df['rating_count']).astype(int)
df['length'] = pd.to_numeric(df['length']).astype(int)
df['year_established'] = pd.to_numeric(df['year_established']).astype(int)


# Eliminate Alaska, Hawaii, and Saipan for simplicity
df = df[~df['region'].isin(['AK', 'HI', 'MP'])]



col_ordering = ['name', 'locality', 'region', 'postal_code', 'latitude', 'longitude',
                'dgcr_id', 'year_established', 'course_type', 'tee_type', 'basket_type',
                'holes', 'length', 'hours_to_play', 'multiple_layouts',
                'hills', 'woods',
                'par', 'sse', 'rating', 'rating_count']


# Remove courses with 0 for latitude/longitude:
df = df[abs(df['longitude']) > 0.01]



# Remove length outlier (Princeton Country Club, IN)
if file_name == '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/data/all_course_database.json':
    df = df.sort_values('length', ascending=False).iloc[1:]





df2 = df[col_ordering]





# Save processed dataframe

df2.to_pickle(save_name + '.plk')


print('Finished.')



