import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.grouping_and_sorting import *
print("Setup complete.")

reviews.groupby('taster_twitter_handle').size()

# Your code here
reviews_written = pd.Series(reviews.groupby('taster_twitter_handle').size())

# Check your answer
q1.check()

best_rating_per_price = reviews.groupby('price').points.max()

# Check your answer
q2.check()

price_extremes = reviews.groupby('variety').price.agg(['min','max'])

# Check your answer
q3.check()

sorted_varieties = price_extremes.sort_values(by=['min','max'],ascending=False)
print(sorted_varieties)
# Check your answer
q4.check()


temp.reset_index(inplace=True)
temp[['taster_name','mean']]

pd.Series(data=temp['mean'],)

reviewer_mean_ratings =reviews.groupby('taster_name').points.mean()

# Check your answer
q5.check()

country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)

# Check your answer
q6.check()
