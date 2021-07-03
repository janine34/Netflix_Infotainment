# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# inspired from towards data science article: https://towardsdatascience.com/how-to-create-simple-keyword-based-movie-recommender-models-from-scratch-afde718636c9
# parse saved keywords using .apply(eval) https://towardsdatascience.com/dealing-with-list-values-in-pandas-dataframes-a177e534f173
import csv
import time

import imdb
import pandas as pd
import numpy as np
import tqdm


# +
# create IMDB API endpoint
imdb_api = imdb.IMDb()

# load dataframes
title_basics = pd.read_csv('data/title.basics.tsv', sep='\t', header=0)
title_ratings = pd.read_csv('data/title.ratings.tsv', sep='\t', header=0)

# set tconst as index of title_basics and title_ratings
title_basics.set_index('tconst', inplace=True)
title_ratings.set_index('tconst', inplace=True)
# -

for title_type in ['movie', 'tvSeries']:
    # select movies and series from title_basics table
    titles = title_basics[title_basics.titleType == title_type]

    # Joint the 2 tables by tconst, the IMDb key for all movies
    titles_with_rating = titles.join(title_ratings, how='inner')

    # Take only the top 10,000 titles, where we rank movies by the number of votes they have received
    top_10000_titles = titles_with_rating.sort_values(by='numVotes', ascending=False)[:10000]
    title_indices = top_10000_titles.index

    with open(f'data/keywords_{title_type}.csv', 'w') as handle:
        writer = csv.writer(handle)
        writer.writerow(['tconst', 'keywords'])
        for movie_index in tqdm.tqdm(title_indices):
            try:
                keywords = imdb_api.get_movie_keywords(movie_index[2:])['data']['keywords']
            except:
                keywords = ''
            writer.writerow([movie_index, keywords])
            time.sleep(1)


