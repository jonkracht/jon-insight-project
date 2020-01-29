# Script to

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


# Path to processed data
#file_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/features/pa_course_database_processed.plk'
file_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/features/all_courses_database_processed.plk'

df = pd.read_pickle(file_name)

alpha_val = 0.4 # set alpha value for plots

print(df.head())


#Print mean rating of all courses
print('Average rating over all courses:  ' + str(df.rating.mean().round(2)))



# Create plots

sns.distplot(df['hills'])
plt.show()


sns.catplot(x="hills", y = "rating", data = df, alpha = alpha_val)
plt.show()

sns.catplot(x="woods", y = "rating", data = df, alpha = alpha_val)
plt.show()

sns.catplot(x = "multiple_layouts", y = "rating", data = df, alpha = alpha_val)
plt.show()


sns.distplot(df.length, bins=20)
plt.show()


df['par-sse'] = df['par'].astype('float') - df['sse']
sns.jointplot(x = 'rating', y = 'par-sse', data = df, alpha = alpha_val)
plt.show()

sns.jointplot(x = 'year_established', y = 'rating', data = df, alpha = alpha_val)
plt.show()

sns.jointplot(x = 'length', y = 'rating', data = df, alpha = alpha_val)
plt.show()

sns.jointplot(x = 'year_established', y = 'length', data = df, alpha = alpha_val)
plt.show()

print('Finished.')