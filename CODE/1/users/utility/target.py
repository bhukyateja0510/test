import pandas as pd
from django.conf import settings

import numpy as np

path = settings.MEDIA_ROOT + "\\" + "FoodRecipeRating.csv"

df = pd.read_csv('media/FoodRecipeRating.csv')

df['new'] = np.where(df['AggregatedRating'] >= float(2.5), True, False)
print(df.to_string())
print(df.columns)
x = df.iloc[:, 0:-1]
y = df.iloc[:, -1]
