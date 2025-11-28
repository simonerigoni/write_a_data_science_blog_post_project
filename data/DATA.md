# Write A Data Science Blog Post Project

## Data

This folder contains the data used by the project.

The dataset is provided by [Airbnb](http://insideairbnb.com/get-the-data.html) and is basically composed by:

* **listings.csv**: Detailed Listings data for Milan
* **calendar.csv**: Detailed Calendar Data for listings in Milan
* **reviews.csv**: Detailed Review Data for listings in Milan
* **summary_listings.csv**: Summary information and metrics for listings in Milan (good for visualisations).
* **summary_reviews.csv**: Summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing).
* **neighbourhoods.csv**: Neighbourhood list for geo filter. Sourced from city or open source GIS files.
* **neighbourhoods.geojson**: GeoJSON file of neighbourhoods of the city.

To map the neighbourhood in the dataset to the real neighbourhood I have created the file **data/quartieri.txt** which contains the real neighbourhood of Milan.