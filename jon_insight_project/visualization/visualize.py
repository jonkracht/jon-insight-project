# Script to

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


#file_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/features/pa_course_database_processed.plk'
file_name = '/home/jon/PycharmProjects/jon-insight-project/jon_insight_project/features/all_courses_database_processed.plk'

alpha_val = 0.4


df = pd.read_pickle(file_name)

print(df.head())
print(df.dtypes)




#Print mean rating of all rounds
print(df.rating.dropna().mean().round(2))


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