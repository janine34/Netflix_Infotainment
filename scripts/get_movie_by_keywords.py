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
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# %matplotlib inline
plt.rcParams['figure.dpi'] = 300

font_files = matplotlib.font_manager.findSystemFonts()
font_files_roboto = [f for f in font_files if 'Roboto' in f]
for font_file in font_files_roboto:
    matplotlib.font_manager.fontManager.addfont(font_file)

plt.rcParams['font.family'] = 'Roboto'

FINAL_COLUMNS = [
    'titleType',
    'primaryTitle',
    'originalTitle',
    'startYear',
    'score',
    'is_genre_from_selection',
    'is_keywords_from_selection',
    'poster_url',
    'isAdult',
    'endYear',
    'runtimeMinutes',
    'genres',
    'keywords',
]

# +
# load basic movie info data
title_basics = pd.read_csv('data/title.basics.tsv', sep='\t', header=0).set_index('tconst')

# load keyword data
title_keywords = pd.read_csv('data/keywords_movie.csv').set_index('tconst')
# inner join it with basics to remove all entries without keywords
titles_with_keywords = title_keywords.join(title_basics, how='inner')
# -

# load poster data
title_posters = pd.read_csv('data/posters_movie.csv').set_index('tconst')
# remove duplicates
title_posters = title_posters[~title_posters.index.duplicated(keep='first')]
# left join it with titles with keywords to keep all entries without poster
titles_with_keywords = titles_with_keywords.join(title_posters, how='left')

fig, ax = plt.subplots()
sns.set_theme(font='Roboto')
# title
ax.text(x=0.0, y=1.07, s='Distribution of movie and series per year', fontsize=18, weight='bold', ha='left', va='bottom', transform=ax.transAxes)
ax.text(x=0.0, y=1.01, s='Large skew for post-2000 movies, recent movies missing', fontsize=12, alpha=0.75, ha='left', va='bottom', transform=ax.transAxes)
ax.text(x=0.3, y=-0.18, s='Source: IMDB Dataset | Data viz: @janine34', fontsize=12, weight='medium', alpha=1.0, ha='left', va='bottom', transform=ax.transAxes)
titles_with_keywords.startYear[
    (titles_with_keywords.startYear != '\\N')].astype(int).hist(bins=np.arange(1930, 2022))
sns.despine(bottom=True, left=True)  # remove borders of plot
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
plt.show()


# +
def tokenize(string):
    """tokenize keyword string"""
    return string.strip().lower().replace(' ', '-')

def clean_genres(genres):
    return [tokenize(genre) for genre in genres.split(',')]


# +
# selections

genres, keywords = {}, {}

# US elections
genres['us-elections'] = [
    'Documentary',
    'Biography',
    'Drama',
    'History',
    'Thriller',
]

keywords['us-elections'] = [
    'Elections',
    'Citizen',
    'Votes',
    'Politic',
    'Politics',
    'Electoral system',
    'Rights',
    'President',
    'Investigation',
    'Social media',
    'Influence',
    'Power',
    'Corruption',
    'Donald Trump',
    'Barack Obama',
    'Alexandria Ocasio-Cortez',
    'Scandal',
    'white house',
    'campaign',
    'political campaigns',
    'leaders',
    'equal rights',
    'Mitt Rodney',
    'congressman',
    'congresswoman',
    'congress',
    'republican',
    'democrat',
    'tea party',
]

# G20: climate summit
genres['g20-climate-summit'] = [
    'Documentary',
    'Biography',
    'Drama',
    'History',
    'Adventure',
]
keywords['g20-climate-summit'] = [
    'Ecology',
    'Nature',
    'Biodiversity',
    'Climate Change',
    'Plastic',
    'Life',
    'Catastrophe',
    'Ocean',
    'Ocean Life',
    'Earth',
    'Wildlife',
    'Flora',
    'Extinction',
    'Forest',
    'Marine species',
    'Pollution',
    'Conservation',
    'Agriculture',
    'Deforestation',
    'Consumption',
    'Globalisation',
    'Challenge',
    'dystopias',
    'Global warming',
    'Investigation',
    'Scientists',
    'Researchers',
    'World',
    'Civilization',
    'Water',
    'new technologies',
    'sustainability',
    'environmental issues',
    'disaster',
    'multinational company',
    'risks',
    'post-apocalyptic world',
    'coral reefs',
]
# -

# make genres an actual list
titles_with_keywords['genres'] = titles_with_keywords['genres'].apply(clean_genres)
# make keywords an actual list
titles_with_keywords['keywords'] = titles_with_keywords['keywords'].fillna("['']").apply(eval)

for selection in ['us-elections', 'g20-climate-summit']:
    # tokenize genres and keywords
    genres[selection] = [tokenize(genre) for genre in genres[selection]]
    keywords[selection] = [tokenize(keyword) for keyword in keywords[selection]]

    # compute # of intersecting genres

    def is_genre_from_selection(title_genres):
        return len(set(genres[selection]).intersection(set(title_genres)))

    titles_with_keywords['is_genre_from_selection'] = \
        titles_with_keywords['genres'].apply(is_genre_from_selection)

    # compute # of intersecting keywords

    def is_keywords_from_selection(title_keywords):
        return len(set(keywords[selection]).intersection(set(title_keywords)))

    titles_with_keywords['is_keywords_from_selection'] = \
        titles_with_keywords['keywords'].apply(is_keywords_from_selection)

    # filter out selected titles
    titles_from_selection = titles_with_keywords.copy()
    titles_from_selection = titles_from_selection[titles_from_selection['is_genre_from_selection'] > 0]
    titles_from_selection = titles_from_selection[titles_from_selection['is_keywords_from_selection'] > 0]

    # sort them by crude "likelihood" score which is computed as
    # score = # intersecting keywords + # intersecting genres
    # ideally we would do smarter, using some NLP stuff, but yea no time
    titles_from_selection['score'] = titles_from_selection['is_genre_from_selection'] + \
        titles_from_selection['is_keywords_from_selection']
    titles_from_selection = titles_from_selection.sort_values(by='score', ascending=False,)

    # save to file
    titles_from_selection[FINAL_COLUMNS].to_csv(f'data/{selection}_movie.csv')
