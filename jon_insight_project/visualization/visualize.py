# Script to

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


file_name = '/home/jon/PycharmProjects/jon-insight-project/data/processed/pa_course_database_processed.plk'
df = pd.read_pickle(file_name)

#print(df.head())

sns.distplot(df.rating.dropna(), bins=10)
plt.show()

# Print mean rating of all rounds
print(df.rating.dropna().mean().round(2))

sns.catplot(x="hilliness", y = "rating", data = df)
plt.show()

sns.catplot(x="woodedness", y = "rating", data = df)
plt.show()

sns.catplot(x = "multiple_layouts", y = "rating", data = df)
plt.show()

sns.distplot(df.length.dropna(), bins=10)
plt.show()

sns.jointplot(x = 'rating', y = 'par-sse', data = df)
plt.show()

sns.jointplot(x = 'year_established', y = 'rating', data = df)
plt.show()

print('Finished.')