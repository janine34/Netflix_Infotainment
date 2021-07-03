# Netflix Infotainment

Python scripts and utilities to download movie data and build rudimentary recommender
system based on keywords and genres.

## 1. Installation instructions

Assuming you use [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/),
and create a conda environment called `netflix-infotainment`. We are using [imdbpy](https://imdbpy.readthedocs.io/en/latest/index.html) to use IMDB API.

```bash
conda create --name netflix-infotainment python=3.6
conda activate netflix-infotainment
conda install -c conda-forge --file requirements.txt
pip install imdbpy
```

## 2. Usage

You will first need to download [IMDB dataset](https://www.imdb.com/interfaces/) `.tsv` files and place them inside the data folder (get both the `title.basics.tsv.gz` and the `title.ratings.tsv.gz`)

You need to call the scripts in this order:

```bash
# get all keywords for the top 10,000 movies, will take 4h at least
python scripts/get_keyword_dataset.py
# get all poster URLs from lists dropped from custom API
python scripts/get_poster_urls.py
# get top recommended movies for each use case (us elections and g20 climate summit)
python scripts/get_movie_by_keywords.py
```
