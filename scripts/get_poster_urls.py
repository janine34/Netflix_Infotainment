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
import csv
import re
from pathlib import Path

import numpy as np
import pandas as pd

# -

genres = ['adventure', 'biography', 'documentary', 'drama', 'history', 'thriller']
title_types = ['movies']

filepath_template = 'data/posters/{genre}_{title_type}.txt'

with open(f'data/posters_movie.csv', 'w') as handle:
    writer = csv.writer(handle)
    writer.writerow(['tconst', 'poster_url'])

    for genre in genres:
        filepath = filepath_template.format(genre=genre, title_type='movies')
        with open(filepath, 'r') as handle:
            # file is in a godforsaken format, neither yaml nor json
            # maybe one day people will follow standards
            lines = handle.readlines()
            tconst, poster_url = None, None
            for line in lines:
                # look for IMDB ID
                result = re.search(r'(?:imdbId: ")(tt\d*)(?:")', line)
                if result is not None:
                    tconst = result.groups()[0]
                # look for poster url
                result = re.search(r'(?:poster: ")(.*)(?:",)', line)
                if result is not None:
                    poster_url = result.groups()[0]
                    # write to file
                    assert tconst is not None
                    writer.writerow([tconst, poster_url])
                    tconst, poster_url = None, None


