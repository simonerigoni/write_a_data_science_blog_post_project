# Write A Data Science Blog Post Project

## Introduction

This project is part of The [Udacity](https://eu.udacity.com/) Data Scientist Nanodegree Program which is composed by:
* Term 1
    * Supervised Learning
    * Deep Learning
    * Unsupervised Learning
* Term 2
    * Write A Data Science Blog Post
    * Disaster Response Pipelines
    * Recommendation Engines

The goal of this project is to put in practice the technical skills teached during the program but manly to focus on the ability to effectively communicate the results of the analysis. In particular the **CRISP-DM Process** (Cross Industry Process for Data Mining) which is composed by the following steps:
1. Business Understanding
2. Data Understanding
3. Prepare Data
4. Data Modeling
5. Evaluate the Results
6. Deploy

## Software and Libraries

This project uses Python 3.10.4 and the most important packages are:

* [NumPy](http://www.numpy.org/)
* [Pandas](http://pandas.pydata.org)
* [nltk](https://www.nltk.org/)
* [scikit-learn](http://scikit-learn.org/stable/)
* [Matplotlib](http://matplotlib.org/)
* [seaborn](https://seaborn.pydata.org/)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* WordCloud

To create the virtual enviroment you can run `python -m venv .venv`.

More informations in `requirements.txt`. I am providing a simplified version of the file and letting pip handle the dependencies to avoid maintenance overhead.

To create a complete requirements file you can run `pip freeze > requirements.txt` and to install all python packages in it you can run `pip install -r requirements.txt`.

To setup a new enviroment and install all requirements you can go in folder `others` and run `setup.cmd`

## Data

The dataset is provided by [Airbnb](http://insideairbnb.com/get-the-data.html) and is basically composed by:

* **listings.csv**: Detailed Listings data for Milan
* **calendar.csv**: Detailed Calendar Data for listings in Milan
* **reviews.csv**: Detailed Review Data for listings in Milan
* **summary_listings.csv**: Summary information and metrics for listings in Milan (good for visualisations).
* **summary_reviews.csv**: Summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing).
* **neighbourhoods.csv**: Neighbourhood list for geo filter. Sourced from city or open source GIS files.
* **neighbourhoods.geojson**: GeoJSON file of neighbourhoods of the city.

To map the neighbourhood in the dataset to the real neighbourhood I have created the file **data/quartieri.txt** which contains the real neighbourhood of Milan.

## Workflow

The code is provided in the [Jupyter Notebook](http://ipython.org/notebook.html) _neighborhoods_sentiment_analysis.ipynb_. It will read the data from `DATA_FOLDER` and step by step explore the data TODO.

## Testing

From the project folder run `pytest`

To run a single test: `pytest .\tests\test_configuration.py::test_create_folders`

## Code styling

[PEP8](https://peps.python.org/pep-0008/) is the style guide for Python code, and it's good practice to follow it to ensure your code is readable and consistent.

To check and format my code according to PEP8 I am using:
- [pycodestyle](https://pypi.org/project/pycodestyle/): tool to check the code against PEP 8 conventions.
- [autopep8](https://pypi.org/project/autopep8/): tool to automatically format Python code according to PEP 8 standards.

To run pycodestyle on all files in the project folder and create a report: `pycodestyle --statistics --count . > code_styling/report.txt`

To run autopep8 on all files in the project folder: `autopep8 --recursive --in-place .`

I prefere to check and update one file at the time because the previous recursive commands affect also `.venv\` files. For example:

`pycodestyle .\utils\configuration.py > .\code_styling\configuration_report.txt`

`autopep8 --in-place .\utils\configuration.py`

You can go in folder `code_styling` and run `format_and_lint.cmd`.

## Running the code

You can open _neighborhoods_sentiment_analysis.ipynb_ and run each cell and check their results.

You can also run the command `ipython -c "%run neighborhoods_sentiment_analysis.ipynb"`.

To convert the notebook in HTML format run `jupyter nbconvert neighborhoods_sentiment_analysis.ipynb --to html`.

## Results

TODO: describe results

## List of activities

In the [TODO](TODO.md) file you can find the list of tasks and on going activities.

## Licensing and acknowledgements

Thank you [Airbnb](https://www.airbnb.com/) for the datasets and more information about the licensing of the data can be find [here](http://insideairbnb.com/about.html).

## Outro

I hope this repository was interesting and thank you for taking the time to check it out. On my Medium you can find a more in depth [story](https://medium.com/@simone.rigoni01/do-you-want-to-move-to-milan-neighborhoods-sentiment-analysis-using-airbnb-data-72db72ebc070?sk=52ad4741d36bb8a3005b2ad13832d622) and on my Blogspot you can find the same [post](https://simonerigoni01.blogspot.com/2022/12/do-you-want-to-move-to-milan.html) in italian. Let me know if you have any question and if you like the content that I create feel free to [buy me a coffee](https://www.buymeacoffee.com/simonerigoni).
